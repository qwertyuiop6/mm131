## MM131妹子图片批量下载爬虫py脚本

爬取网站:[MM131](http://mm131.com)

爬了**2000**套妹子图集　将近**10万**张，共**8.5个G**  （图为我的腾讯云cos存储

![](images/mm131_number.png)

![](images/biehuang1.jpeg)

最开始的版本其实是先解析页面再提取url链接逐个请求,
后来发现了图片的url规律：
url变量只有末尾的: id/num

然后发现对req header请求头伪装一下UA用户代理和链接所在文档位置Referer 就可以直接就可以对图片进行请求,这就很舒服~

再配合上多进程+协程的一个库[aiomultiprocess](https://github.com/jreese/aiomultiprocess)进行异步请求,concurrent包的futures线程池进行并发爬取,爬取速度效率大幅提升。

## Usage:
1.安装依赖(Python3):
> pip install -r requirements.txt

2.
运行脚本,爬虫有两个版本<br>
~~windows建议 运行多线程版本: **thread_mm131.py**~~<br>
~~linux/os x 运行 多进程+协程版本: **aio_mm131.py** 或前者皆可~~

- <=2019.3.23=>
-  更新依赖支持python3.7
- <=2018 12.1=><br>
- 自动获取网站最新更新
- 终断下载后再次下载会继续上次的进度
- 自动选择不同系统合适的下载方法

只需
>  python main.py    


来不及解释了，快上车！！


![](images/www.jpg)


### 有问题可以提issue,欢迎老司机们 star,fork ~