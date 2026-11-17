import streamlit as st

st.set_page_config(
    page_title = "AI智能伴侣",
    page_icon = "🍅",
#     布局
    layout = "wide",
#     控制的是侧边栏的状态
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": "https://www.extremelycoolapp.com/help",
        "Report a bug": "https://www.extremelycoolapp.com/bug",
        "About": "# This is a header. This is an *extremely* cool app!"
    }

)
# 大标题
st.title("AI智能伴侣")

# Logo
st.logo("resource/favicon.ico")

# 聊天消息输入框
prompt = st.chat_input("请输入你的问题")
if prompt:  #字符串会自动转化为布尔值，如果字符串非空则返回True，否则为False
    # st.write(f"用户：{prompt}")
    st.chat_message("user").write(prompt)
    print("------------------>" + prompt)
    st.chat_message("assistant").write("这是AI的回复")
