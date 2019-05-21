#!/usr/bin/python
#coding=utf-8
#desc:16.Chain of Responsibility 责任链模式
#日志输出例子

from abc import ABCMeta, abstractmethod

#region base cls

class AbstractLogger(metaclass=ABCMeta):
	INFO = 1
	DEBUG = 2
	ERROR = 3

	def __init__(self, level):
		self._nextLogger = None
		# print(self, level)
		self._level = level

	def setNextLogger(self, nextLogger):
		self._nextLogger = nextLogger

	def logMessage(self, level, msg):
		if (self._level <= level):
			self.write(msg)
		if(self._nextLogger != None):
			self._nextLogger.logMessage(level, msg)	

	@abstractmethod
	def write(self, msg): pass

#endregion

#region 

class ConsoleLogger(AbstractLogger):
	
	def write(self, msg):
		print("Standard Console:", msg)

class ErrorLogger(AbstractLogger):
	
	def write(self, msg):
		print("Error Console:", msg)


class FileLogger(AbstractLogger):
	
	def write(self, msg):
		print("File Console:", msg)


#endregion


#region main

if __name__ == "__main__":
	# for arg in sys.argv:  
	# 	print(arg)

	print("Start!\n\n")
	
	errorLogger = ErrorLogger(AbstractLogger.ERROR)
	fileLogger = FileLogger(AbstractLogger.DEBUG)
	consoleLogger = ConsoleLogger(AbstractLogger.INFO)

	errorLogger.setNextLogger(fileLogger)
	fileLogger.setNextLogger(consoleLogger)

	#chain 
	loggerChain = errorLogger
	loggerChain.logMessage(AbstractLogger.INFO, "this is an information.")
	print(30*"-")

	loggerChain.logMessage(AbstractLogger.DEBUG, "This is a debug level information.")
	print(30*"-")

	loggerChain.logMessage(AbstractLogger.ERROR, "This is an error information.")
	print(30*"-")

	print("Done!")


#endregion
