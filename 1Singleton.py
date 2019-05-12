#!/usr/bin/python
#coding=utf-8
#desc: 1.单利设计模式

import os,sys
from Core import MetaSingleton

DIR=os.getcwd()

class Singleton_B(object):
	'''
	1.覆盖用于实例化的特殊方法：__new__方法，来控制对象创建
	'''
	def __new__(cls):
		if not hasattr(cls, 'instance'):
			cls.instance = super(Singleton_B, cls).__new__(cls)
		return cls.instance

	@classmethod
	def Demo(cls):
		print("1.__new__方式")
		s1 = Singleton_B()
		s2 = Singleton_B()
		print("Object s1", s1, "id:", id(s1))
		print("Object s2", s2, "id:", id(s2))


class Singleton_lazy(object):
	'''
	2.懒汉式：延迟创建单利，在导入模块的时候可能会无意创建一个对象但当时根本用不到它，比如上面一上来就创建了静态对象，不论用不用，
	都在占用内存，懒汉式节约资源仅在需要时候才会创建静态对象
	__init__ 和 @classmethod 实现
	'''
	__instance = None
	def __init__(self):
		if not Singleton_lazy.__instance:
			print("__init__ method called")
		else:
			print("instance already created:", self.getInstance())

	#classmethod 修饰符对应的函数不需要实例化，不需要 self 参数，
	#但第一个参数需要是表示自身类的 cls 参数，可以来调用类的属性，类的方法，实例化对象等。
	@classmethod
	def getInstance(cls):
		if not cls.__instance:
			cls.__instance = Singleton_lazy()
		return cls.__instance

	@classmethod
	def Demo(cls):
		print("2.lazy 创建")
		sl1 = Singleton_lazy()
		
		print("------")
		# getInstance 是静态方法，可以用类直接掉
		# Singleton_lazy.getInstance()

		print("lazy Object s1", sl1.getInstance(), "id:", id(sl1.getInstance()))
		print("------")
		sl2 = Singleton_lazy()
		print("lazy Object s2", sl2.getInstance(), "id:", id(sl2.getInstance()))


class Logger(metaclass=MetaSingleton):
	"""	
	3.元类方式
	通过类的类，元类对类创建和对象实例化有更多的控制权
	覆盖__call__ 存在字典缓存中

	"""
	
	def __new__(cls):
		print("Logger New")
		return super(Logger, cls).__new__(cls)

	def __init__(self):
		print("Logger init.")

	@classmethod
	def Demo(cls):
		print("l1 == l2")
		l1 = Logger()
		l2 = Logger()
		print(l1, l2)






class Borg(object):
	'''
	Monostate 单例模式的一个变种
	让实例共享相同的状态，关注状态和行为
	主要使用__dict__实现
	object.__dict__
	A dictionary or other mapping object used to store an object’s (writable) attributes.
	类对象的Class.__dict__只返回当前类的属性字典，但不包含其基类的属性。
	dir(Class)会返回当前类以及它的所有基类的类属性名，即当前类及所有基类的__dict__键值。

	'''
	_shared_state = {}
	def __new__(cls, *args, **kwargs):
		obj = super(Borg, cls).__new__(cls, *args, **kwargs)
		obj.__dict__ = cls._shared_state
		return obj

	@classmethod
	def Demo(cls):
		b1 = Borg()
		b2 = Borg()
		b1.x = 10
		print("b1, b2 共享相同的__dict__属性所以里面的属性相同", b2.x)
		print("id(b1.x)==id(b2.x)", id(b1.x), id(b2.x))


#python设计模式一系列代码，大多在mac上写，后来在一次win10 运行单例模式，报错
#Sqlite3: ImportError: DLL load failed: The specified module could not be found.
#解决方案： https://stackoverflow.com/questions/54876404/unable-to-import-sqlite3
#下载64为sqlite.dll 放在 anaconda/DLLs 重启vscode，就没问题了
#https://www.sqlite.org/2019/sqlite-dll-win64-x64-3280000.zip

import sqlite3
class Database(metaclass=MetaSingleton):
	'''
	DB单例示例,基于元类MetaSingleton 装饰后，实现单例
	'''
	connection = None
	def connect(self):
		if self.connection is None:
			self.connection = sqlite3.connect("db.sqlite3")
			self.cursorobj = self.connection.cursor()
		return self.cursorobj

	@classmethod
	def Demo(cls):
		db1 = Database().connect()
		db2 = Database().connect()
		print(db1, db2)

		#操作sqlite3
		# db1.execute('create table Test (id integer primary key, name varchar(10))')
		# db1.execute('insert into Test values (100, "nice!")')
		# db1.connection.commit()
		# db1.execute('select * from Test')
		# print(db1.fetchall())


class TP_Singleton:
	'''
	TutorialsPoint 例子
	代码看起来太熟悉了，和java和c++写法一模一样
	一个静态的全局访问点，一个私有的构造函数
	'''
	__instance = None
	@staticmethod
	def getInstance():
		if TP_Singleton.__instance == None:
			TP_Singleton()
		return TP_Singleton.__instance

	def __init__(self):
		if TP_Singleton.__instance != None:
			raise Exception("THis class is a singleton!")
		else:
			print(self.__class__, "inited.")
			TP_Singleton.__instance = self

	@classmethod
	def Demo(cls):
		t1 = TP_Singleton.getInstance()
		t2 = TP_Singleton.getInstance()
		t3 = TP_Singleton.getInstance()
		print(t1, t2, t3)
		print("如果尝试再创建一个实例，就会触发异常")

if __name__ == "__main__":
	# for arg in sys.argv:  
	# 	print(arg)

	print("Start!\n\n")

	clsList = [Singleton_B, Singleton_lazy, Logger, Borg, Database, TP_Singleton]
	for c in clsList:
		print(c.__name__, c.__doc__)
		c.Demo()
		print(30*"=")

	print("Done!")



