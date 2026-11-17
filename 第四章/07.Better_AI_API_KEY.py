import os
from openai import OpenAI
import streamlit as st
from openai.resources.beta.threads import messages
from openai.types.containers import file_list_response
import json
from datetime import datetime

from pandas.core.reshape import encoding
from streamlit import rerun

# streamlit的基本布局
st.set_page_config(
    page_title="AI智能伴侣",
    page_icon="🍅",
    layout="wide",
    initial_sidebar_state="expanded"
)

def save_session():
    if st.session_state.current_session and st.session_state.messages:
        with open(f"resource/sessions/{st.session_state.current_session}.json", "w") as f:
            session_data = {
                "nick_name": st.session_state.nick_name,
                "character": st.session_state.character,
                "current_session": st.session_state.current_session,
                "sessions": st.session_state.messages,
            }
            json.dump(session_data, f, indent=4)

# 加载所有的会话列表
def load_sessions():
    session_list = []
#     加载sessions目录文件
    if os.path.exists("resource/sessions"):
        file_list = os.listdir("resource/sessions")
        for file_name in file_list:
            if file_name.endswith(".json"):
                session_list.append(file_name[:-5])
    return session_list[::-1]

# 加载指定的会话数据
def load_session(session_name):
    try:
        if os.path.exists(f"resource/sessions/{session_name}.json"):
            with open(f"resource/sessions/{session_name}.json", "r", encoding = "utf-8") as f:
                session_data = json.load(f)
                st.session_state.nick_name = session_data["nick_name"]  # type: ignore
                st.session_state.character = session_data["character"]  # type: ignore
                st.session_state.current_session = session_data["current_session"]  # type: ignore
                st.session_state.messages = session_data["sessions"]  # type: ignore
    except Exception as e:
        st.error(f"加载会话失败！ {session_name}: {e}")

st.divider()


# 大标题
st.title("AI智能伴侣")

# logo
st.logo("resource/favicon.ico")

# 创建与AI大模型交互的客户端对象（）
client = OpenAI(api_key="sk-fc30925c8c3940238609481b8e61201f", base_url="https://api.deepseek.com/")

# 初始化聊天信息，st.session_state是一个字典，这里在检查有没有这key在里面
if "messages" not in st.session_state:
    st.session_state.messages = []
# 昵称和性格的session的保存
if "nick_name" not in st.session_state:
    st.session_state.nick_name = "小甜甜"
if "character" not in st.session_state:
    st.session_state.character = "活泼开朗的台湾女生"
# 会话保存
if "current_session" not in st.session_state:
    st.session_state.current_session = datetime.now().strftime("%Y%m%d_%H%M%S")
st.text(f"当前会话：{st.session_state.current_session}")
# 左侧的侧边栏，使用sidebar元素
# st.sidebar.subheader("伴侣性格")
# 如果要在侧边栏加东西，需要进入sidebar中，即st.side
# nick_name = st.sidebar.text_input("伴侣名称")
# # # # # 但是如果这个样子，那么代码很复杂，这里推荐使用with st.sidebar
with st.sidebar: # with：streamlit的上下文管理器，一旦使用了with，后续针对性
    # 内容只需要写在下面即可：
    # 会话信息
    st.subheader("AI控制面板")

    #     新建会话的按钮
    if st.button("新建会话", width="stretch",icon = "✏️"):
        # 1、保存当前会话信息
        save_session()

    #     2、创建新的会话
        st.session_state.messages = []
        st.session_state.current_session = datetime.now().strftime("%Y%m%d_%H%M%S")
        save_session()

    # 会话历史
    st.text("会话历史")

    session_list = load_sessions()
    for session in session_list:
        # st.button(session, width="stretch", icon = "📄")
        # st.button("", width="stretch", icon = "X")
        # 按照4:1去划分
        column1, column2 = st.columns([4,1])
        with column1:
            # 三元运算符：如果条件为真，则返回第一个表达式的值
            # 值1 if 表达式 else 值2
            if st.button(session, width="stretch", icon="📄", key=f"session_{session}", type="primary" if session==st.session_state.current_session else "secondary"):
                load_session(session)
                # 这里rerun()会重新运行整个脚本，使得伴侣名称和性格都展示出来

                st.rerun()

        with column2:
            # 删除指定会话
            # 删除指定会话的按钮
            if st.button("", width="stretch", icon="❌", key=f"delete_{session}"):
                try:
                    # 删除文件
                    os.remove(f"resource/sessions/{session}.json")
                    # 如果删除的是当前对话，则需要更新消息列表
                    if session == st.session_state.current_session:
                        st.session_state.messages = []
                        st.session_state.current_session = datetime.now().strftime("%Y%m%d_%H%M%S")
                except Exception as e:
                    st.error(f"删除会话失败！ {session}: {e}")
                # 重新运行脚本
                st.rerun()

    st.subheader("伴侣性格")
    # 这里去找官方文档，都有参数介绍
    nick_name = st.text_input("伴侣名称",placeholder = "请输入昵称",value = st.session_state.nick_name)
    if nick_name:
        st.session_state.nick_name = nick_name
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
    # 流式输出方式
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            full_response += content
            response_message.chat_message("assistant").write(full_response)

    # 保存AI的回复
    st.session_state.messages.append({"role": "assistant", "content": full_response})
    # DEBUG:
    print(f"<----------{full_response}")

    # 保存在JSON中
    save_session()
    st.rerun()