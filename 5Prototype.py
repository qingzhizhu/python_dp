#!/usr/bin/python
#coding=utf-8
#desc:原型模式 Prototype Pattern

from Core import Prototype


class Test(Prototype):
	_type = None
	_value = None
	_list = None
	_dict = None

	def __init__(self):
		print("Test init. clone 不执行")
		self._type = "test"
		self._value = 10
		self._list = ["hi", True, 20, ["python", "go", "erlang"]]
		self._dict = {"one":1, "two":2}

	def sayhi(self):
		print("sayhi", type(self).__name__, id(self))
		print("_type:", self._type, id(self._type))
		print("_value:", self._value, id(self._value))
		print("_list:", self._list, id(self._list))
		print("_dict", self._dict, id(self._dict))
		print(30*'-')

#region main

if __name__ == "__main__":
	# for arg in sys.argv:  
	# 	print(arg)

	print("Start!\n\n")
	t = Test()
	print("原值t：")
	t.sayhi()

	t_lightcopy = t.clone()
	t_lightcopy._list[3].append("matlab")
	print("浅拷贝：")
	t_lightcopy.sayhi()
	print("由于浅拷贝操作_list，导致原值t._list 发生变化:")
	t.sayhi()

	t_deepcopy = t.deepclone()
	t_deepcopy._value = 99
	t_deepcopy._list[3].append("perl")
	print("深拷贝：")
	t_deepcopy.sayhi()



	print("Done!")


#endregion
