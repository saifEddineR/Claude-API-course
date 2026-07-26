# test_groq.py
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def add_user_message(messages, content):
    user_message = {"role": "user", "content": content}
    messages.append(user_message)
    
def add_assitant_message(messages, content):
    assistant_message = {"role": "assistant", "content": content}
    messages.append(assistant_message)
    
messages = []

add_user_message(messages, "write a 1 sentence description of a fake database")
stream = client.chat.completions.create(
    model="llama-3.3-70b-versatile",  # <-- Changed this
    messages=messages,
    temperature=1.0,
    stream=True
)

for event in stream:
    if event.choices:
        delta = event.choices[0].delta.content
        if delta is not None:
            print(delta, end="", flush=True)