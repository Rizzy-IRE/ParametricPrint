import os
from openai import OpenAI
from dotenv import load_dotenv

# Load your .env file if you have one
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_script(description):
    prompt = f"""
    You are a CAD expert. Generate an OpenSCAD script based on the following description:
    Description: \"\"\"{description}\"\"\"
    The script must use parametric variables (like width = 20, height = 50, etc.).
    Include comments. Do not explain the code—only return the script.
    """

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a CAD expert that writes OpenSCAD scripts."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
    )

    return response.choices[0].message.content.strip()
