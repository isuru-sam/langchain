import os
from openai import AzureOpenAI
import numpy as np
client = AzureOpenAI(
    azure_endpoint="https://isuru-openai.openai.azure.com/",
    api_version="2023-07-01-preview",
    api_key=os.environ["OPENAI_API_KEY"]
)
response= client.embeddings.create(model="text-embedding-ada-002",input="cat")
response2= client.embeddings.create(model="text-embedding-ada-002",input="dog")
print(response)
print(response2)
em1=response.data[0].embedding
em2=response2.data[0].embedding
similarity_score=np.dot(em1, em2)
print(similarity_score*100)