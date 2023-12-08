import os
from openai import AzureOpenAI

client = AzureOpenAI(
    azure_endpoint="https://isuru-openai.openai.azure.com/",
    api_version="2023-07-01-preview",
    api_key=os.environ["OPENAI_API_KEY"]
)
response= client.embeddings.create(model="text-embedding-ada-002",input="cat ")
print(response)
print([response.data[0].embedding])