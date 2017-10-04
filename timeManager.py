
from src.Clock import Clock
from src.Window import Model
import tkinter as tk
from threading import Thread
import time
class makeThread (Thread):
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
		self.cl = Clock()
		self.model = Model("Time Manager", 700, 500)
	def run(self):
		self.timeThread = makeThread(self.TimeTick)
		self.timeThread.start()
	def TimeTick(self):
		t = self.cl.GetCurrTime()
		self.model.UpdateTime(t)
	def stop(self):
		self.timeThread.stop=True

			
def main():
	TM = TimeManager()
	TM.run()
	tk.mainloop()
	TM.stop()
if __name__=='__main__':
	main()
