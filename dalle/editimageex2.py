import os
import requests
from openai import OpenAI

client = OpenAI()
response = client.images.edit(model="dall-e-2", image=open("/home/isuru/virtusa.udemy.com/genai.png", "rb"), mask=open("/home/isuru/virtusa.udemy.com/genai.png", "rb"),  prompt="A sunlit indoor lounge area with a pool containing a flamingo",  n=1,  size="1024x1024")
#response = client.images.edit(model="dall-e-2", image=open("/home/isuru/virtusa.udemy.com/genai.png", "rb"),  prompt="A sunlit indoor lounge area with a pool containing a flamingo",  n=1,  size="1024x1024")
url = response.data[0].url




data = requests.get(url).content

f = open('/home/isuru/virtusa.udemy.com/output/img.png','wb')

f.write(data)
f.close()