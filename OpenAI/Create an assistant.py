#this code simply creates an assistant with the name "Math Tutor3" and the instructions "You are a personal math tutor. Write and run code to answer math questions."
from openai import OpenAI
client = OpenAI()

assistant = client.beta.assistants.create(
  name="Math Tutor3",
  instructions="You are a personal math tutor. Write and run code to answer math questions.",
  tools=[{"type": "code_interpreter"}],
  model="gpt-4o",
)

#ExbordiaBOT Assistant ID: asst_OeWmert08cExBONl6dQcvZyq