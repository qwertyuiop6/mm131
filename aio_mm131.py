from set_mm131_header import set_header,ref_set
from aiomultiprocess import Pool
import aiohttp,asyncio,time,os

async def get(url):
    print('Waiting for', url)
    i=url[24:29]
    j=url[30:-4]
    if os.path.exists(iofolder+i):
        pass
    else:
        async with aiohttp.ClientSession() as session:
            response = await session.get(url,headers=set_header(url))
            pic = await response.read()
        if response.status==404:
            return '404 not found!'

        print('Get res from', url, 'Result:', response.status,'ok!')
        if not os.path.exists(iofolder+i):
            os.makedirs(iofolder+i)
        with open(iofolder+'%s/%s.jpg'% (i,j),'wb') as pp:
            pp.write(pic)
    

async def makeurl(sta,end,limit): 
    urls=['http://img1.mm131.me/pic/'+str(i)+'/'+str(j)+'.jpg' for i in range(sta,end) for j in range(1,limit)]
    return await Pool().map(get,urls)


if __name__ == '__main__':
    # sta,end=map(int,input('输入mm起始编号和结束编号 以空格隔开:').split(' '))
    limit=60
    iofolder='mm131/'
    start = time.time()
    task = asyncio.ensure_future(makeurl(2500,4400,limit)) 
    loop = asyncio.get_event_loop()
    loop.run_until_complete(task)
    end = time.time()
    print('爬取任务已完成,消耗时间:', end - start)