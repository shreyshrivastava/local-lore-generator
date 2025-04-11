import os
from dotenv import load_dotenv
from groq import Groq
import openai

# Load API keys from .env or Hugging Face secrets
load_dotenv()

# Groq client for LLaMA 4
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def query_llama4_story(prompt: str) -> str:
    try:
        response = client.chat.completions.create(
            model="meta-llama/llama-4-scout-17b-16e-instruct",
            messages=[
                {"role": "system", "content": "You are a masterful Indian mythological storyteller."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_completion_tokens=700,
            top_p=1,
            stream=False
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ Error generating story: {e}"

# OpenAI setup for DALL·E
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_image(prompt: str) -> str:
    try:
        response = openai.Image.create(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1
        )
        return response["data"][0]["url"]
    except Exception as e:
        print("❌ Image generation error:", e)
        return None
