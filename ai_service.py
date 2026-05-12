from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv(override=True)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask_ai(question: str, history: list = []):

 # Step 1 — System prompt (bot personality)
    messages = [
        {
            "role": "system",
            "content": """You are a customer support agent for TechStore.
            Only answer questions related to orders, products, and refunds.
            Be professional and helpful."""
        }
    ]
    
    # Step 2 — DB se aayi history add karo
    messages.extend(history)

    # Step 3 — Current question add karo
    messages.append({"role": "user", "content": question})

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": question}]
    )
    return response.choices[0].message.content