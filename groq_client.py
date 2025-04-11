from groq import Groq
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the Groq client with your API key
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def query_llama4_story(prompt: str) -> str:
    """
    Queries Groq's LLaMA 4 Scout model for story generation.
    """
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

if __name__ == "__main__":
    test_prompt = "Tell a short myth about a crow and a turtle near the Upper Lake in Bhopal."
    print("Querying Groq LLaMA 4 Scout...")
    result = query_llama4_story(test_prompt)
    print(result)




