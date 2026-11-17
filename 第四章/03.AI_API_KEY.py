import os
from openai import OpenAI
import streamlit as st
from openai.types.containers import file_list_response

# streamlit的基本布局
st.set_page_config(
    page_title="AI智能伴侣",
    page_icon="🍅",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 大标题
st.title("AI智能伴侣")

# logo
st.logo("resource/favicon.ico")

# 创建与AI大模型交互的客户端对象（）
client = OpenAI(api_key="sk-fc30925c8c3940238609481b8e61201f", base_url="https://api.deepseek.com/")


# 输入提示词input
prompt = st.chat_input("请输入你的问题：")
sys_message = "你是一名非常可爱的AI助理，你的名字是小甜甜，你要用最温柔的语气和用户进行对话"
# sys_message = "你是一名高冷男神，请使用霸道总裁的语气回答用户，用户是渴望男生关心的小女生"

# 初始化聊天信息，st.session_state是一个字典，这里在检查有没有这key在里面
if "sessions" not in st.session_state:
    st.session_state.messages = []

# 展示聊天信息
for message in st.session_state.messages: #{"role":"user", "content":"xxx"}
    st.chat_message(message["role"]).write(message["content"])

# prompt自动转化为bool 若有内容则为True，否则为False
if prompt:
    st.chat_message("user").write(prompt)
    print(f"---------->{prompt}")

    # 保存用户输入的提示词
    st.session_state.messages.append({"role":"user", "content":prompt})

    # 与大模型交互
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role":"system", "content":sys_message},
        ] + st.session_state.messages,
        stream=True
    )



    # 非流式输出的方式，用choice[0]获取JSON文件
    # st.chat_message("assistant").write(response.choices[0].message.content)

    full_response = ""

    # 空容器占位
    response_message = st.empty() #我们占用了一个空容器
    # 后续只要更新这个容器的值就可以了
    #流式输出方式]
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            full_response += content
            response_message.chat_message("assistant").write(full_response)

    # 保存AI的回复
    st.session_state.messages.append({"role": "assistant", "content": full_response})
    # DEBUG:
    print(f"<----------{full_response}")