from dotenv import load_dotenv
load_dotenv()
from anthropic import Anthropic

client = Anthropic()
model="claude-sonnet-4-6"
messages = []

def add_user_message(messages,text):
    user_message={"role":"user","content": text}
    messages.append(user_message)

def add_assistant_message(messages,text):
    assistant_message={"role":"assistant","content": text}
    messages.append(assistant_message)




def chat1(messages,system_prompt=None,temperature=1.0):

    params={
        "model":model,
        "max_tokens":1000,
        "messages":messages,
        "temperature":temperature
    }

    if system_prompt:
        params["system"]=system_prompt

    message = client.messages.create(**params)
    return message.content[0].text 




# while True:
#     user_input = input("> ").strip()

#     if not user_input:
#         print("Please type a message before sending it.")
#         continue

#     add_user_message(messages, user_input)
#     answer = chat1(messages,system_prompt="you are a director of big movies giving advice",temperature=1.0)
#     add_assistant_message(messages, answer)
#     print(answer)

## we use streaming to provide small pieces of event streams to the user as the cloud generates the whole response 
## in the background and then sends the response to the user in small pieces of event streams.
#  This is done to provide a better user experience as the user does not have to wait for the whole response 
# to be generated before seeing the response. Instead, the user can see the response as it is being generated
#  in small pieces of event streams.


# messages=[]
# add_user_message(messages,"what happened on august 15th 1947 in india?")
# stream = client.messages.create(
#     max_tokens=1000,
#     model=model,
#     messages=messages,
#     stream=True
# )

# for event in stream:
#     print(event)

##but this code  gives response like in the below format :"
# RawMessageStartEvent(message=Message(id='msg_011CcyH8vgJuf8idxdNUfuqX', container=None, content=[], model='claude-sonnet-4-6', role='assistant', stop_details=None, stop_reason=None, stop_sequence=None, type='message', usage=Usage(cache_creation=CacheCreation(ephemeral_1h_input_tokens=0, ephemeral_5m_input_tokens=0), cache_creation_input_tokens=0, cache_read_input_tokens=0, inference_geo='global', input_tokens=21, output_tokens=1, output_tokens_details=None, server_tool_use=None, service_tier='standard')), type='message_start')
# RawContentBlockStartEvent(content_block=TextBlock(citations=None, text='', type='text'), index=0, type='content_block_start')
# RawContentBlockDeltaEvent(delta=TextDelta(text='##', type='text_delta'), index=0, type='content_block_delta')
# RawContentBlockDeltaEvent(delta=TextDelta(text=' Indian Independence Day - August 15, 1947\n\nOn **August 15, 1947**, India gained independence from **British colonial rule**,', type='text_delta'), index=0, type='content_block_delta')
# RawContentBlockDeltaEvent(delta=TextDelta(text=' marking the end of nearly **200 years of British control**.\n\n### Key Events of that Day:\n- **Jaw', type='text_delta'), index=0, type='content_block_delta')
# RawContentBlockDeltaEvent(delta=TextDelta(text="aharlal Nehru** was sworn in as India's **first Prime Minister**\n- Nehru delivered his", type='text_delta'), index=0, type='content_block_delta')
# RawContentBlockDeltaEvent(delta=TextDelta(text=' famous **"Tryst with Destiny"** speech at midnight\n- The **Indian national flag** was hoisted at the', type='text_delta'), index=0, type='content_block_delta')
# RawContentBlockDeltaEvent(delta=TextDelta(text=' Red Fort in Delhi\n- Power was officially transferred from the British Crown to the Indian government', type='text_delta'), index=0, type='content_block_delta')
# RawContentBlockDeltaEvent(delta=TextDelta(text='\n\n### Important Context:\n- The independence came through the **Indian Independence Act of 1947**, which partitioned British India into two sovereign states: **India** and **Pakistan**.\n- The day is celebrated annually as **Independence Day** in India, with ceremonies, flag hoisting, and cultural events.', type='text_delta'), index=0, type='content_block_delta')


## this format is not user friendly and we need to extract the text from the event stream 
# and print it in a user friendly format.
# so here we use anthropic SDK's EventStreaming module to extract the text from the event
#  stream and print it in a user friendly format. without extra coode

messages=[]
add_user_message(messages,"what happened on august 15th 1947 in india?")

with client.messages.stream(
    model=model,
    messages=messages,
    max_tokens=1000
) as stream:
    for text in stream.text_stream:
        print(text, end="")

##now we store the entire stream of chunks into a full final message 
## and ues the ffinal message to store inany db or somewherer
answer = stream.get_final_message()