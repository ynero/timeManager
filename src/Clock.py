
import datetime
from enum import Enum

WeekDays={
	0 : 'Mon',
	1 : 'Tue',
	2 : 'Wed',
	3 : 'Thu',
	4 : 'Fri',
	5 : 'Sat',
	6 : 'Sun',
}

class CTime:
	def __init__(self, hh, mm, ss):
		self.hh = hh
		self.mm = mm
		self.ss = ss
		
	def GetHH24(self):
		return self.hh
		
	def GetHH12(self):
		if(self.hh > 12):
			return self.hh-12
		elif(self.hh ==0):
			return 12;
		return self.hh
		
	def GetMM(self):
		return self.mm
		
	def GetSS(self):
		return self.ss
		
	def GetAmPm(self):
		if(self.hh > 12):
			return "PM"
		return "AM"

class Clock:	
	def GetCurrTime(self):
		self.lastTime = datetime.datetime.now()
		return CTime(self.lastTime.hour, self.lastTime.minute, self.lastTime.second)
		
	def GetWeekDay(self):
		return WeekDays[self.lastTime.weekday()]

