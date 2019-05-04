#!/usr/bin/python
#coding=utf-8
#desc:简单工厂&工厂方法

from abc import ABCMeta, abstractmethod

class Animal(metaclass = ABCMeta):
	'''
	定义抽象类Animal
	'''

	@abstractmethod
	def do_say(self):
		pass
	
class Dog(Animal):
	
	def do_say(self):
		print("Bhow bhow!")

class Cat(Animal):
	def do_say(self):
		print("Miaow!")

#实例化的时候才 TypeError: Can't instantiate abstract class Mouse with abstract methods do_say
# class Mouse(Animal):
# 	pass


class ForestFactory(object):
	'''
	简单工厂示例
	在此 eval 相当于java的反射了，写法更简单粗暴
	'''

	def make_sound(self, object_type):
		return eval(object_type)().do_say()


#=====================================

class Section(metaclass=ABCMeta):
	'''
	抽象类Section 部分、区域, 相当于uml的Product
	'''
	@abstractmethod
	def describe(self):
		pass
	
class PersonalSection(Section):
	'''
	个人展示区 相当于uml的ConcreteProduct 具体产品
	'''
	def describe(self):
		print("Personal Section")
		
class AlbumSection(Section):
	def describe(self):
		print("Album Section")

class PatentSection(Section):
	'''
	专利区
	'''
	def describe(self):
		print("Patent Section")

class PublicationSection(Section):
	'''
	出版作品区
	'''
	def describe(self):
		print("Publication Section")

class Profile(metaclass=ABCMeta):
	'''
	工厂方法示例
	抽象类 人物简介 工厂，如uml的Creator类
	'''
	def __init__(self):
		self.sections = []
		self.createProfile()

	@abstractmethod
	def createProfile(self):
		pass

	def getSections(self):
		return self.sections
	def addSections(self, section):
		self.sections.append(section)


class LinkedinProfile(Profile):
	'''
	Linkedin 个人简介 相当于uml ConcreteCreator 具体工厂
	'''
	def createProfile(self):
		self.addSections(PersonalSection())
		self.addSections(PatentSection())
		self.addSections(PublicationSection())


class FacebookProfile(Profile):
	def createProfile(self):
		self.addSections(PersonalSection())
		self.addSections(AlbumSection())



if __name__ == "__main__":
	# for arg in sys.argv:  
	# 	print(arg)

	print("Start!\n\n")

	print(ForestFactory.__doc__)
	ff = ForestFactory()
	animal = input("which animal should make_sound Dog or Cat?")
	ff.make_sound(animal)


	print(30*"=")

	print(Profile.__doc__)
	profile_type = input("Which Profile you'd like to create? [LinkedinProfile or FacebookProfile]")	
	profile = eval(profile_type)()
	print("Createing Profile ... ", type(profile).__name__)
	print("Profile has sections :", profile.getSections())
	print("Done!")