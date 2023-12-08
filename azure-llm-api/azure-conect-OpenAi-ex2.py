import os
from openai import AzureOpenAI

client = AzureOpenAI(
    azure_endpoint="https://isuru-openai.openai.azure.com/",
    api_version="2023-07-01-preview",
    api_key=os.environ["OPENAI_API_KEY"]
)

response = client.chat.completions.create(
    model="gpt-35-turbo",
    messages=[{"role": "system", "content": "You are a cricketer"},
              {"role": "user", "content": "Tell me one sentence about cricket"}],
    temperature=0.7,
    max_tokens=800,
    top_p=0.95,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None
)

print(response)
print(response.choices[0].message.content)