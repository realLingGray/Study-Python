import streamlit as st

#大标题
st.title("streamlit入门演示")
st.header("Streamlit一级标题")
st.subheader("Streamlit二级标题")

#段落文字
st.write("测试字符串")
st.write("段落二：中華人民共和國是位於東亞的社會主義國家，也是現今世界少數由共產黨建立並持續單獨執政的國家。國土面積約960萬平方公里，位居世界各國第三位，其以漢族傳統領域為核心，涵蓋鄰太平洋的亞洲大陸東側大部區域，並與14個國家以陸地邊界接壤。")
st.write("段落三：美国为首的西方列强开始了……")

# 图片
st.image("./resource/picture_test.png", width=300)

# 音频
st.audio("resource/08 放課後ティータイム - U&I.flac")

# 视频
st.video("resource/video_test.mkv")

# Logo
st.logo("resource/favicon.ico")

# 表格
# 用字典去构造，key = 行的名字，value = 内容
# 字典的每个元素都是一行
student_data = {
    "姓名": ["小明","小王","小刚","小李","郭聪","刘丽"],
    "学号":["2601","2602","2603","2604","2605","2606"],
    "总分":[577,608,698,655,699,654]
}
st.table(student_data)

# 输入框
name = st.text_input("请输入姓名", type = "password")
st.write(f"您输入的姓名为：{name}")

# 单选按钮
# index：默认选项
gender = st.radio("请输入您的性别",["男", "女", "未知"], index = 1)
st.write(f"您的性别为：{gender}")