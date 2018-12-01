## MM131妹子图片批量下载爬虫py脚本

爬取网站:[MM131](http://mm131.com)

爬了**2000**套妹子图集　将近**10万**张，共**8.5个G**  （图为我的腾讯云cos存储

![](images/mm131_number.png)

![](images/biehuang1.jpeg)

最开始爬取的时候是对页面解析得到链接再进行请求，
后来发现了站点的url规律：
id/num

然后发现对req header伪装一下UA和Referer 就可以直接就可以对图片进行请求,
再配合上多进程,协程 和线程池进行并发爬取,效率大幅提升!

## Usage:
1.安装依赖(Python3):
> pip install -r requirements.txt

~~运行脚本,爬虫有两个版本~~<br>
~~windows建议 运行多线程版本: **thread_mm131.py**~~<br>
~~linux/os x 运行 多进程+协程版本: **aio_mm131.py** 或前者皆可~~

- 2018 12.1号更新 <br>
- 自动获取网站最新更新
- 终断下载后再次下载会继续上次的进度
- 自动选择不同系统合适的下载方法
> 直接 python main.py  将自动选择合适版本运行  

来不及解释了，快上车！!


![](images/www.jpg)


### 有问题可以提issue,欢迎老司机们 star,fork ~