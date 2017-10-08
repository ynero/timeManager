
import tkinter as tk
from tkinter import Label
from src.Clock import CTime


class Model():
	def __init__(self, title, width, height, clockFont):
		root = tk.Tk()
		gem = str(width) + "x" + str(height)
		root.geometry(gem)
		self.mWin = MainWindow(root, title, width, height, clockFont)
		self.mWinCont = MainWinController(self)
		
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
		self.mWin.UpdateTime(tm)
 
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
	def __init__(self, parent, title, width, height, ClockFont):
		self.ClockLabelText = "Clock"
		self.ClockLabelTextColor = "blue"
		self.ClockLabelTextSize = 50
		self.ClockTimeColor = "blue"
		self.ClockTimeSize = 100
		self.ClockFont = ClockFont

		Window.__init__(self, parent, title, width, height)
		self.clock_label = Label(self.canvas,  text=self.ClockLabelText, relief=tk.FLAT, fg=self.ClockLabelTextColor)
		self.clock_label.config(font=(self.ClockFont, self.ClockLabelTextSize))
		self.clock_label.pack()
		self.HH_label = Label(self.canvas, text="", relief=tk.FLAT, fg=self.ClockTimeColor)
		self.HH_label.config(font=(self.ClockFont, self.ClockTimeSize))
		self.HH_label.pack()
		
	def UpdateTime(self, t):
		self.HH_label.config(font=(self.ClockFont, self.ClockTimeSize), text=t)
		self.HH_label.pack()

class MainWinController():
	def __init__(self, model):
		self.model = model
		
