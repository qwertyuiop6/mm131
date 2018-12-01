from aio_mm131 import Aio_mm
from thread_mm131 import Thread_mm
import os,time,requests
from lxml import etree

def getmmdir():
	if os.path.exists(mm_folder) and len(os.listdir(mm_folder))>0:
		return int(max(os.listdir(mm_folder)))
	else:
		return default_start

def getnew():
	try:
		url='http://www.mm131.com/xinggan/'
		content=etree.HTML(requests.get(url).text)
		href=content.xpath('//dl[@class="list-left public-box"]//dd[1]/a/@href')[0]
		newid=href[-9:-5]
		return int(newid)
	except Exception as e:
		return default_end

def main_start(begin,end):
	start_time=time.time()
	if os.name=='nt':
		app=Thread_mm()
		app.go_start(begin,end)
	else:
		app=Aio_mm()
		app.go_start(begin,end)
	end_time=time.time()
	print('爬取任务已完成,消耗时间:', end_time - start_time)


if __name__ == '__main__':
	# config={
	# 	'mm_folder':'mm131/',
	# 	'each_limit':60
	# }
	mm_folder='mm131/'

	default_start,default_end=2400,4500

	finished,newid=getmmdir(),getnew()
	
	main_start(finished,newid)