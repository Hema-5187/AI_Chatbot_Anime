import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Groq API client
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

def get_anime_reply(user_input):
    """Send user input to Groq API and return reply."""
    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {"role": "system", "content": "You are an Anime bot, answer only anime-related queries."},
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message.content
