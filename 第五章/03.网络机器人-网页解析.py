import requests
from lxml import html


# 定义url
target_url = "https://www.tiobe.com/tiobe-index/"


# 发送请求 获取数据
response = requests.get(target_url)


# 获取数据
doc = html.fromstring(response.text)

# 解析表头
data = doc.xpath("//table[@id = 'top20']/thead/tr/th/text()")
print(data)
# 解析表格数据
tr_list = doc.xpath("//table[@id = 'top20']/tbody/tr")
for data in tr_list:
    dataa = data.xpath("./td/text()")
    print(dataa)

# 另一种自动获取：在浏览器打开F12，找到表格的tr标签，右键选择Copy -> Copy XPath
# //table[@id = 'top20']/tbody/tr[1]/td[1]/text()
# //table[@id = 'top20']/tbody/tr[1]/td[2]/text()
# //table[@id = 'top20']/tbody/tr[1]/td[3]/text()
