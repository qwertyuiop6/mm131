import time,os
from aio_mm131 import Aio_mm
from thread_mm131 import Thread_mm
from lib.utils import getmmdir,getnew

def start(begin,end):
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
	folder='mm131/'
	finished,newid=getmmdir(folder),getnew()
	start(finished,newid)