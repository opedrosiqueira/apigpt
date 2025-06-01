import tiktoken
from openai import OpenAI
import pprint
from typing import List, Dict, Any

# Model definitions
MODELS: List[Dict[str, str]] = [
    {
        "name": "o1-mini",
        "obs": "Input Context Length 128,000 tokens. Output Context Length 65,536 tokens. Input Price $3 per 1M Tokens. Output Price $12 per 1M Tokens. Knowledge Cutoff 2023-09."
    },
    {
        "name": "gpt-4o-mini",
        "obs": "Input Context Length 128,000 tokens. Output Context Length 16,384 tokens. Input Price $0.15 per 1M Tokens. Output Price $0.60 per 1M Tokens. Knowledge Cutoff 2023-10-01."
    },
    {
        "name": "gpt-4.1-nano",
        "obs": "Input Context Length 1,047,576 tokens. Output Context Length 32,768 tokens. Input Price $0.10 per 1M Tokens. Output Price $0.40 per 1M Tokens. Knowledge Cutoff 2024-05-31."
    }
]

def count_tokens(text: str, encoding_name: str = "cl100k_base") -> int:
    """Count the number of tokens in a string using the specified encoding."""
    encoding = tiktoken.get_encoding(encoding_name)
    return len(encoding.encode(text))

def select_model(num_tokens: int) -> str:
    """Prompt user to select a model."""
    print(f"\nText with {num_tokens} tokens. Which model do you want?")
    print("0. List available models and exit")
    print("1. Other (must inform)")
    for idx, model in enumerate(MODELS, 2):
        print(f"{idx}. {model['name']}: {model['obs']}")
    try:
        choice = int(input("Choice: "))
    except ValueError:
        return select_model(num_tokens)
    if choice == 0:
        return "LIST"
    elif choice == 1:
        return input("Inform the model: ")
    elif 2 <= choice < len(MODELS) + 2:
        return MODELS[choice - 2]["name"]
    else:
        return select_model(num_tokens)

def list_models(client: OpenAI) -> Any:
    """List available models from the OpenAI client."""
    return client.models.list()

def ask(client: OpenAI, question: str, model: str) -> Any:
    """Send a question to the OpenAI API using the specified model."""
    response = client.responses.create(model=model, input=question)
    return response

def main():
    client = OpenAI()
    file_path = input("Input file (leave blank to load from ./input.html): ") or "./input.html"
    with open(file_path, "r", encoding="utf-8") as file:
        question = file.read()

    token_count = count_tokens(question)
    model_choice = select_model(token_count)

    if model_choice == "LIST":
        pprint.pprint(list_models(client))
        print("Exiting...")
        return

    print(f"Using '{model_choice}' for {token_count} tokens")
    response = ask(client, question, model_choice)
    data_to_save = response.output_text

    pprint.pprint(response)
    output_path = input("Output file (leave blank to save to ./output.md): ") or "./output.md"
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(data_to_save)

if __name__ == "__main__":
    main()
