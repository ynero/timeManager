
from src.Clock import Clock
from src.Clock import CTime
from src.AlarmClock import AlarmClock
from src.Window import Model
import tkinter as tk
from threading import Thread
import time

TimeManagerWinWidth = 700
TimeManagerWinHeight = 550
TimeManagerTitle = "Time Manager"
TimeManagerClockFont = "Calibri"

class TimeThread (Thread):
	def __init__ (self,func):
		Thread.__init__(self)
		self.__action = func
		self.stop = False

	## Starts this thread.
	#
	def run (self):
		while(self.stop!=True):
			self.__action()
			time.sleep(1)
				
class TimeManager():
	def __init__ (self):
		self.CL = Clock()
		self.AlarmCL = AlarmClock()
		self.model = Model(self, TimeManagerTitle, TimeManagerWinWidth, TimeManagerWinHeight,TimeManagerClockFont)
		
	def UpdateAlarm(self, t, days):
		self.AlarmCL.SetAlarmTime(t)
		self.AlarmCL.SetAlarmDays(days)
		
	def run(self):
		self.timeThread = TimeThread(self.TimeTick)
		self.timeThread.start()
		
	def TimeTick(self):
		t = self.CL.GetCurrTime()
		self.model.UpdateTime(t)
		ON = self.AlarmCL.isAlarmOn()
		ta = self.AlarmCL.GetAlarmTime()
		d = self.AlarmCL.GetAlarmDays()
		self.model.UpdateAlarm(ON, ta, d)
		
	def stop(self):
		self.timeThread.stop=True

			
def main():
	TM = TimeManager()
	TM.run()
	tk.mainloop()
	TM.stop()

if __name__=='__main__':
	main()
