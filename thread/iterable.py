#coding=utf-8
from collections import Iterable
import time

class ClassMate(object):
	def __init__(self):
		self.names = list()
		self.current_num = 0
	
	def add(self,name):
		self.names.append(name)
	
	def __iter__(self):
		return self

	def __next__(self):
		if self.current_num < len(self.names):
			ret = self.names[self.current_num]
			self.current_num += 1
			return ret
		else:
			raise StopIteration


if __name__ == "__main__":
	classmate  = ClassMate()
	classmate.add("老王")
	classmate.add("老张")
	classmate.add("老李")

	for name in classmate:
		print(name)
		time.sleep(1)
	

