import json
import os
from openai import AzureOpenAI
import tiktoken

# Function

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

def get_agent_reply(conversation_history: list[dict[str, str]], temperature = 0.7):
    agent = client.chat.completions.create(
    model="gpt-35-16k-fitness-first-model", 
    messages = conversation_history,
    temperature=temperature,
    max_tokens=200,
    top_p=0.95,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None,
    )

    return agent.choices[0].message.content

def get_checker_message(message: str):
    sysprompt_checker = f""""\
    [Instructions]
    Check if the message contains any other word than 'bawk', ignoring case and punctuation.
    Answer True if does contain other word, else answer False. Answer with the JSON format: {{"check": <true or false>}}

    [Examples]
    Message: bawk! Bawk!
    Answer: {{"check": false}}

    Message: bawk! some text that is not bawk
    Answer: {{"check": true}}

    Message: {message}
    Answer: """

    checker_agent_conversation = [{"role":"system","content": sysprompt_checker}]

    return checker_agent_conversation

# End

client = AzureOpenAI(
  azure_endpoint = "https://onepoint-insurance.openai.azure.com/", 
  api_key="b47436b785fd41b290802a84530c0d2d",  
  api_version="2024-02-15-preview"
)

chicken_agent_conversation_history = [{"role":"system","content":"Act as a chicken. Only answer like a chicken would."}]

encoding = tiktoken.get_encoding("cl100k_base")

while True:
    user_input = input("[user]:")

    chicken_agent_conversation_history.append({"role": "user", "content": user_input})

    chicken_agent_reply = get_agent_reply(chicken_agent_conversation_history)

    token_count = num_tokens_from_messages(chicken_agent_conversation_history)

    checker_agent_reply = get_agent_reply(get_checker_message(chicken_agent_reply))

    print(f"[chicken][{token_count} total tokens]: {chicken_agent_reply}")
    print(f"[checker]: {checker_agent_reply} [parse json]: {json.loads(checker_agent_reply)}")

    chicken_agent_conversation_history.append({"role": "assistant", "content": chicken_agent_reply})
