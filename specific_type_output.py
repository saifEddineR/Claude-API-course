# test_groq.py
# test_groq.py
from groq import Groq
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def add_user_message(messages, content):
    user_message = {"role": "user", "content": content}
    messages.append(user_message)
    
def add_assistant_message(messages, content):
    assistant_message = {"role": "assistant", "content": content}
    messages.append(assistant_message)
    
def chat(messages):
    response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",  # <-- Changed this
    messages=messages,
    temperature=1.0,
    )
    return response.choices[0].message.content
    

# Claude use the assistant message to provide the initial response to start only with json 
# and use stop sequence to stop with the end of the json format
# message = "generate an ansible playbook to install nginx on ubuntu in yaml format"
# add_user_message(messages, message)
# add_assistant_message(messages, "```json")
# answer = chat(messages, stop_sequences=["```"])
# json.loads(answer.strip())
# starting list of messages
messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant. Respond with ONLY valid JSON. Do not use markdown or code fences."
    },
    {
        "role": "user",
        "content": "Generate an Ansible playbook to install nginx on Ubuntu."
    }
]


answer = chat(messages)
print(answer)
