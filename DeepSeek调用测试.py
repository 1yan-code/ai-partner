import os
from openai import OpenAI

#创建与AI大模型交互的客户端对象（DEEPSEEK_API_KEY是环境变量名）
client = OpenAI(
    api_key=os.environ.get('aipy_DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

#调用AI大模型
response = client.chat.completions.create(
    model="deepseek-flash",
    messages=[
        {"role": "system", "content": "你是一个幽默的助手，你叫小丑"},
        {"role": "user", "content": "你好，你叫什么"},
    ],
    stream=False,
    reasoning_effort="high",
    extra_body={"thinking": {"type": "enabled"}}
)

#输出大模型返回的结果
print(response.choices[0].message.content)