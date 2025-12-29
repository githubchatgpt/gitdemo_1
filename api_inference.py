import anthropic

client = anthropic.Anthropic(
    base_url='https://api-inference.modelscope.cn',
    api_key='ms-792fda96-2963-4df6-b3fb-5cd9b6515989',  # ModelScope Token
)

with client.messages.stream(
    model='Qwen/Qwen3-0.6B', # ModelScope Model-Id
    messages=[
        {
            "role": "user",
            "content": "你好"
        }
    ],
    max_tokens = 1024
) as stream:
  for text in stream.text_stream:
      print(text, end="", flush=True)