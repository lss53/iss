import os
import json
import time
import requests

# 获取当前工作目录
current_dir = os.getcwd()
# 获取当前工作目录的父目录
parent_dir = os.path.dirname(current_dir)
name_json = parent_dir + '/data/neodb/movie.json'
access_token = 'JSX0HX1ocdDB9dmd3lZJASw6XEj8US'
directory = parent_dir + '/static/assets/images/movie/cover'
movie_details = parent_dir + '/data/neodb/movie_details.json'

# 第1步，下载 movie.json
print('第1步，下载 movie.json')

# 设置请求 URL
url = 'https://neodb.social/api/me/shelf/complete?category=movie&page=1'
# 设置请求标头
headers = {
    'accept': 'application/json',
    'Authorization': 'Bearer ' + access_token
}

# 创建一个 GET 请求会话
response = requests.get(url, headers=headers)

# 检查响应状态代码
if response.status_code == 200:
    # 获取 JSON 响应数据
    data = response.json()

    # 将 JSON 数据写入文件
    with open(name_json, 'w') as f:
        json.dump(data, f)
        print(data)

    print(name_json + ' 下载完成。')
else:
    # 处理请求错误
    print(f'错误: {response.status_code} {response.reason}')


# 第2步，下载 cover image
print('第2步，下载 cover image')

# 从 movies.json 文件中加载 JSON 数据
with open(name_json, encoding='utf-8') as f:
    json_data = json.load(f)['data']

image_urls = []
for item in json_data:
    image_urls.append(item['item']['cover_image_url'])
    # print(image_urls)

# 如果不存在，创建用于存储图像的目录
os.makedirs(directory, exist_ok=True)

# 遍历图像 URL 并下载每张图像
for url in image_urls:
    # 获取图像文件名
    filename = os.path.basename(url)
    # 拼接图像文件路径
    filepath = os.path.join(directory, filename)

    # 检查文件是否存在
    if os.path.isfile(filepath):
        print(f"跳过 {filename} - 文件已存在")
    else:
        # 下载图像
        response = requests.get(url)
        with open(filepath, 'wb') as f:
            f.write(response.content)
        print(f"已下载 {filename}")

# 第3步，生成 movie_details.json
print('第3步，生成 movie_details.json')

# 以 UTF-8 编码打开 JSON 文件进行读取。
with open(name_json, encoding='utf-8') as f:
    # 加载 JSON 数据并提取其中的 data 字段
    data = json.load(f)['data']
    
# 创建一个空列表来存储 API URL
api_urls = []

# 遍历 data 字段中的每个项目
for item in data:
    # 将每个项目的 api_url 字段添加到 api_urls 列表中
    api_urls.append(item['item']['api_url'])

# 为每个 API URL 添加网站域名
api_urls = ['https://neodb.social' + url for url in api_urls]

# 创建一个空列表来存储电影详情
details = []

# 遍历 api_urls 列表中的每个 URL
for url in api_urls:
    # 发送 GET 请求以获取电影详情
    response = requests.get(url)
    #将电影详情添加到 details 列表
    details.append(response.json())
    
# 以 UTF-8 编码打开 movie_details.json 文件进行写入
with open(movie_details, 'w', encoding='utf-8') as f:
    # 将电影详情转储到 JSON 文件中，并确保不转义非 ASCII 字符（例如中文）
    json.dump(details, f, ensure_ascii=False)
print(movie_details + ' 已完成。')

# 暂停脚本执行 10 秒
time.sleep(10)




