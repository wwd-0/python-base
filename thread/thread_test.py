#coding=utf-8
import threading
import time

mutex = threading.Lock()
num  = 0

class MyThread(threading.Thread):
	def __init__(self,flag):
		self.flag = flag
		threading.Thread.__init__(self)

	def run(self):	
		global num
		for i in range(1000000):
			if self.flag:
			#	mutex.acquire()
				num += 1
			#	mutex.release()
			else:
			#	mutex.acquire()
				num -= 1
			#	mutex.release()
		print("-----------done")

if __name__ == "__main__":
	t = MyThread(True)
	t.start()		
	
	t2 = MyThread(False)
	t2.start()		
	time.sleep(5)
	print("---------%d" % num)
