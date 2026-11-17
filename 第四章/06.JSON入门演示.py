import json
def write_json():
    # 写入json
    user = {
        "name": "张三",
        "age": 18,
        "sex": "男",
        "is_student": True,
        "hobbies": ["coding", "gaming", "reading"]
    }
    with open("resource/user.json", "w", encoding="utf-8") as f:
        # dump有一些参数可以选择
        # ensure_ascii= False：确保中文不被转义，默认为True True是确保为ASCII
        # 编码，改为False确保为中文，非ASCII码保持原样子
        # indent = 4：缩进4个空格，格式化
        json.dump(user,f,ensure_ascii= False,indent=4)
def read_json():
#     读取JSON文件
    with open("resource/user.json", "r", encoding="utf-8") as f:
        user = json.load(f)
        print(user)
        print(type(user))

if __name__ == '__main__':
    read_json()