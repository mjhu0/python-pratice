import re

# 读取百度主页HTML代码
with open('baidu.html', 'r', encoding='utf-8') as file:
    content = file.read()

# 使用正则表达式匹配URL
urls = re.findall(r'https?://[^\s"\']+', content)

# 输出所有匹配的URL
for url in urls:
    print(url)

######  542313460109 胡华吉 ###########