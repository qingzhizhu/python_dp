#!/usr/bin/python
#coding=utf-8
#desc:22.Filter Pattern 过滤器模式
#单条件过滤和双条件过滤例子，如过滤男性或单身男性

from abc import ABCMeta, abstractmethod

#region Person， 在此类应用标准

class Person(object):
	def __init__(self, name, gender, martitalStatus):
		self._name = name
		self._gender = gender
		self._matitlStatus = martitalStatus
	
	def getName(self): return self._name
	
	def getGender(self): return self._gender
	
	def getMatiralStatus(self): return self._matitlStatus

	def __str__(self):
		return "Person:[Name:" + self._name + ", 性别:" + self._gender + ", 结婚状态:" + self._matitlStatus +"]" 

#endregion

#region 标准接口 Criteria

class Criteria(metaclass=ABCMeta):
	def meetCriteria(self, persons): pass

#endregion

#region Criteria 标准的实现类

class CriteriaMale(Criteria):
	def meetCriteria(self, persons):
		malePersons = []
		for p in persons:
			if p.getGender().lower() == "male":
				malePersons.append(p)
		return malePersons

class CriteriaFemale(Criteria):
	def meetCriteria(self, persons):
		females = []
		for p in persons:
			if p.getGender().lower() == "female":
				females.append(p)
		return females


class CriteriaSingle(Criteria):
	def meetCriteria(self, persons):
		singles = []
		for p in persons:
			if p.getMatiralStatus().lower() == "single":
				singles.append(p)
		return singles


class AndCriteria(Criteria):
	def __init__(self, criteria, otherCriteria):
		self._criteria = criteria
		self._otherCriteria = otherCriteria

	def meetCriteria(self, persons):
		firstCriteriaPersons = self._criteria.meetCriteria(persons)
		return self._otherCriteria.meetCriteria(firstCriteriaPersons)


class OrCriteria(Criteria):
	def __init__(self, criteria, otherCriteria):
		self._criteria = criteria
		self._otherCriteria = otherCriteria

	def meetCriteria(self, persons):
		firstCriteriaPersons = self._criteria.meetCriteria(persons)
		otherCriteriaPersons = self._otherCriteria.meetCriteria(persons)

		for p in otherCriteriaPersons:
			if p not in firstCriteriaPersons:
				firstCriteriaPersons.append(p)

		return firstCriteriaPersons

#endregion



#region main

def printPersons(label, persons):
	print(label)
	for p in persons:
		print(p)
	print(30*"-")	

if __name__ == "__main__":
	# for arg in sys.argv:  
	# 	print(arg)

	print("Start!")
	
	persons = []
	persons.append(Person("小明", "Male", "Single"))
	persons.append(Person("小王", "Male", "Married"))
	persons.append(Person("小花", "FeMale", "Married"))
	persons.append(Person("小香", "FeMale", "Single"))
	persons.append(Person("小强", "Male", "Single"))
	persons.append(Person("小刚", "Male", "Single"))
	
	c_male = CriteriaMale()
	c_female = CriteriaFemale()
	c_single = CriteriaSingle()
	c_singleAndMale = AndCriteria(c_single, c_male)
	c_singleOrFemale = OrCriteria(c_single, c_female)

	printPersons("男性:", c_male.meetCriteria(persons))
	printPersons("女性:", c_female.meetCriteria(persons))
	printPersons("单身的:", c_single.meetCriteria(persons))
	printPersons("双条件与:单身男性:", c_singleAndMale.meetCriteria(persons))
	printPersons("双条件或:女性或者单身:", c_singleOrFemale.meetCriteria(persons))



	print("Done!")


#endregion
