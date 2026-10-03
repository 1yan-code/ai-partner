import streamlit as st
import os
from openai import OpenAI

#设置页面配置项
st.set_page_config(
    page_title="AI Partner",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={}
)

#大标题
st.title("AI智能伴侣")

#Logo
st.logo("resources/logo.jpg")


#系统提示词
system_prompt="你是一个幽默的助手，你叫小丑"

#创建与AI大模型交互的客户端对象（DEEPSEEK_API_KEY是环境变量名）
client = OpenAI(
    api_key=os.environ.get('aipy_DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

#输入框
prompt = st.chat_input("请输入您的问题：")
if prompt:
    st.chat_message("user").write(prompt)
    print("---------->调用AI大模型，提示词: ",prompt)

    # 调用AI大模型
    response = client.chat.completions.create(
        model="deepseek-flash",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ],
        stream=False,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}}
    )

    # 输出大模型返回的结果
    print("<--------- 大模型返回的结果： ",response.choices[0].message.content)
    st.chat_message("ai").write(response.choices[0].message.content)

