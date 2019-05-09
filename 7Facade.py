#!/usr/bin/python
#coding=utf-8
#desc:7. 门面模式、外观模式 Facade Pattern
#举行婚礼，委托给专门的婚庆经理的例子

#region 子系统

class Hotelier(object):
	def __init__(self):
		print("Arranging the Hotel for Marriage? 预定结婚的酒店吗")

	def __isAvailable(self):
		print("Is the Hotel free for the event on given day? 检查预定哪天有空酒店可以预定吗")
		return True

	def bookHotel(self):
		if self.__isAvailable():
			print("Registered the Booking.预定酒店成功. ")


class Florist(object):
	def __init__(self):
		print("Flower Decorations for the Event? 需要活动的花卉装饰吗")

	def setFlowerRequirements(self):
		print("Carnations, Roses and Lilies would be used for Decorations康乃馨，玫瑰和百合将用于装饰。. ;")


class Caterer(object):
	def __init__(self):
		print("Food Arrangements for the Event. 活动的餐食")

	def setCuisine(self):
		print("Chiness && Contiental Cuisine to be served.提供中式和欧式美食")

class Musician(object):
	def __init__(self):
		print("Musical Arrangements for the Marriage.")

	def setMusicType(self):
		print("Jazz and Classical will be played. 古典和爵士类型的音乐")

#endregion


#region 婚庆经理 相当于uml中的Facade类

class EventManager(object):

	def __init__(self):
		print("Event Manager:Let me talk to the folks 谈谈预定安排 ...")

	def arrange(self):
		self.hotelier = Hotelier()
		self.hotelier.bookHotel()

		self.florist = Florist()
		self.florist.setFlowerRequirements()

		self.caterer = Caterer()
		self.caterer.setCuisine()

		self.musician = Musician()
		self.musician.setMusicType()

		print("arrange done.----------")

#endregion


#region Client端

class You(object):
	def __init__(self):
		print("You:Whoa!Marriage Arrangements? 啥，婚礼安排？")

	def askEventManager(self):
		print("You:Let's Contract the Event Manager.还是联系婚庆经理\n\n")
		em = EventManager()
		em.arrange()
	
	def __del__(slef):
		print("You: Thanks to Event Manager, all preparations done!")

#endregion




if __name__ == "__main__":
	# for arg in sys.argv:  
	# 	print(arg)

	print("Start!\n\n")

	you = You()
	you.askEventManager()
	
	print("Done!")