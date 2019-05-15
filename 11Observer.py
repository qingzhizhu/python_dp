#!/usr/bin/python
#coding=utf-8
#desc:11.观察者模式 
#新闻机构发布新闻，订户通过电子邮件、移动设备、等形式订阅

from abc import ABCMeta, abstractmethod

#region Observer 观察者 , ConcreteObserver Email、 SMS、AnyOtherObserver 3个具体观察者

class Subscriber(metaclass=ABCMeta):

    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    @abstractmethod
    def update(self): pass

class EmailSubscriber(Subscriber):
    def __init__(self, publisher):
        Subscriber.__init__(self, publisher)

    def update(self):
        print(type(self).__name__, self.publisher.getNews())

    
class SMSSubscriber(Subscriber):
    def __init__(self, publisher):
        Subscriber.__init__(self, publisher)
    def update(self):
        print(type(self).__name__, self.publisher.getNews())


class AnyOtherObserver(Subscriber):
    def __init__(self, publisher):
        Subscriber.__init__(self, publisher)
    def update(self):
        print(type(self).__name__, self.publisher.getNews())



#endregion


#region Subject 主题

class NewsPublisher:

    def __init__(self):
        self.__subscribers = []
        self.__latestNews = None

    def attach(self, subscriber):
        self.__subscribers.append(subscriber)

    def detach(self):
        return self.__subscribers.pop()

    def subscribers(self):
        return [type(x).__name__ for x in self.__subscribers]

    def notifySubscribers(self):
        for sub in self.__subscribers:
            sub.update()

    def addNews(self, news):
        self.__latestNews = news

    def getNews(self):
        return "Got News:" + self.__latestNews

#endregion



if __name__ == "__main__":
    print("Start!")

    np = NewsPublisher()

    for clsSub in [SMSSubscriber, EmailSubscriber, AnyOtherObserver]:
        clsSub(np)

    print("订阅者：", np.subscribers())

    np.addNews("今天天气晴好")
    np.notifySubscribers()

    print("\n取消订阅:", type(np.detach()).__name__)
    print("现在订阅者：", np.subscribers())
    np.addNews("可以穿T恤，短裤")
    np.notifySubscribers()

    print("Done!")