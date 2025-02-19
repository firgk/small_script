# 元素定位隐性等待
# 演示地址：https://bahuyun.com/bdp/form/1327923698319491072

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


# 设置浏览器、启动浏览器
def she():
    q1 = Options()
    q1.add_argument("--no-sandbox")
    q1.add_experimental_option("detach", True)
    a1 = webdriver.Chrome(service=Service(r'chromedriver.exe'), options=q1)
    return a1


a1 = she()
a1.maximize_window()
a1.get('https://bz.zzzmh.cn/index')
# 元素定位隐性等待(多少秒内找到元素就立刻执行，没找到元素就报错)
a1.implicitly_wait(30)

time.sleep(1)
for j in range(1733):
    time.sleep(0.3)
    for i in range(24):
        a1.find_elements(By.CLASS_NAME, 'down-span')[i].click()
    a1.find_element(By.XPATH, '//*[@id="app"]/div/main/div/div/div/div[5]/div/div/div/div/div/div[2]').click()

