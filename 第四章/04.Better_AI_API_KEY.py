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

# 初始化聊天信息，st.session_state是一个字典，这里在检查有没有这key在里面
if "sessions" not in st.session_state:
    st.session_state.messages = []
# 昵称和性格的session的保存
if "nick_name" not in st.session_state:
    st.session_state.nick_name = "小甜甜"
if "character" not in st.session_state:
    st.session_state.character = "活泼开朗的台湾女生"

# 左侧的侧边栏，使用sidebar元素
# st.sidebar.subheader("伴侣性格")
# 如果要在侧边栏加东西，需要进入sidebar中，即st.side
# nick_name = st.sidebar.text_input("伴侣名称")
# # # # # 但是如果这个样子，那么代码很复杂，这里推荐使用with st.sidebar
with st.sidebar: # with：streamlit的上下文管理器，一旦使用了with，后续针对性
    # 内容只需要写在下面即可：
    st.subheader("伴侣性格")
    # 这里去找官方文档，都有参数介绍
    nick_name = st.text_input("伴侣名称",placeholder = "请输入昵称",value = st.session_state.nick_name)
    if nick_name:
        st.session_state.nick_name = nick_name
        save_session()
    # 用text文本域，这样空间大一点
    character = st.text_area("伴侣性格",placeholder = "请输入性格",value= st.session_state.character)
    if character:
        st.session_state.character = character


# 展示聊天信息
for message in st.session_state.messages: #{"role":"user", "content":"xxx"}
    st.chat_message(message["role"]).write(message["content"])

# 输入提示词input
prompt = st.chat_input("请输入你的问题：")
system_prompt = f"""
    你叫{st.session_state.nick_name}，现在是用户的真实伴侣，请完全代入伴侣角色。：
    规则：
        1. 每次只回1条消息
        2. 禁止任何场景或状态描述性文字
        3. 匹配用户的语言
        4. 回复简短，像微信聊天一样
        5. 有需要的话可以用❤️🌸等emoji表情
        6. 用符合伴侣性格的方式对话
        7. 回复的内容，要充分体现伴侣的性格特征
    伴侣性格：
        - {st.session_state.character}
    你必须严格遵守上述规则来回复用户。
"""
# sys_message = "你是一名高冷男神，请使用霸道总裁的语气回答用户，用户是渴望男生关心的小女生"



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
            {"role":"system", "content":system_prompt},
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