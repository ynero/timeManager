
from src.Clock import CTime
class AlarmClock:
	def __init__ (self):
		self.AlarmTime = CTime(12,0,0)
		self.Alarm = False
		self.AlarmDays = [False, False, False, False, False, False, False]
		
	def SetAlarmTime(self, t):
		self.AlarmTime = t;
		
	def SetAlarmDays(self, days):
		self.AlarmDays = days;
		
	def SetAlarmOn(self):
		self.Alarm = True
		
	def SetAlarmOff(self):
		self.Alarm = False
		
	def isAlarmOn(self):
		return self.Alarm
		
	def GetAlarmTime(self):
		return self.AlarmTime
		
	def GetAlarmDays(self):
		return self.AlarmDays
	
