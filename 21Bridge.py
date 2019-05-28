#!/usr/bin/python
#coding=utf-8
#desc:21.桥接模式 Bridge Pattern
#使用相同的抽象类方法但是不同的桥接实现类，来画出不同颜色的圆

from abc import ABCMeta, abstractmethod

#region Implementor 实现类接口

class DrawAPI(metaclass=ABCMeta):
	@abstractmethod
	def drawCircle(self, radius, x, y): pass

#endregion

#region ConcreteImplementor 具体实现类

class RedCircle(DrawAPI):
	def drawCircle(self, radius, x, y):
		print("画红色圆形：半径:",radius, "位置:",x,":",y)

class GreenRectCircle(DrawAPI):
	def drawCircle(self, radius, x, y):
		print("画绿色圆角圆形")

#endregion

#region 抽象类
class Shape(metaclass=ABCMeta):
	def __init__(self, drawAPI):
		# print("api:", drawAPI)
		self._drawAPI = drawAPI 

	@abstractmethod
	def draw(self): pass
#endregion


#region RefinedAbstraction 扩充抽象类

class Circle(Shape):
	def __init__(self, x, y, radius, drawAPI):
		super().__init__(drawAPI)
		self._x = x
		self._y = y
		self._radius = radius

	def draw(self):
		self._drawAPI.drawCircle(self._radius, self._x, self._y)

#endregion


#region main

if __name__ == "__main__":
	# for arg in sys.argv:  
	# 	print(arg)

	print("Start!")
	
	redCircle = Circle(10, 10, 5, RedCircle())
	redCircle.draw()

	greenCircle = Circle(20, 20, 3, GreenRectCircle())
	greenCircle.draw()
	
	print("Done!")


#endregion
