#!/usr/bin/python
#coding=utf-8
#desc:20.组合模式 Composite Pattern

#region 节点叶子类

class Leaf(object):

	def add(self):
		pass
	
	def __str__(self):
		return "叶子"

#endregion

#region 分支类

class Branch(object):
	def __init__(self):
		super().__init__()
		self.branch = []
		self.leaf = []

	def add(self, obj):
		if type(obj) == Branch:
			self.branch.append(obj)
		else:
			self.leaf.append(obj)

	def __str__(self):
		content = ""
		for bran in self.branch:
			content +=  str(bran) 
		return "分支" + str([str(leaf) for leaf in self.leaf]) + "\n" + content

#endregion


#region main

if __name__ == "__main__":
	# for arg in sys.argv:  
	# 	print(arg)

	print("Start!")
	branch_a = Branch()
	branch_a.add(Leaf())
	branch_a.add(Leaf())

	branch_b = Branch()
	branch_b.add(Leaf())
	branch_b.add(branch_a)

	branch_main = Branch()
	branch_main.add(branch_b)

	print(branch_main)
	
	print("Done!")


#endregion
