#!/usr/bin/python
#coding=utf-8
#desc:9.装饰模式 Decorator Pattern
#TP：咖啡，可以加入糖，香草，牛奶不同口味的装饰模式demo：

from abc import ABCMeta, abstractmethod
import six


#region Component, ConcreteCompoent

@six.add_metaclass(ABCMeta)
class Abstract_Coffee(object):
	
	def get_cost(self): pass
	def get_ingredients(self): pass
	
	def get_tax(self):
		return 0.1*self.get_cost()
	
	def get_receipt(self):
		print("成分："+self.get_ingredients() + "; 价格："+ str(self.get_cost()) +"; tax:"+ str(self.get_tax()) )

class Concrete_Coffee(Abstract_Coffee):
	def get_cost(self):
		return 1.00

	def get_ingredients(self):
		return "coffee"

#endregion


#region Decorator, ConcreteDecorator 具体装饰者

@six.add_metaclass(ABCMeta)
class Abstract_Coffee_Decorator(Abstract_Coffee):
	def __init__(self, decorated_coffee):
		self.decorated_coffee = decorated_coffee
	
	def get_cost(self):
		return self.decorated_coffee.get_cost()

	def get_ingredients(self):
		return self.get_ingredients()

class Sugar(Abstract_Coffee_Decorator):
	def __init__(self, decorated_coffee):
		Abstract_Coffee_Decorator.__init__(self,decorated_coffee)

	def get_cost(self):
		return self.decorated_coffee.get_cost()

	def get_ingredients(self):
		return self.decorated_coffee.get_ingredients() + ", sugger"


class Milk(Abstract_Coffee_Decorator):
	def __init(self, decorated_coffee):
		Abstract_Coffee_Decorator.__init__(self, decorated_coffee)

	def get_cost(self):
		return self.decorated_coffee.get_cost() + 0.25

	def get_ingredients(self):
		return self.decorated_coffee.get_ingredients() + ", milk"

class Vanilla(Abstract_Coffee_Decorator):
	def __init__(self, decorated_coffee):
		Abstract_Coffee_Decorator.__init__(self,decorated_coffee)

	def get_cost(self):
		return self.decorated_coffee.get_cost() + 0.75

	def get_ingredients(self):
		return self.decorated_coffee.get_ingredients() + ", Vanilla"


#endregion


if __name__ == "__main__":
	# for arg in sys.argv:  
	# 	print(arg)

	print("Start!\n\n")

	print("来杯加糖咖啡：")	
	myCoffee = Concrete_Coffee()
	myCoffee = Sugar(myCoffee)
	myCoffee.get_receipt()

	print("在来杯牛奶香草加糖咖啡")
	coffee2 = Concrete_Coffee()
	print("coffee obj:", coffee2)
	coffee2 = Milk(coffee2)
	coffee2 = Vanilla(coffee2)
	print("coffee obj:", coffee2, "类型已经是装饰器的子类了")
	coffee2 = Sugar(coffee2)
	coffee2.get_receipt()
	
	print("Done!")