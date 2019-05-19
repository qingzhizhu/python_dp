#!/usr/bin/python
#coding=utf-8
#desc:15.策略模式 Strategy Pattern


import types

#MethodType： 
# 用MethodType将方法绑定到类，并不是将这个方法直接写到类内部，而是在内存中创建一个link指向外部的方法，在创建实例的时候这个link也会被复制。

class StrategyExample:
	def __init__(self, func = None):
		self.name = "Strategy Example 0"
		if func is not None:
			self.execute = types.MethodType(func, self)

	def execute(self):
		print(self.name)

def execute_replacement1(self):
	print(self.name + "from execute 1")


def execute_replacement2(self):
	print(self.name + "from execute 2")

def test():
	strat0 = StrategyExample()
	strat1 = StrategyExample(execute_replacement1)
	strat1.name = "strategy example 1"

	strat2 = StrategyExample(execute_replacement2)
	strat1.name = "strategy example 2"


	strat0.execute()
	strat1.execute()
	strat2.execute()

#region main

if __name__ == "__main__":
	# for arg in sys.argv:  
	# 	print(arg)

	print("Start!\n\n")
	test()

	print("Done!")


#endregion
