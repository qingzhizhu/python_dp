#!/usr/bin/python
#coding=utf-8
#desc:适配器模式，Adapter Pattern
#TP电水壶示例


#region Adaptee 适配者类

class EuropeanSocketInterface:
    def voltage(self): pass
    def live(self): pass
    def neutral(self): pass
    def earth(self): pass

class EuropeanSocket(EuropeanSocketInterface):
    def voltage(self):
        return 230
    def live(self):
        return 1
    def neutral(self):
        return -1
    def earth(self):
        return 0

#endregion

#region target 目标抽象类

class USASocketInterface:
    def voltage(self): pass
    def live(self): pass
    def neutral(self): pass
    

#endregion

#region Adapter 适配器类

class Adapter(USASocketInterface):
    '''
    适配器将欧洲的230V电压转成美国的110v电压
    '''

    __socket = None

    def __init__(self, socket):
        self.__socket = socket

    def voltage(self):
        return 110

    def live(self):
        return self.__socket.live()

    def neutral(self):
        return self.__socket.neutral()

#endregion


#region Client 客户端

class ElectricKettle:
    '''
    美国买的水壶，在欧洲使用
    '''
    __power = None

    def __init__(self, power):
        self.__power = power

    def boil(self):
        if self.__power.voltage() > 110:
            print("Kettle on Fire!") 
        else:
            if self.__power.live() == 1 and self.__power.neutral() == -1:
                print("Coffee time!")
            else:
                print("No power!")
#endregion

if __name__ == "__main__":
    print("Start!")
    print(ElectricKettle.__doc__)
    print(Adapter.__doc__)

    socket = EuropeanSocket()
    adapter = Adapter(socket)
    kettle = ElectricKettle(adapter)

    kettle.boil()
    
    print("Done!")
