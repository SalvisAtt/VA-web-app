# app/main.py

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Model for a single message
class Message(BaseModel):
    role: str
    content: str

# Return a dummy response from the Virtual Assistant
@app.post("/send_message/")
async def send_message(message: Message):
    return {"assistant_response": "This is a test response from your Virtual Assistant"}

# Return a dummy conversation history - 5 messsages from the user, and 5 from the assistant
@app.get("/conversation_history/")
async def get_conversation_history():
    conversation_history = [
        {"role": "user", "content": "Hello!"},
        {"role": "assistant", "content": "Hi! How can I help you today?"},
        {"role": "user", "content": "Can you help me with my homework?"},
        {"role": "assistant", "content": "Sure! What subject are you working on?"},
        {"role": "user", "content": "Math."},
        {"role": "assistant", "content": "I can help with that! What's the question?"},
        {"role": "user", "content": "What is 5 + 7?"},
        {"role": "assistant", "content": "The answer is 12."},
        {"role": "user", "content": "Thanks!"},
        {"role": "assistant", "content": "You're welcome!"}
    ]
    return {"conversation_history": conversation_history}
