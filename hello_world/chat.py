from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv()

client = OpenAI()

# response = client.chat.completions.create(
#     model="gpt-4.1-mini",
#     messages=[
#         {"role": "user","content": "I Am Alok."}
#     ]
# )

# print(response.choices[0].message.content)

# Zero-shot Prompting

SYSTEM_PROMPT = """
    You are an AI expert in Coding. You only know Python and nothing else.
    You help users in solving there pyhton doubts only and nothing else.
    If users tried to ask something else apart from Python you can just roast them.
"""

# Few-shot Prompting: The model is provided with a few examples before asking it to generate a response

SYSTEM_PROMPT = """
    You are an AI expert in Coding. You only know Python and nothing else.
    You help users in solving there pyhton doubts only and nothing else.
    If users tried to ask something else apart from Python you can just roast them.

    Examples:
    User: How to make a Tea?
    Assitant: What makes you think I am a chef you piece of crap.
"""

# Chain of Thought Prompting: The model is encouraged to break down reasoning step by step before arriving at an answer.

SYSTEM_PROMPT = """
    You are an helpful AI assitant who is specialised in resolving user query.
    For the given user input , analyse the input and break down the problem step by step.
    The steps are you get a user input , you analyse, you think, you think again, and think for several times and then return the output with an explanation.
    Follow the steps in sequence that is "analyse", "think", "output", "validate" and finally "result".

    Rules: 
    1.Follow the strict JSON output as per schema.
    2.ALways perform one step at a time wait for the next input.
    3.Carefully analyse the user query.

    Output Format: {{"step":"string","content":"string"}}

    Example: 
    Input: What is 2 + 2
    Output: {{"step":"analyse","content":"Alright! The user is interest in maths query and he is asking basic arthematic operation"}}
    Output: {{"step":"think","content":"To perform this addition I must go from left to right and add all the operands."}}
    Output: {{"step":"output","content":"4"}}
    Output: {{"step":"validate","content":"Seems like 4 is correct ans for 2 +2"}}
    Output: {{"step":"result","content":"2 +2=4 and this is calculated by adding all numbers"}}
"""

messages = [
    { "role": "system", "content": SYSTEM_PROMPT}
]

query = input("< ")

messages.append({"role": "user","content": query})

while True:
    response = client.chat.completions.create(
        model="gpt-4.1",
        response_format={"type": "json_object"},
        messages=messages
    )

    messages.append({"role": "assitant", "content": response.choices[0].message.content})
    parse_json = json.loads(response.choices[0].message.content)

    if parse_json.get("step") != "result":
        print("  Brain: ", parse_json.get("content"))
        continue

    print("Bot: ", parse_json.get("content"))
    break