#!/usr/bin/python
#coding=utf-8
#desc:12.命令模式 Command Pattern
#股票交易例子

from abc import ABCMeta, abstractmethod




#region Command 接口

class Order(metaclass=ABCMeta):

    @abstractmethod
    def execute(self): pass

#endregion

#region ConcreteCommand 具体买卖命令 

class BuyStockOrder(Order):
    def __init__(self, stock):
        self.stock = stock
    
    def execute(self):
        self.stock.buy()

class SellStockOrder(Order):
    def __init__(self, stock):
        self.stock = stock

    def execute(self):
        self.stock.sell()


#endregion


#region Receiver 接收者

class StockTrade:
    def buy(self):
        print("你即将购买股票")

    def sell(self):
        print("你即将卖出股票")
        
#endregion


#region 调用者 Invoker

class Agent:
    def __init__(self):
        self.__orderQueue = []

    def placeOrder(self, order):
        self.__orderQueue.append(order)
        order.execute()

#endregion


if __name__ == "__main__":
    print("Start!")

    #client
    stock = StockTrade()
    buy = BuyStockOrder(stock)
    sell = SellStockOrder(stock)

    #invoker
    agent = Agent()
    agent.placeOrder(buy)
    agent.placeOrder(sell)
   

    print("Done!")