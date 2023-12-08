import os
from openai import AzureOpenAI
import numpy as np
client = AzureOpenAI(
    azure_endpoint="https://openai-llm-westeurope.openai.azure.com/",
    api_version="2023-07-01-preview",
    api_key=os.environ["OPENAI_API_KEY"]
)
#audio-demo
audio_file=open("/home/isuru/virtusa.udemy.com/audio/sample_french.mp3","rb")
response=client.audio.transcriptions.create(model="whisper",file=audio_file)
print(response)