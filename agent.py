from dotenv import load_dotenv
load_dotenv()
from anthropic import Anthropic

client = Anthropic()
model="claude-sonnet-4-6"
print(load_dotenv())

#making an initial message list with empty messages
messages = []

# made an helper function to add user message to the messages list
def add_user_message(messages, text):
    user_message = {"role":"user","content":text}
    messages.append(user_message)

# made an helper function to add assistant message to messages list 
def add_assistant_message(messages, text):
    assistant_message={"role":"assistant", "content":text}
    messages.append(assistant_message)


# made the api call into a function that passes the list of  messages to the api 
# call parameter named "messages" and passes 
# the messages list to the claude so that it remembers the context which creates the multi turn aspect.
def chat(messages):
    
    message = client.messages.create(
        
            model=model,
            max_tokens=1000,
            messages = messages    
    )
    return message.content[0].text


# Step 1
# lets first add the user message to the messages list.
add_user_message(messages, "Hello,whats is 2 + 3? give answer in one word")

# Step 2 send the user message to claude and store the response in a variable called answer
# as the claude call function chat() returns a text.

answer = chat(messages)
    
# Step 3 , now we store the reply/message from the caude/assistant into the messages list we 
# use the helper ffunction we made for adding assisnta message to the messages list 

add_assistant_message(messages,answer)

# Step 4 lets print and see how our messages list looks after adding user and assisnat message
# into the messages list
print(messages);

# Step 5 now again send a message to the claude with context
#  of previous question=(messages) and ask another question linked to it

add_user_message(messages,"what will be the answer if we add 7 more to the sum you have given previously")

answer = chat(messages)

add_assistant_message(messages,answer)

print(messages);


####RESPONSE######
# True
# [{'role': 'user', 'content': 'Hello,whats is 2 + 3? give answer in one word'}, {'role': 'assistant', 'content': '**Five**'}]
# [{'role': 'user', 'content': 'Hello,whats is 2 + 3? give answer in one word'}, {'role': 'assistant', 'content': '**Five**'},
#  {'role': 'user', 'content': 'what will be the answer if we add 7 more to the sum you have given previously'},
#  {'role': 'assistant', 'content': '**Twelve**'}]
