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
    
def chat(messages):
    tone = """
    You are a fitness coach. You will provide advice on exercise, nutrition, and overall wellness. 
    Your responses should be informative, and tailored to the user's needs.
    """
    add_user_message(messages, tone)
    response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",  # <-- Changed this
    messages=messages,
    temperature=1.0,
    )
    return response.choices[0].message.content
    
# starting list of messages
messages = []
while True:
    user_input = input("> ")
    if user_input.lower() == "exit":
        break
    add_user_message(messages, user_input)
    answer = chat(messages)
    print(answer)
    print("--------------------------------------------------")
    add_assitant_message(messages, answer)

