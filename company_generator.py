import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_companies(industry, location, num):

    prompt = f"""
    List {num} companies in the {industry} industry located in {location}.
    Only return company names separated by commas.
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    text = response.choices[0].message.content

    companies = [c.strip() for c in text.split(",")]

    return companies