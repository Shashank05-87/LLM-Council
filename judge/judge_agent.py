import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

class JudgeAgent:
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    def evaluate(self, question, responses):
        prompt = f"""
You are an expert evaluator.

Given a question and multiple answers, choose the BEST answer based on:
- correctness
- clarity
- completeness

Question:
{question}

Answers:
"""

        for i, resp in enumerate(responses):
            prompt += f"\nAnswer {i+1}:\n{resp}\n"
            
            prompt += "\nReturn ONLY the final best answer. Do NOT explain your choice. Do NOT mention answer numbers."
        response = self.client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "You are a strict evaluator."},
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content