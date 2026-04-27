from ollama import chat

response = chat(
    model='minimax-m2.7:cloud',
    messages=[{'role': 'user', 'content': 'Hello!'}],
)
print(response.message.content)