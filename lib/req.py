import requests,os
from .utils import set_header

class Request(object):

    def __init__(self):
        self.folder='mm131/'
        
    def save(self,pic,i,j):
        if not os.path.exists(self.folder+i):
            os.makedirs(self.folder+i)
        with open(self.folder+'%s/%s.jpg'% (i,j),'wb') as pp:
            pp.write(pic)
        return 'saved!'

    def get(self,url,i,j):
        response = requests.get(url,headers=set_header(url))
        pic=response.content
        if response.status_code==404:
            return '404 not found!'
        elif response.status_code==200:
            return self.save(pic,i,j)

    def requrl(self,ij):
        i=ij[:4]
        j=ij[4:]
        url = 'http://img1.mm131.me/pic/'+i+'/'+j+'.jpg'
        print('正在请求-->', url)
        result = self.get(url,i,j)
        print('获取到结果:-->', url, '-->', result)

