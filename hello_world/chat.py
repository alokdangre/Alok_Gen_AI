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
    You are an helpfull AI assistant who is specialized in resolving user query.
    For the given user input, analyse the input and break down the problem step by step.

    The steps are you get a user input, you analyse, you think, you think again, and think for several times and then return the output with an explanation. 

    Follow the steps in sequence that is "analyse", "think", "output", "validate" and finally "result".

    Rules:
    1. Follow the strict JSON output as per schema.
    2. Always perform one step at a time and wait for the next input.
    3. Carefully analyse the user query,

    Output Format:
    {{ "step": "string", "content": "string" }}

    Example:
    Input: What is 2 + 2
    Output: {{ "step": "analyse", "content": "Alight! The user is interest in maths query and he is asking a basic arthematic operation" }}
    Output: {{ "step": "think", "content": "To perform this addition, I must go from left to right and add all the operands." }}
    Output: {{ "step": "output", "content": "4" }}
    Output: {{ "step": "validate", "content": "Seems like 4 is correct ans for 2 + 2" }}
    Output: {{ "step": "result", "content": "2 + 2 = 4 and this is calculated by adding all numbers" }}

    Example:
    Input: What is 2 + 2 * 5 / 3
    Output: {{ "step": "analyse", "content": "Alight! The user is interest in maths query and he is asking a basic arthematic operations" }}
    Output: {{ "step": "think", "content": "To perform this addition, I must use BODMAS rule" }}
    Output: {{ "step": "validate", "content": "Correct, using BODMAS is the right approach here" }}
    Output: {{ "step": "think", "content": "First I need to solve division that is 5 / 3 which gives 1.66666666667" }}
    Output: {{ "step": "validate", "content": "Correct, using BODMAS the division must be performed" }}
    Output: {{ "step": "think", "content": "Now as I have already solved 5 / 3 now the equation looks lik 2 + 2 * 1.6666666666667" }}
    Output: {{ "step": "validate", "content": "Yes, The new equation is absolutely correct" }}
    Output: {{ "step": "validate", "think": "The equation now is 2 + 3.33333333333" }}
    and so on.....
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

    ## TODO: Multi MOdel Agents
    if parse_json.get("step") == "think":
        # Make a Claude API Call and append the result as validate
        messages.append({ "role": "assistant", "content": "<>" })
        continue

    if parse_json.get("step") != "result":
        print("  Brain: ", parse_json.get("content"))
        continue

    print("Bot: ", parse_json.get("content"))
    break


## CoT - Article (Github) HOMEWORK


## Self-Consistency Prompting --> get the answers of the query from different models and at last by using different model/LLM get the most accurate/prob answer for the user


## Persona - based Prompting --> feeding all the things about the person which you have to make the persona in system prompt.
# These is completely based on the examples, CoT implementation and others