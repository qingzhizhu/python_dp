#!/usr/bin/python
#coding=utf-8
#desc:基类



#region MetaSingleton 单例元类
class MetaSingleton(type):
	'''
	单例类的元类,使用方式：metaclass=MetaSingleton
	'''
	_instances = {}

	def __call__(cls, *args, **kwargs):
		'''
		形参列表的*args表示任何多个无名参数，它是一个tuple；**kwargs表示关键字参数，它是一个dict。
		如果是在语句中*args 表示解包把元组序列解包成位置参数，**kwargs解包成关键字参数
		'''

		print("__call__", cls, *args, **kwargs)
		if cls not in cls._instances:
			print(' not in dict list ')
			cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
		return cls._instances[cls]


	def __init__(self, p1, p2, p3):
		print("MetaSingleton __init__",self, "p1=",p1,  "p2=",p2)#,  "p3=",p3)
	
#endregion


#region Prototype 原型基类 包含深浅copy, 相当于java 的 Cloneable
import copy

class Prototype:
	
	def clone(self):
		return copy.copy(self)
	def deepclone(self):
		return copy.deepcopy(self)

#endregion

