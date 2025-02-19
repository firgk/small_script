
# 2获取链接 过滤或者找元素
# 3解析数据 并且下载





import requests
import re




# 附加 下载函数
# Function to download images
# i 是 序数 url 下载链接 file_name 文件名
def download_image(i, url, file_name):
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print(f"✅ [{i + 1}]: {file_name}")
    else:
        print(f"🥺 [{i + 1}]: Failed to download {url}")

# Path to the README file
url = 'https://bz.zzzmh.cn/index' 

# 1请求壁纸页面
# 失败 无法请求 vue 技术

 
# Function to scrape image URLs from README file
def scrape_image_urls(url):
    response=requests.get(url)
    response.encoding = "utf-8" # 手动指定字符编码为utf-8

