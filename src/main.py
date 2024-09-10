#!/usr/bin/python

import os
import openai
from dotenv import dotenv_values

# Set up OpenAI credentials

CONFIG = dotenv_values(".env")

OPEN_AI_KEY = CONFIG["KEY"] or os.environ["OPEN_AI_KEY"]
OPEN_AI_ORG = CONFIG["ORG"] or os.environ["OPEN_AI_ORG"]

openai.api_key = OPEN_AI_KEY
openai.organization = OPEN_AI_ORG

def load_file(filename: str = "") -> str:
    """Loads an arbitrary file name"""
    with open(filename, "r") as fh:
        return fh.read()

def main():

    # Load source file
    source = load_file("data/source.txt")
    prompt = load_file("data/prompt.txt")

    # Create constraint
    constraint = f"{prompt}\n{source}"

    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": constraint}
        ],
        # "Level of risk" associated with model predictions
        temperature = 0.9,
        top_p = 1,
        # Maximum size of requests
        max_tokens = 100,
        # Number of results to attempt and return
        n = 1
    )

    # Extract the response text
    result = response.choices[0].message.content

    print(result)
    
if __name__ == "__main__":
    main()