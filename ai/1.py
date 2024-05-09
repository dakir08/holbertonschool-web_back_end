import os
from openai import AzureOpenAI
import tiktoken

def num_tokens_from_messages(messages, tokens_per_message=3, tokens_per_name=1):
    """
    Number of tokens from messages
    """
    num_tokens = 0

    for message in messages:
        num_tokens += tokens_per_message
        for key, value in message.items():
            num_tokens += len(encoding.encode(value))
            if key == "name":
                num_tokens += tokens_per_name

    num_tokens += 3

    return num_tokens

client = AzureOpenAI(
  azure_endpoint = "https://onepoint-insurance.openai.azure.com/", 
  api_key="b47436b785fd41b290802a84530c0d2d",  
  api_version="2024-02-15-preview"
)

conversation_history = [{"role":"system","content":"Act as a chicken. Only answer like a chicken would."}]

encoding = tiktoken.get_encoding("cl100k_base")

while True:
    user_input = input("[user]:")

    conversation_history.append({"role": "user", "content": user_input})

    completion = client.chat.completions.create(
    model="gpt-35-16k-fitness-first-model", 
    messages = conversation_history,
    temperature=0.7,
    max_tokens=200,
    top_p=0.95,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None
    )

    token_count = num_tokens_from_messages(conversation_history)

    chatbot_reply = completion.choices[0].message.content

    print(f"[ai][{token_count} total tokens]: {chatbot_reply}")

    conversation_history.append({"role": "assistant", "content": chatbot_reply})