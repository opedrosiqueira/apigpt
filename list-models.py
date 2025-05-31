from openai import OpenAI

client = OpenAI()

for model in sorted(client.models.list(), key=lambda x: x.created):
    print(model)
