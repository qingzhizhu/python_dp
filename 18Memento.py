#!/usr/bin/python
#coding=utf-8
#desc:18.Memento 备忘录设计模式

#region 备忘录类

class Memento(object):
	def __init__(self):
		super().__init__()
		self.dict = {}

	def set_status(self, dict):
		self.dict = {}
		for key in dict:
			if not key.startswith("_"):
				self.dict[key] = dict[key]

	def get_status(self):
		return self.dict



#endregion


#region 管理类

class CareTaker(object):
	def __init__(self):
		self._mementoList = []

	def add(self, mementoObj):
		self._mementoList.append(mementoObj)

	def get(self, idx):
		return self._mementoList[idx]


#endregion

#region

class Originator(object):
	def __init__(self, age, name):
		super().__init__()
		self.setNew(age, name)	

	def setNew(self, age, name):
		self.age = age
		self.name = name

	def restore_to(self, mementoObj):
		self.__dict__.update(mementoObj.get_status())

	def backup_to(self):
		mementoObj = Memento()
		mementoObj.set_status(self.__dict__)
		return mementoObj

#endregion



#region main

if __name__ == "__main__":
	# for arg in sys.argv:  
	# 	print(arg)

	print("Start!")
	
	orig = Originator(10, "map1")
	care = CareTaker()
	care.add(orig.backup_to())


	orig.setNew(15, "fifteen_name")
	
	orig.setNew(18, "map3")
	care.add(orig.backup_to())

	print("当前值：", orig.name, orig.age)
	
	orig.restore_to(care.get(0))
	print("返回到第一阶段值：", orig.name, orig.age)

	
	print("Done!")


#endregion
