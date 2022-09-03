# homework
本次作业提交两个自行编写的爬虫项目：1点点租网站获取写字楼租金等信息2异步社区获取书单信息


## 1.点点租网站获取写字楼租金等信息（使⽤bs4库提取信息）

### 基本介绍
- 从点点租获取上海市写字楼的名称、所在市区、租金、竣工时间以及经纬度信息并存储于csv文件中

- 经纬度通过transCoordinateSystem.py进行纠偏转化为WGS1984坐标系，便于后续用ArcGIS在官方底图上绘制图件

- 本项目设置爬取150页数据，共1400+条数据

- 结果输出为海写字楼.csv文件和5个存储写字楼空间位置的shpfile文件，默认保存路径为桌面

### 结果展示

   -| 写字楼名称  | 所在市区  | 租金  | 竣工时间  | 经度  | 纬度  | geometry
 ---- | ----- | ------  | ----- | ------  | ----- | ------| ----- 
 0  | 森兰美奂大厦(国企楼盘VR看房)(租售中) | 上海市浦东区  | 3-6.6元/m2/天  | 2019年9月30号  | 31.313477  | 121.591477  | POINT (121.591477 31.313477)   

### 注意事项
- ***transCoordinateSystem.py 用于纠偏统一经纬度，必须和爬虫文档放在同一目录一下***

- 本次爬取前150页数据，可以根据需要进行调整，但注意**不要超过网页最大页数**

- 最后导出的shpfile文件和csv保存路径默认是桌面，可以自行调整

- 为减缓网页压力可以设置每页爬取后的休眠时间，示例设置随机1-5秒


## 异步社区爬取书单：(Selenium获取动态网页数据）

### 基本介绍
- 从异步社区网站爬取书单，包含书名和价格信息，并存储于csv文件中

-本项目Selenium是通过实例化谷歌浏览器而获取数据

- 本项目设置爬取100页数据，共1500+条数据

- 结果输出为书单.csv，默认保存路径为桌面

### 结果展示
  -| 书名  | 价格（元）
 ---- | ----- | ------  
 0  | Rust实战 | 110.33 
1  | Python编程快速上手 让繁琐工作自动化 第2版【购买纸质书免费赠送本书e读版电子书】 | 75.65
 
### 注意事项
- 爬取前需要下载和配置selenium驱动，本项目用Selenium驱动Chrome浏览器，故**需下载谷歌浏览器及相应版本的驱动**
```
chrome浏览器驱动下载网址：https://registry.npmmirror.com/binary.html?path=chromedriver/
```

- **防⽌⽹⻚加载速度慢，设置翻页休眠时间**，确保网页信息可全部加载，可以自行根据网速调整，经过实验一般2-10s

- 本次爬取的是100页书单，可以根据需要进行调整，但注意不要超过网页最大页数

- 最后的csv的保存路径可以自行设置，默认即为桌面



学生是新手，上学期通过上课和自学初步了解python语言的基础知识，为应用于城市地理研究，暑假主要通过网课学习空间数据的爬取、处理与储存，目前主要学习了xpath、Beautifulsoup、Selenium的应用（暑假学习时的部分练习在python_crawer和python_basic仓库中），对于Scrapy、App爬虫、JavaScript逆向爬虫等进阶爬虫方法还在学习中，有关解决滑块登陆、代理IP池避免IP被封等问题也在学习进程中。深知现在水平还很初级，存在很多缺陷以及需改进的地方，例如二级页面的爬取，缺失数据的处理，爬取性能的改善等，学习之路漫长，敬请老师同学批评指正！
