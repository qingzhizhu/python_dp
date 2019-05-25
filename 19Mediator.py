#!/usr/bin/python
#coding=utf-8
#desc:19中介者模式 Mediator Pattern

#region colleague 合作者

class User(object):
	def __init__(self, name):
		self._name = name

	def __str__(self):
		return self._name

	def recv(self, fromName, msg):
		print(fromName, "--->", self._name, ":", msg)

#endregion

#region mediator 中介者

class Mediator(object):
	def __init__(self):
		self._onlineDict = {}
	
	def register(self, obj):
		self._onlineDict[str(obj)] = obj
	
	def send(self, fromName, toName, msg):
		if fromName in self._onlineDict and toName in self._onlineDict:
			self._onlineDict[toName].recv(fromName, msg)


#endregion

#region main

if __name__ == "__main__":
	# for arg in sys.argv:  
	# 	print(arg)

	print("Start!")
	
	mediator = Mediator()
	user_a = User("小明")
	user_b = User("小王")
	mediator.register(user_a)
	mediator.register(user_b)

	mediator.send(str(user_a), str(user_b), "你好啊")

	print("Done!")


#endregion
