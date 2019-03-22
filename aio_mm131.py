from lib.utils import set_header
from aiomultiprocess import Pool
import aiohttp,asyncio,time,os

class Aio_mm(object):

    def __init__(self):
        self.mm_folder='mm131/'
        self.each_limit=60

    async def async_get(self,url):
        i=url[24:29]
        j=url[30:-4]

        if not os.path.exists(self.mm_folder+i):
            os.makedirs(self.mm_folder+i)
     
        async with aiohttp.ClientSession() as session:
            print('Waiting for', url)
            response = await session.get(url,headers=set_header(url))
            pic = await response.read()
        if response.status==404:
            return '404 not found!'
        print('Get res from', url, 'Result:', response.status,'ok!')
        
        with open(self.mm_folder+'%s/%s.jpg'% (i,j),'wb') as pp:
            pp.write(pic)
        

    async def makeurl(self,sta,end,limit): 
        urls=['http://img1.mm131.me/pic/'+str(i)+'/'+str(j)+'.jpg' for i in range(sta,end+1) for j in range(1,limit)]
        return await Pool().map(self.async_get,urls)

    def go_start(self,begin,end):
        task = asyncio.ensure_future(self.makeurl(begin,end,self.each_limit)) 
        loop = asyncio.get_event_loop()
        loop.run_until_complete(task)

if __name__ == '__main__':
    sta,end=map(int,input('输入mm起始编号和结束编号 以空格隔开:').split(' '))
    app=Aio_mm()
    start_time = time.time()
    app.go_start(sta,end)
    end_time = time.time()
    print('爬取任务已完成,消耗时间:', end_time - start_time)