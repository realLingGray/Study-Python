from lxml import html

# 获取 html 文件
with open("./resource/xunlian.html", "r", encoding="utf-8") as f:
    html_text = f.read()


# 解析html的文本，将其统一为一个html对象
document = html.fromstring(html_text)

# 解析表头 - XPath用法
# //：表示所有的这类元素，从任意位置匹配
# /：表示从根节点开始索引，要写绝对路径


th_list = document.xpath("//thead/tr/th/text()")
print(th_list)
# 此时是所有的文本，可以使用[]来获取第一个内容
td_list = document.xpath("//tbody/tr/td//text()")
print(td_list)
# 获取第一个tr的文本内容，使用 tr[1] 来获取第一个tr的文本内容
# 注意：不是tr[0]，而是tr[1]
tr_list = document.xpath("//tbody/tr[2]/td/text()")
print(tr_list)
# 获取最后一行数据
tr_last_list = document.xpath("//tbody/tr[last()]/td/text()")
print(tr_last_list)
# 倒数第二个：last() - 1
tr_last_list = document.xpath("//tbody/tr[last()-1]/td/text()")
print(tr_last_list)

# 获取p标签
p_list = document.xpath("//p/text()")
print(p_list)

# 我要匹配有class属性的p标签，用@表示属性
p_list = document.xpath("//p[@class]/text()")
print(p_list)

# 我要匹配有class属性的p标签，用@表示属性，可以用 = 来匹配值
p_list = document.xpath("//p[@id = 'nihao2']/text()")
print(p_list)

# 用 * 来表示通配
tr_last_list = document.xpath("//tbody/*/td/text()")
print(tr_last_list)

# 匹配属性：@src，如果匹配所有属性，用@*
img_list = document.xpath("/html/body/img/@src")
print(img_list)
