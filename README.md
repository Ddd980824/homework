# homework
本次作业提交两个自行编写的爬虫项目：1点点租网站获取写字楼租金等信息2异步社区获取书单信息


## 1.点点租网站获取写字楼租金等信息（使⽤bs4库提取信息）

a.transCoordinateSystem.py 用于纠偏统一经纬度，必须和爬虫文档放在同一目录一下

b.本次爬取前150页数据，可以根据需要进行调整，但注意不要超过网页最大页数

c.最后导出的shpfile文件和csv保存路径默认是桌面，可以自行调整

d.为减缓网页压力可以设置每页爬取后的休眠时间，示例设置随机1-5秒

e.最终创建的shpfile包含五个文件，上海写字楼.csv为数据储存文件



2.异步社区爬取书单：(Selenium获取动态网页数据）

a.防⽌⽹⻚加载速度慢，设置休眠时间，可以自行根据网速调整，经过实验一般2-10s

b.最后的csv的保存路径可以自行设置，默认即为桌面

c.本次爬取的是100页书单，可以根据需要进行调整，但注意不要超过网页最大页数

d.书单.csv为最终保存数据的文档

学生是新手，上学期通过上课和自学初步了解python语言的基础知识，为应用于城市地理研究，暑假主要通过网课学习空间数据的爬取、处理与储存，目前主要学习了xpath、Beautifulsoup、Selenium的应用（暑假学习时的部分练习在python_crawer和python_basic仓库中），对于Scrapy、App爬虫、JavaScript逆向爬虫等进阶爬虫方法还在学习中，有关解决滑块登陆、代理IP池避免IP被封等问题也在学习进程中。深知现在水平还很初级，学习之路漫长，敬请老师同学批评指正！
