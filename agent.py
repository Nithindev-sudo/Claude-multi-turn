from dotenv import load_dotenv
load_dotenv()
from anthropic import Anthropic

client = Anthropic()
model="claude-sonnet-4-6"
print(load_dotenv())
message = client.messages.create(
    
        model=model,
        max_tokens=999,
        messages = [
            {
                "role" : "user",
                "content" : "Hi can you tell me what is meant by an MCP or controller in claude terms? give answer in one sentence"
            }
        ]
    
)

print(message.content[0].text)

