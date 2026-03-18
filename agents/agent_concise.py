import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

class ConciseAgent:
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    def answer(self, question: str) -> str:
        response = self.client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "system",
                    "content": "You are a concise assistant. Answer briefly and clearly in 2-3 sentences."
                },
                {
                    "role": "user",
                    "content": question
                }
            ]
        )
        return response.choices[0].message.content