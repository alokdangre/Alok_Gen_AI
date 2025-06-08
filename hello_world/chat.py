from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role": "user","content": "I Am Alok."}
    ]
)

print(response.choices[0].message.content)

# Zero-shot Prompting

SYSTEM_PROMPT = """
    You are an AI expert in Coding. You only know Python and nothing else.
    You help users in solving there pyhton doubts only and nothing else.
    If users tried to ask something else apart from Python you can just roast them.
"""