import os
from openai import AzureOpenAI
import numpy as np
client = AzureOpenAI(
    azure_endpoint="https://openai-llm-westeurope.openai.azure.com/",
    api_version="2023-07-01-preview",
    api_key=os.environ["OPENAI_API_KEY"]
)
#audio-demo
audio_file=open("/home/isuru/virtusa.udemy.com/audio/aws_lambda.mp3","rb")
response=client.audio.transcriptions.create(model="whisper",file=audio_file)
print(response)

response = client.chat.completions.create(
    model="text-demo",
    messages=[
              {"role": "user", "content": "Summarize the text to 2 bullet points. "+ response} ],n=3,
  
)

print(response)
print(response.choices[1].message.content)