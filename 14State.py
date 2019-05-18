#!/usr/bin/python
#coding=utf-8
#desc:14.状态模式 State Pattern
#电脑状态例子

#region State & concreteState 状态机

class ComputerState(object):
	name = "state"
	label = ""
	allowed = []

	def switch(self, state):
		if state.name in self.allowed:
			print("current:", self, "=>切换到新状态:", state.name, state.label)
			self.__class__ = state
		else:
			print("current:", self, "=>不能切换到：", state.name, state.label)

	def __str__(self):
		return self.name

class Off(ComputerState):
	name = "off"
	label = "关闭"
	allowed = ["on"]

class On(ComputerState):
	name = "on"
	label = "开启"
	allowed = ["off", "suspend", "hibernate"]

class Suspend(ComputerState):
	name = "suspend"
	label = "休眠"
	allowed = ["on"]

class Hibernate(ComputerState):
	name = "hibernate"
	label = "睡眠"
	allowed = ["on"]


	
#endregion

#region Context

class Computer(object):
	def __init__(self, model="HP"):
		self.model = model
		#默认状态
		self.state = Off()
	
	def change(self, state):
		self.state.switch(state)

#endregion



#region main

if __name__ == "__main__":
	# for arg in sys.argv:  
	# 	print(arg)

	print("Start!\n\n")
	
	comp = Computer()
	comp.change(On)
	comp.change(Off)
	comp.change(On)
	comp.change(Suspend)
	comp.change(Hibernate)
	comp.change(On)
	comp.change(Off)
	
	print("Done!")


#endregion
