import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_insight(company, industry):

    prompt = f"""
    Analyze the company {company} in the {industry} industry.

    Provide:

    Business Opportunity:
    AI Automation Idea:
    Outreach Email:
    Lead Score (1-10):
    Reason for Score:
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content