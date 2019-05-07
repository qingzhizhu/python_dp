#!/usr/bin/python
#coding=utf-8
#desc:建造者模式又名生成器模式 Builder Pattern
#from tutorialspoint 造车示例

#region Car Parts 车零件
class Wheel:
	size = None
class Engine:
	horsepower = None
class Body:
	shape = None
#endregion

#region The whole product 整车
class Car:
	def __init__(self):
		self.__wheels = list()
		self.__engine = None
		self.__body = None
	def setBody(self, body):
		self.__body = body
	def setEngine(self, engine):
		self.__engine = engine
	def attachWheel(self, wheel):
		self.__wheels.append(wheel)

	def specification(self):
		print("body:", self.__body.shape)
		print("engine horsepower:", self.__engine.horsepower)
		print("tire size:", self.__wheels[0].size)
#endregion


#region Builder 构造者
class Builder:
	def getWheel(self): pass
	def getEngine(self): pass
	def getBody(self): pass

class JeepBuilder(Builder):
	'''
	jeep车制造厂
	'''
	def getWheel(self):
		wheel = Wheel()
		wheel.size = 22
		return wheel

	def getEngine(self):
		engine = Engine()
		engine.horsepower = 400
		return engine

	def getBody(self):
		body = Body()
		body.shape = "SUV"
		return body
#endregion

#region Director 指挥者、导演 就如装机师傅
class Director:
	'''
	指挥者、导演 就如装机师傅
	'''

	__builder = None
	
	def setBuilder(self, builder):
		self.__builder = builder

	def getCar(self):
		car = Car()

		#first goes the body
		body = self.__builder.getBody()
		car.setBody(body)

		#then engine
		engine = self.__builder.getEngine()
		car.setEngine(engine)

		#and four wheels 
		i = 0
		while i < 4:
			car.attachWheel(self.__builder.getWheel())
			i += 1
		return car




#endregion

#region main

if __name__ == "__main__":
	# for arg in sys.argv:  
	# 	print(arg)

	print("Start!\n\n")
	
	jeepBuilder = JeepBuilder()
	director = Director()
	director.setBuilder(jeepBuilder)
	car = director.getCar()
	print(type(director).__doc__, type(jeepBuilder).__doc__)
	car.specification()

	
	print("Done!")


#endregion
