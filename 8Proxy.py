#!/usr/bin/python
#coding=utf-8
#desc:8.代理模式 Proxy Pattern
#划卡购物例子,就不用拿现金买了,微信是另外一种代理

from abc import ABCMeta, abstractmethod

#region Subject 主题，主题是由代理和真实主题实现的接口

class Payment(metaclass=ABCMeta):

	@abstractmethod
	def do_pay(self): pass

#endregion 


#region RealSubject 真实主题，实际系统
 
class Bank(Payment):
	'''
	Bank 完成从账户向商家账户划账的工作，为了简单起见，getAccount返回账号和借记卡号相同
	'''
	def __init__(self):
		self.card = None
		self.account = None
	
	def __getAccount(self):
		#assume card number is account number,to easy
		self.account = self.card

		return self.account

	def __hasFunds(self):
		print("检查账户", self.__getAccount(), "has enough funds.")
		return True

	def setCard(self, card):
		self.card = card

	def do_pay(self):
		if self.__hasFunds():
			print("Bank:给商家付款")
			return True
		else:
			print("Bank:余额不足")
			return False


#endregion
 

#region Proxy 借记卡，充当真实主题（银行）的代理

class DebitCard(Payment):
	def __init__(self):
		self.bank = Bank()

	def do_pay(self):
		card = "11123365-5666" #input("Proxy:输入卡号：")
		self.bank.setCard(card)
		return self.bank.do_pay()

#endregion

#region Client

class You:
	def __init__(self):
		print("买件衬衣吧")
		self.debitCard = DebitCard()
		self.isPurchased = None

	def make_payment(self):
		self.isPurchased = self.debitCard.do_pay()

	def __del__(self):
		if self.isPurchased:
			print("买到了不错的衬衣 :-)")
		else:
			print("钱不够买")


#endregion

if __name__ == "__main__":
	# for arg in sys.argv:  
	# 	print(arg)

	print("Start!\n\n")
	print("划卡购物例子,就不用拿现金买了,微信是另外一种代理\n")
	you = You()
	you.make_payment()
	
	print("Done!")