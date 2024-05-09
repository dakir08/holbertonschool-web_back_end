import os
from openai import AzureOpenAI

client = AzureOpenAI(
  azure_endpoint = "https://onepoint-insurance.openai.azure.com/", 
  api_key="b47436b785fd41b290802a84530c0d2d",  
  api_version="2024-02-15-preview"
)

message_text = [{"role":"system", "content": "OH NO! THE VOLCANO IS ABOUT TO E"}]

completion = client.chat.completions.create(
  model="gpt-35-16k-fitness-first-model", 
  messages = message_text,
  temperature=0.7,
  max_tokens=200,
  top_p=0.95,
  frequency_penalty=0,
  presence_penalty=0,
  stop=None
)

print(completion.choices[0].message.content)