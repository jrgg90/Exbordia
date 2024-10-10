#Send a message to that Thread
#I believe this only sends the message, doesnt has a response

from openai import OpenAI
client = OpenAI()

message = client.beta.threads.messages.create(
  thread_id='thread_Mez2qMmZ2wMk2sLHRQ87rMnn',
  role="user",
  content="I need to solve the equation `3x + 11 = 14`. Can you help me?"
)
# The result in the termimanal is the answer of the assistant to the user's question.
print(message)



#message id='msg_glTBPUdB03f3pfFth8L0EMYk'
#thread_id='thread_Mez2qMmZ2wMk2sLHRQ87rMnn'