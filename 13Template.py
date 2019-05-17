#!/usr/bin/python
#coding=utf-8
#desc:13模板模式 Template Pattern
#旅行社一个三天旅行的例子

from abc import ABCMeta, abstractmethod

#region Abstract 定义不同日子使用的交通方式和参观的地点等细节 Trip

class Trip(metaclass=ABCMeta):
	'''
	itinerary()模板方法创建完成的行程，即算法，在例子中表示旅行。
	'''

	@abstractmethod
	def setTransport(self): pass
	
	@abstractmethod
	def day1(self): pass

	@abstractmethod
	def day2(self): pass

	@abstractmethod
	def day3(self): pass

	@abstractmethod
	def returnHome(self): pass

	def itinerary(self):
		self.setTransport()
		self.day1()
		self.day2()
		self.day3()
		self.returnHome()


#endregion

#region ConcreteClass 威尼斯、马尔代夫两条旅行路线

class VeniceTrip(Trip):
	def setTransport(self):
		print("乘船")

	def day1(self):
		print("day1 参观圣马可教堂")

	def day2(self):
		print("day2 欣赏 Doge 宫殿")
	
	def day3(self):
		print("day3 里亚多桥吃美食")

	def returnHome(self):
		print("为家人朋友买纪念品回家")

class MaldviesTrip(Trip):
	def setTransport(self):
		print("在任何岛屿徒步")

	def day1(self):
		print("day1 参观香蕉礁的海洋生物")

	def day2(self):
		print("day2 去浮潜和水上娱乐")

	def day3(self):
		print("day3 在沙特上晒太阳放松")
	
	def returnHome(self):
		print("离开海滩吧")

#endregion


#region Client 选择具体路线

class TraveAgency:
	def arrange_trip(self):
		# choice = input("what kind of place you'd like to go historical or to a beanch ? 1 or 2")
		choice = 1
		if choice == 1:
			self.trip = VeniceTrip()
			self.trip.itinerary()
		elif choice == 2:
			self.trip = MaldviesTrip()
			self.trip.itinerary()



#endregion


#region main

if __name__ == "__main__":
	# for arg in sys.argv:  
	# 	print(arg)

	print("Start!\n\n")
	
	TraveAgency().arrange_trip()

	print("Done!")


#endregion
