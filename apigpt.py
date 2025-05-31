import tiktoken
from openai import OpenAI
import pprint

# examples of questions
#
# translate to pt_br
# summarize in HTML format

model1 = "o1-mini"
model2 = "gpt-4o"


def menu(num_tokens):
    match int(
        input(
            f"""
text with {num_tokens} tokens. which model do you want?
1. {model1} (up to ??? token including question+answer)
2. {model2} (up to ??? token including question+answer)
3. other (must inform)
0. List available models and exit
"""
        )
    ):
        case 1:
            return f"{model1}"
        case 2:
            return f"{model2}"
        case 3:
            return 3
        case _:
            return 0


def num_tokens(string: str, encoding_name: str = "cl100k_base") -> int:
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens


def models():
    return client.models.list()


def chat(user_content, system_content="You are a helpful assistant.", model=f"{model1}"):
    response = client.responses.create(
        model=model,
        messages=[
            {"role": "system", "content": system_content},
            {"role": "user", "content": user_content},
        ],
    )

    return response


client = OpenAI()

question = input("what you want to know? ")

file_path = input("input file (leave blank to load from ./input.html): ") or "./input.html"
with open(file_path, "r", encoding="utf-8") as file:
    user_content = file.read()

num_tokens = num_tokens(user_content)

choice = menu(num_tokens)

if choice == 0:
    pprint.pprint(models())
    print("exiting...")
    quit()
elif choice == 3:
    model = input("inform the model: ")
else:
    model = choice

print("using", model, "for", num_tokens, "tokens")
completion = chat(user_content, question, model)

data_to_save = completion.choices[0]

# pprint.pprint(completion.choices[0].message.content)
print(completion.choices[0].message.content)
file_path = input("output file (leave blank to save to ./output.py): ") or "./output.py"
with open(file_path, "w", encoding="utf-8") as file:
    file.write(
        'from dataclasses import make_dataclass\nStock = make_dataclass("Stock", ("symbol", "current", "high", "low"))\n\nChatCompletionMessage=make_dataclass("ChatCompletionMessage", ("content","role","function_call","tool_calls","refusal"))\nChoice=make_dataclass("Choice",("finish_reason", "index", "logprobs", "message"))\n\nresult = '
    )
    file.write(str(data_to_save))
    file.write("\nprint(result.message.content)")
