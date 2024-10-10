## This works to create a Thread in OpenAI, nevertheless, the thread is empty until now.
# The result in the termimanal is: 
# id='thread_Mez2qMmZ2wMk2sLHRQ87rMnn'

from openai import OpenAI
client = OpenAI()

message_thread = client.beta.threads.create(
  messages=[
    {
      "role": "user",
      "content": "Hello, what is AI?"
    },
    {
      "role": "user",
      "content": "How does AI work? Explain it in simple terms."
    },
  ]
)

print(message_thread)


