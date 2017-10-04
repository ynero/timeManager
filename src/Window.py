
import tkinter as tk
from tkinter import Label
from src.Clock import CTime

class Model():
	def __init__(self, title, width, height):
		root = tk.Tk()
		root.geometry('800x600')
		self.mWin = MainWindow(root, title, width, height)
		self.mWinCont = MainWinController(self)
	def UpdateTime(self, t):
		str = t.GetHH12()
		self.mWin.UpdateTime(t)
 
	
class Window(tk.Frame):
	def __init__(self, parent, title, width, height):
		tk.Frame.__init__(self, parent)
		self.parent = parent
		self.width = width
		self.height = height
		self.title = title
		self.drawWindow()
		
	def drawWindow(self):
		self.parent.title(self.title)
		self.pack(fill = tk.BOTH, expand = 1)
		self.canvas = tk.Canvas(self, relief = tk.FLAT,  width = self.width, height = self.height)
		self.canvas.pack()

	def exit(self):
		self.quit()

class MainWindow(Window):
	def __init__(self, parent, title, width, height):
		Window.__init__(self, parent, title, width, height)
		self.clock_label = Label(self.canvas,  text="Clock", relief=tk.FLAT, fg="blue")
		self.clock_label.config(font=("Calibri", 50))
		self.clock_label.pack()
		self.HH_label = Label(self.canvas, text="", relief=tk.FLAT, fg="blue")
		self.HH_label.config(font=("Calibri", 100))
		self.HH_label.pack()
		
	def UpdateTime(self, t):
		hh = t.GetHH12()
		tm=""
		if(hh<10):
			tm ="0"
		tm += str(hh)
		tm +=":"
		mm = t.GetMM()
		if(mm<10):
			tm +="0"
		tm +=str(mm)
		tm +=":"
		ss = t.GetSS()
		if(ss<10):
			tm +="0"
		tm +=str(ss)
		#if(self.HH_label):
		#	self.HH_label.pack_forget()
		#self.HH_label = Label(self.canvas, text=tm, relief=tk.FLAT, fg="blue")
		self.HH_label.config(font=("Calibri", 100), text=tm)
		self.HH_label.pack()

class MainWinController():
	def __init__(self, model):
		self.model = model
		
