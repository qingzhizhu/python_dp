#!/usr/bin/python
#coding=utf-8
#desc:17.Iterator pattern 迭代器

from inspect import isgeneratorfunction
import types
from collections import Iterable

#region 繁琐写法

class Iterator(object):
	def __init__(self, iterator_list):
		super().__init__()
		self.list = iterator_list
		self.current_index = 0
		self.max_index = 0

	def __iter__(self):
		self.current_index = 0
		self.max_index = len(self.list) - 1
		return self

	def __next__(self):
		if self.current_index <= self.max_index:
			one = self.list[self.current_index]
			self.current_index += 1
			return one
		else:
			raise StopIteration

#endregion


#region yield 精简

def fab(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield b
		a, b = b, a+b
		n += 1


#endregion


#region main

if __name__ == "__main__":
	# for arg in sys.argv:  
	# 	print(arg)

	print("Start!")
	
	iter = Iterator([5, 8, 1, 'q', 'h'])

	for one in iter:
		print(one)
	
	print(30*"-")

	print("斐波那契数列")
	arr = fab(7)
	for n in arr:
		print(n)

	print("fab 是生成器吗？", isgeneratorfunction(fab))

	print("fab 是实例吗？", isinstance(fab, types.GeneratorType))
	print("fab(5) 是实例吗？", isinstance(fab(5), types.GeneratorType))

	print("fab 可迭代吗？", isinstance(fab, Iterable) )
	print("fab(5) 可迭代吗？", isinstance(fab(5), Iterable) )

	print("Done!")


#endregion
