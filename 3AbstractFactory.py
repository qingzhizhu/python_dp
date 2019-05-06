#!/usr/bin/python
#coding=utf-8
#desc:3. 抽象工厂示例 Abstract Factory Patterns

from abc import ABCMeta, abstractmethod

#region 产品群 类
class VegPizza(metaclass=ABCMeta):
	'''
	抽象产品类1 素食pizza，
	相当于uml的AbstractProduct
	'''
	
	@abstractmethod
	def prepare(self): pass
	
class NonVegPizza(metaclass=ABCMeta):
	'''
	抽象产品类2 非素食pizza，它在素食披萨上面再加工
	相当于uml的AnotherAbstractProduct
	'''

	@abstractmethod
	def serve(self, VegPizza): pass

class DeluxVegPizza(VegPizza):
	'''
	豪华蔬菜pizza ，相当于uml的ConcreteProduct1
	'''

	def prepare(self):
		print("Prepare", type(self).__name__, type(self).__doc__)

class ChickenPizza(NonVegPizza):
	'''
	鸡肉pizza，相当于uml的AnotherConcreteProduct
	'''

	def serve(self, VegPizza):
		print(type(self).__name__, "is served with Chicken on ", type(VegPizza).__name__, type(self).__doc__)

class MexicanVegPizza(VegPizza):
	'''
	墨西哥蔬菜pizza ，相当于uml的ConcreteProduct2
	'''

	def prepare(self):
		print("Prepare", type(self).__name__, type(self).__doc__)
		
class HamPizza(NonVegPizza):
	'''
	火腿pizza，相当于uml的AnotherConcreteProduct
	'''

	def serve(self, VegPizza):
		print(type(self).__name__, "is served with Ham on ", type(VegPizza).__name__, type(self).__doc__)

#endregion


#region 工厂类
class AbstractPizzaFactory(metaclass=ABCMeta):
	@abstractmethod
	def createVegPizza(self): pass
	@abstractmethod
	def createNonVegPizza(self): pass

class IndianPizzaFactory(AbstractPizzaFactory):
	'''
	印式口味pizza工厂（加工组）
	'''
	def createVegPizza(self):
		return DeluxVegPizza()
	def createNonVegPizza(self):
		return ChickenPizza()

class USPizzaFactory(AbstractPizzaFactory):
	'''
	美式口味pizza工厂（加工组）
	'''
	def createVegPizza(self):
		return MexicanVegPizza()
	def createNonVegPizza(self):
		return HamPizza()

#endregion

#region Client端

class PizzaStore:
	'''
	pizza 店可以生产，美式的蔬菜或美式鸡肉pizza；印式的蔬菜或印式火腿pizza
	'''
	def __init__(self):
		print(type(self).__name__, type(self).__doc__)

	def makePizzas(self):
		for factory in [IndianPizzaFactory(), USPizzaFactory()]:
			self.factory = factory
			print(type(self.factory).__name__, type(self.factory).__doc__)
			self.nonVegPizza = self.factory.createNonVegPizza()
			self.vegPizza = self.factory.createVegPizza()
			self.vegPizza.prepare()
			self.nonVegPizza.serve(self.vegPizza)
			print(30*'-')

#endregion

if __name__ == "__main__":
	# for arg in sys.argv:  
	# 	print(arg)

	print("Start!\n\n")
	pizza = PizzaStore()
	pizza.makePizzas()
	
	
	print("Done!")