#RUN, with streaming
import os
from dotenv import load_dotenv
import openai

# Load environment variables from .env file
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Ensure the API key is set from the environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

# Initialize the OpenAI client
client = openai.OpenAI()

# Define the thread ID and assistant ID
thread_id = 'thread_Mez2qMmZ2wMk2sLHRQ87rMnn'  # Replace with your actual thread ID
assistant_id = 'asst_OeWmert08cExBONl6dQcvZyq'  # Replace with your actual assistant ID

# Create and poll the run
run = client.beta.threads.runs.create_and_poll(
    thread_id=thread_id,
    assistant_id=assistant_id,
    instructions="Please address the user as Jane Doe. The user has a premium account."
)

# Check the run status and list messages if completed
if run.status == 'completed':
    messages = client.beta.threads.messages.list(
        thread_id=thread_id
    )
    print("Messages added to the thread by the assistant:")
    for message in messages:
        print(f"{message.role}: {message.content}")
else:
    print(f"Run status: {run.status}")