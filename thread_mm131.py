from set_mm131_header import set_header,ref_set
from concurrent import futures
import requests
import os,time

def get(url,i,j):
    response = requests.get(url,headers=set_header(url))
    pic=response.content
    if response.status_code==404:
        return '404 not found!'
    if not os.path.exists(iofolder+i):
        os.makedirs(iofolder+i)
    with open(iofolder+'%s/%s.jpg'% (i,j),'wb') as pp:
        pp.write(pic)
    return 'okay~!'
 
def req(ij):
    i=ij[:4]
    j=ij[4:]
    if not os.path.exists(iofolder+i):    
        url = 'http://img1.mm131.me/pic/'+i+'/'+j+'.jpg'
        print('Waiting for', url)
        result = get(url,i,j)
        print('Get res from', url, 'Result:', result)

if __name__ == '__main__':
    # sta,end=map(int,input('输入mm起始编号和结束编号 以空格隔开:').split(' '))
    limit=65
    iofolder='mm131/'
    start = time.time()
    wokers=100
    with futures.ThreadPoolExecutor(wokers) as e:
        e.map(req,[ str(i)+str(j) for i in range(2500,4400) for j in range(1,limit)])
    end = time.time()
    print('爬取任务已完成,消耗时间:', end - start)