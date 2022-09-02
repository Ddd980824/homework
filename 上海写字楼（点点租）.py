import pandas as pd
import geopandas as gpd
import requests
from bs4 import BeautifulSoup
import transCoordinateSystem as tr
from tqdm import tqdm  # 显示处理进度
import time
import random


def building_message(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}
    res = requests.get(url, headers=headers)
    html = res.text
    soup = BeautifulSoup(html, "lxml")
    # 获取写字楼的名称
    name = soup.find_all(name="h1", attrs={"class": "fl"})[0].text
    # 获取所在市区
    block = "上海市" + \
        soup.find_all(name="a", attrs={"target": "_blank"})[
            1].text.split("写")[0] + "区"
    # 获取租金
    price = soup.find_all(name="span", attrs={"class": "price-num"})[0].text.replace("~","-")
    unit = soup.find_all(name="div", attrs={
                         "class": "top-price fr"})[0].text.split("元")[1]
    rental = price + "元" + unit
    # 获取竣工时间
    for i in soup.find_all(name="span", attrs={"class": "f-con"}):
        if "年" in i.text and len(i.text)<12 and "/" not in (i.text):
            time = i.text
        try:
            a = time
        except:
            time = ""
    # 获取经纬度并纠偏（转为wgs1984）
    longitude = float(soup.find_all(
        name="span", attrs={"id": "longitude"})[0].text)
    latitude = float(soup.find_all(
        name="span", attrs={"id": "latitude"})[0].text)
    location = tr.bd09_to_wgs84(latitude, longitude)
    lon_wgs1984 = round(location[1], 6)
    lat_wgs1984 = round(location[0], 6)
    return {"写字楼名称": name,
            "所在市区": block,
            "租金": rental,
            "竣工时间": time,
            "纬度": lat_wgs1984,
            "经度": lon_wgs1984}


data = []
for i in tqdm(range(1, 151)): #爬取150页数据
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}
    url = "https://sh.diandianzu.com/listing/p"+str(i)+"/"
    a = requests.get(url, headers=headers)
    html = a.text
    soup = BeautifulSoup(html, "lxml")
    for page in soup.find_all(name="div", attrs={"class": "list-item-link"}):
        building_url = "https://sh.diandianzu.com" + page.find_all(name="a", attrs={"target": "_blank"})[0]["href"]
        data.append(building_message(building_url))
    print(f"完成第{i}页打印")
    # time.sleep(random.randint(1,5))
df = pd.DataFrame()
df = df.append(data, ignore_index=True)
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.经度, df.纬度))
gdf.crs = "EPSG:4326"
gdf.plot()
gdf.to_file(
    r"D:\科研数据处理\立方数据学社\python城市数据爬取\python城市数据爬取练习\暑假作业\上海写字楼.shp", encoding="gb18030")
gdf.to_csv(
     r"D:\科研数据处理\立方数据学社\python城市数据爬取\python城市数据爬取练习\暑假作业\上海写字楼.csv", encoding='utf-8')
