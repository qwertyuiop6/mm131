from set_mm131_header import set_header,ref_set
from concurrent import futures
import requests,os,time

class Thread_mm(object):
    
    def __init__(self):
        self.mm_folder='mm131/'
        self.each_limit=60

    def get(self,url,i,j):
        response = requests.get(url,headers=set_header(url))
        pic=response.content
        if response.status_code==404:
            return '404 not found!'
        if not os.path.exists(self.mm_folder+i):
            os.makedirs(self.mm_folder+i)
        with open(self.mm_folder+'%s/%s.jpg'% (i,j),'wb') as pp:
            pp.write(pic)
        return 'okay~!'
     
    def req(self,ij):
        i=ij[:4]
        j=ij[4:]    
        url = 'http://img1.mm131.me/pic/'+i+'/'+j+'.jpg'
        print('Waiting for', url)
        result = self.get(url,i,j)
        print('Get res from', url, 'Result:', result)

    def go_start(self,begin,end,wokers=100,**kw):
        with futures.ThreadPoolExecutor(wokers) as e:
            e.map(self.req,[ str(i)+str(j) for i in range(begin,end) for j in range(1,self.each_limit)])

if __name__ == '__main__':
    # sta,end=map(int,input('输入mm起始编号和结束编号 以空格隔开:').split(' '))
    app=Thread_mm()

    start_time = time.time()
    app.go_start(2500,4400)
    end_time = time.time()
    print('爬取任务已完成,消耗时间:', end_time - start_time)