from selenium import webdriver
from lxml import etree
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import pandas as pd

# 实例化⼀个chrome浏览器对象
s = Service(r"D:\chromedriver_win32\chromedriver.exe")
chrome = webdriver.Chrome(service=s)

# 获取书单的中的书名和价格
book_name = []
book_price = []


def extract_data(page_source):
    tree = etree.HTML(page_source)
    book_list = tree.xpath('//*[@id="bookItem"]/a')
    for book in book_list:
        name = book.xpath("./div[2]/text()")[0]
        price = book.xpath("./div[3]/div[1]/text()")[0]
        if "￥" in price:
            price1 = price.split("￥")[1]
        else:
            price1 = "None"

        book_name.append(name)
        book_price.append(price1)
        print(name, price1)

# 定位下⼀⻚标签并点击（实现翻页）


def to_next_page():
    next_btn = chrome.find_element(
        By.XPATH, '//*[@id="entry"]/div[2]/div[2]/div[2]/div/button[2]')
    next_btn.click()  # 左键点击操作

# 获取100页书单信息


def run():
    url = 'https://www.epubit.com/books'
# 请求网页，打开url地址（此处的get不是requests中的get请求）
    chrome.get(url)
    print("第1页书单")
    extract_data(chrome.page_source)
    for i in range(2, 3):
        print(f"第{i}页书单")
        time.sleep(1)  # 防⽌⽹⻚加载速度慢，等1秒再翻页
        to_next_page()
        time.sleep(10)  # 确保页面的信息被加载出来
        extract_data(chrome.page_source)

    chrome.close()


run()

# 书单信息存储到csv中
booklist = {"书名": book_name, "价格(元）": book_price}
df = pd.DataFrame(booklist)
df.to_csv(
    r"C:\Users\Lenovo\Desktop\书单.csv", encoding='utf-8')