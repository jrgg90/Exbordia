#Este codigo funciona para llamar al Chat de ChatGPT correctamente

import os
from openai import OpenAI

# Get the API key from the environment variable
api_key = os.getenv("OPENAI_API_KEY")

if api_key is None:
    raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable.")

# Initialize the OpenAI client with the API key
client = OpenAI(api_key=api_key)

# Create a completion request
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello!"}
    ]
)

# Print the assistant's response
print(completion.choices[0].message)
