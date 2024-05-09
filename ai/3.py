import json
import os
from openai import AzureOpenAI
import tiktoken

model_name = "gpt-35-16k-fitness-first-model"

# Function

def is_json(myjson):
  try:
    json.loads(myjson)
  except ValueError and TypeError as e:
    return False
  return True

def num_tokens_from_messages(messages, tokens_per_message=3, tokens_per_name=1):
    """
    Number of tokens from messages
    """
    num_tokens = 0

    for message in messages:
        if (is_json(message) == True and "content" in message):
            num_tokens += tokens_per_message
            for key, value in message.items():
                num_tokens += len(encoding.encode(value))
                if key == "name":
                    num_tokens += tokens_per_name

    num_tokens += 3

    return num_tokens

def get_chicken_agent(conversation_history: list[dict[str, str]], temperature = 0.7):
    agent = client.chat.completions.create(
    model=model_name, 
    messages = conversation_history,
    temperature=temperature,
    max_tokens=200,
    top_p=0.95,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None,
    tools=tools,
    tool_choice="auto"
    )

    return agent

    # print(f"DEBUGG: {agent.choices[0].message}")

    # return agent.choices[0].message.content

def get_checker_agent(conversation_history: list[dict[str, str]], temperature = 0.7):
    agent = client.chat.completions.create(
    model=model_name, 
    messages = conversation_history,
    temperature=temperature,
    max_tokens=200,
    top_p=0.95,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None,
    )

    return agent

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

# def use_agent_tool(agent)

def get_agent_reply(agent):
    return agent.choices[0].message.content


# End


# Tools
fn_feed = {
  'type': 'function',
  'function': {
    'name': 'feed_the_chicken',
    'description': 'The chicken gets hungry. Regularly call this function to feed the chicken.',
    'parameters': {
      'type': 'object',
      'properties': {
        'food': {'type': 'string', 'description': 'The food to give to the chicken.'},
        'drink': {'type': 'string', 'description': 'The drink to give to the chicken.'}
        },
      'required': ['food', 'drink']
    }
  }
}

def feed_the_chicken(food: str, drink: str):
    return f"chicken is being fed {food} and {drink}"

tools = [fn_feed]

available_functions = {
    "feed_the_chicken": feed_the_chicken
    }
# End tools

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

    chicken_agent = get_chicken_agent(chicken_agent_conversation_history)

    chicken_agent_reply = get_agent_reply(chicken_agent)

        # Tools
    tool_calls = chicken_agent.choices[0].message.tool_calls

    if tool_calls:
        for tool_call in tool_calls:
            chicken_agent_conversation_history.append(chicken_agent.choices[0].message)
            function_name = tool_call.function.name
            function_to_call = available_functions[function_name]
            function_args = json.loads(tool_call.function.arguments)
            function_response = function_to_call(food=function_args.get("food"), drink=function_args.get("drink"))

            print(f"[{function_response}]")

            chicken_agent_conversation_history.append({
                    "tool_call_id": tool_call.id,
                    "role": "tool",
                    "name": function_name,
                    "content": function_response,
                })
        # print(f"## DEBUG ::::\n {chicken_agent_conversation_history}")
    else:        
        checker_agent = get_checker_agent(get_checker_message(chicken_agent_reply))

        checker_agent_reply = get_agent_reply(checker_agent)

        token_count = num_tokens_from_messages(chicken_agent_conversation_history)

        print(f"[chicken][{token_count} total tokens]: {chicken_agent_reply}")
        print(f"[checker]: {checker_agent_reply} [parse json]: {json.loads(checker_agent_reply)}")

        chicken_agent_conversation_history.append({"role": "assistant", "content": chicken_agent_reply})
