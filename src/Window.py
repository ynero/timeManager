
import tkinter as tk
from tkinter import Label
from src.Clock import CTime
from src.Clock import WeekDays
from src.lang import TM_Lang

class Model():
	def __init__(self, TManager, title, width, height, clockFont):
		root = tk.Tk()
		gem = str(width) + "x" + str(height)
		root.geometry(gem)
		self.TimeManager = TManager
		self.mWin = MainWindow(root, self, title, width, height, clockFont)
		
	def ConverTimetoStr(self, t):
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
		return tm
		
	def UpdateTime(self, t):
		tm = self.ConverTimetoStr(t)
		self.mWin.UpdateTime(tm)

	def UpdateAlarm(self, ON, t, d):
		if(t == None):
			tm = TM_Lang['NO_ALARM']
		else:
			tm = self.ConverTimetoStr(t)
		self.mWin.UpdateAlarmTime(tm)
		
		if(ON):
			AlarmState = TM_Lang['ON']
			AlarmColor = "green"
		else:
			AlarmState = TM_Lang['OFF']
			AlarmColor = "red"
		self.mWin.UpdateAlarmOn(AlarmState, AlarmColor)
		self.mWin.UpdateAlarmDays(d)
		
	def OpenSetupScreen(self):
		print("Model: OpenSetupScreen")

	def ExitButtonClick(self):
		print("Model: ExitButtonClick")

	def TurnOnOffAlarm(self):
		print("Model: TurnOnOffAlarm")

	def OpenAlarmScreen(self):
		print("Model: OpenAlarmScreen")
		
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
	def __init__(self, parent,model, title, width, height, ClockFont):
		Window.__init__(self, parent, title, width, height)
		self.ClockLabelText = TM_Lang['CLOCK']
		self.ClockLabelTextColor = "blue"
		self.ClockLabelTextSize = 40
		self.DaysLabelTextSize = 20
		self.ClockTimeColor = "blue"
		self.ClockTimeSize = 80
		self.ClockFont = ClockFont
		self.QuitButtonText = TM_Lang['QUIT']
		self.SetupButtonText = TM_Lang['SETUP']
		self.AlramOnOffButtonText = TM_Lang['TURN_ALARM_ON_OFF']
		self.AlarmScreenButtonText = TM_Lang['ALARM_SCREEN']
		self.AlarmDays_labels = []
		
		#CLOCK
		self.model = model
		self.mWinCont = MainWinController(self.model)
		self.clock_label = Label(self.canvas,  text=self.ClockLabelText, relief=tk.FLAT, fg=self.ClockLabelTextColor)
		self.clock_label.config(font=(self.ClockFont, self.ClockLabelTextSize))
		self.clock_label.pack()
		self.HH_label = Label(self.canvas, text="", relief=tk.FLAT, fg=self.ClockTimeColor)
		self.HH_label.config(font=(self.ClockFont, self.ClockTimeSize))
		self.HH_label.pack()
		
		#ALARM CLOCK
		self.AlarmFrame = tk.Frame(self.canvas)
		self.AlarmFrame.pack()
		self.AlarmText_label = Label(self.canvas,  text=TM_Lang['ALARM'], relief=tk.FLAT, fg=self.ClockLabelTextColor)
		self.AlarmText_label.config(font=(self.ClockFont, self.ClockLabelTextSize))
		self.AlarmText_label.pack(in_=self.AlarmFrame, side = tk.LEFT)
		self.AlarmOnOff_label = Label(self.canvas,  text="", relief=tk.FLAT, fg=self.ClockLabelTextColor)
		self.AlarmOnOff_label.config(font=(self.ClockFont,self.ClockTimeSize))
		self.AlarmOnOff_label.pack(in_=self.AlarmFrame, side = tk.LEFT)
		
		self.AlarmTime_label = Label(self.canvas,  text="", relief=tk.FLAT, fg=self.ClockLabelTextColor)
		self.AlarmTime_label.config(font=(self.ClockFont, self.ClockTimeSize))
		self.AlarmTime_label.pack()
		
		#Days
		self.DaysFrame = tk.Frame(self.canvas)
		self.DaysFrame.pack()

		for i in range(0,len(WeekDays)):
			self.AlarmDays_labels.append(Label(self.canvas,  text="", relief=tk.FLAT, fg=self.ClockLabelTextColor))
			self.AlarmDays_labels[i].config(font=(self.ClockFont, self.DaysLabelTextSize))
			self.AlarmDays_labels[i].pack(in_=self.DaysFrame, side = tk.LEFT)

		
		#SEPARATOR
		l = Label(self.canvas,  text="")
		l.pack()
		#BUTTONS
		bottom = tk.Frame(self.canvas)
		bottom.pack()
		self.SetupButton = tk.Button(self.canvas, text=self.SetupButtonText, command = self.SetupButtonClick)
		self.SetupButton.pack(in_=bottom, side = tk.LEFT)
		l1 = Label(bottom, text="  ", relief=tk.FLAT)
		l1.pack(in_=bottom, side = tk.LEFT)
		self.QuitButton = tk.Button(self.canvas, text=self.QuitButtonText, command = self.ExitButtonClick)
		self.QuitButton.pack(in_=bottom, side = tk.LEFT)
		l2 = Label(self.canvas, text="  ", relief=tk.FLAT)
		l2.pack(in_=bottom, side = tk.LEFT)
		self.AlarmOnOffButton = tk.Button(self.canvas, text=self.AlramOnOffButtonText, command = self.AlarmOnOffButtonClick)
		self.AlarmOnOffButton.pack(in_=bottom, side = tk.LEFT)
		l3 = Label(self.canvas, text="  ", relief=tk.FLAT)
		l3.pack(in_=bottom, side = tk.LEFT)
		self.AlarmScreenButton = tk.Button(self.canvas, text=self.AlarmScreenButtonText, command = self.AlramScreenButtonClick)
		self.AlarmScreenButton.pack(in_=bottom, side = tk.LEFT)
	
	def SetupButtonClick(self):
		self.mWinCont.SetupButtonClick()

	def ExitButtonClick(self):
		self.mWinCont.ExitButtonClick()

	def AlarmOnOffButtonClick(self):
		self.mWinCont.AlarmOnOffButtonClick()

	def AlramScreenButtonClick(self):
		self.mWinCont.AlramScreenButtonClick()
		
	def UpdateTime(self, t):
		self.HH_label.config(font=(self.ClockFont, self.ClockTimeSize), text=t)
		self.HH_label.pack()

	def UpdateAlarmTime(self, t):
		self.AlarmTime_label.config(font=(self.ClockFont, self.ClockTimeSize), text=t)
		self.AlarmTime_label.pack()
		
	def UpdateAlarmOn(self, AlarmState, AlarmStateColor):
		self.AlarmOnOff_label.config(font=(self.ClockFont, self.ClockLabelTextSize), text=AlarmState, fg=AlarmStateColor)
		self.AlarmOnOff_label.pack(in_=self.AlarmFrame, side = tk.LEFT)
	
	def UpdateAlarmDays(self, d):
		for i in range(0,len(d)):
			if(d[i]==True):
				color = "grey"
			else:
				color = 'light grey'
			self.AlarmDays_labels[i].config(font=(self.ClockFont, self.DaysLabelTextSize), text=WeekDays[i], fg=color)
			self.AlarmDays_labels[i].pack()


class MainWinController():
	def __init__(self, model):
		self.model = model
		
	def SetupButtonClick(self):
		self.model.OpenSetupScreen()

	def ExitButtonClick(self):
		self.model.ExitButtonClick()

	def AlarmOnOffButtonClick(self):
		self.model.TurnOnOffAlarm()

	def AlramScreenButtonClick(self):
		self.model.OpenAlarmScreen()
		
