#!/usr/bin/python
#coding=utf-8
#desc:3.TutorialsPoint 抽象工厂示例 Abstract Factory Patterns


class Window:
	__toolkit = ""
	__purpose = ""

	def __init__(self, toolkit, purpose):
		self.__toolkit = toolkit
		self.__purpose = purpose

	def getToolkit(self):
		return self.__toolkit

	def getPurpose(self):
		return self.__purpose

class GtkToolbox(Window):
	def __init__(self):
		Window.__init__(self, "Gtk Group", "Toolbox")

class GtkLayers(Window):
	def __init__(self):
		Window.__init__(self, "Gtk Group", "Layers")

class GtkMainWindow(Window):
	def __init__(self):
		Window.__init__(self, "Gtk Group", "MainWindow")

class QtToolbox(Window):
	def __init__(self):
		Window.__init__(self, "Qt Group", "Toolbox")

class QtLayers(Window):
	def __init__(self):
		Window.__init__(self, "Qt Group", "Layers")

class QtMainWindow(Window):
	def __init__(self):
		Window.__init__(self, "Qt Group", "MainWindow")


class AbstractUIFactory:
	def getToolbox(self): pass
	def getLayers(self): pass
	def getMainWindow(self): pass

class GtkUIFactory(AbstractUIFactory):
	def getToolbox(self):
		return GtkToolbox()
	def getLayers(self):
		return GtkLayers()
	def getMainWindow(self):
		return GtkMainWindow()

class QtUIFactory(AbstractUIFactory):
	def getToolbox(self):
		return QtToolbox()
	def getLayers(self):
		return QtLayers()
	def getMainWindow(self):
		return QtMainWindow()


if __name__ == "__main__":
	# for arg in sys.argv:  
	# 	print(arg)

	print("Start!\n\n")
	
	gnome = True
	kde = not gnome
	if gnome:
		ui = GtkUIFactory()
	elif kde:
		ui = QtUIFactory()

	toolbox = ui.getToolbox()
	layers = ui.getLayers()
	mainWin = ui.getMainWindow()
	print("TP Abstract Factory Demo:")
	print("%s:%s" % (toolbox.getToolkit(), toolbox.getPurpose()))
	print("%s:%s" % (layers.getToolkit(), layers.getPurpose()))
	print("%s:%s" % (mainWin.getToolkit(), mainWin.getPurpose()))
	
	print("Done!")