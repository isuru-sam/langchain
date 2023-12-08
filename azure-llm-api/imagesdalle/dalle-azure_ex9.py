# Note: DALL-E 3 requires version 1.0.0 of the openai-python library or later
import os
from openai import AzureOpenAI
import json

client = AzureOpenAI(
    api_version="2023-12-01-preview",
    azure_endpoint="https://dalle-isuru.openai.azure.com",
    api_key=os.environ["OPENAI_API_KEY"],
)

result = client.images.generate(
    model="isuru-dalle3", # the name of your DALL-E 3 deployment
    prompt="cat on house roof",
    n=1
)

image_url = json.loads(result.model_dump_json())['data'][0]['url']
print(image_url)
