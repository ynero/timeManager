from enum import Enum
from src.Clock import CTime


class TestCTime:
	failResult = "Failed"
	successResult = "Success"
	class Result(Enum):
		OK = 0
		GetHH24_fail = 1
		GetHH12_fail = 2
		GetMM_fail = 3
		GetSS_fail = 4
		GetAmPm_fail = 5
	def test(self, hh, mm, ss, e12hh, e24hh, emm, ess, eam_pm):
		t = CTime(hh, mm, ss)
		if(t.GetAmPm() != eam_pm):
			return self.Result.GetAmPm_fail;
		if(t.GetHH12() != e12hh):
			return self.Result.GetHH12_fail;
		if(t.GetHH24() != e24hh):
			return self.Result.GetHH24_fail;
		if(t.GetMM() != emm):
			return self.Result.GetMM_fail;
		if(t.GetSS() != ess):
			return self.Result.GetSS_fail;
		return self.Result.OK

	def run(self):
		count = 0
		fail = False
	# TEST 1
		count+=1
		res = self.test(00, 23, 44, 12, 00, 23, 44, "AM")
		if(res!=self.Result.OK):
			print("TestCTime test{} failed {}\n".format(count, res));
			fail = True
	# TEST 2
		count+=1
		res = self.test(23, 12, 25, 11, 23, 12, 25, "PM")
		if(res!=self.Result.OK):
			print("TestCTime test{} failed {}\n".format(count, res));
			fail = True
	# TEST 3
		count+=1
		res = self.test(2, 12, 25, 2, 2, 12, 25, "AM")
		if(res!=self.Result.OK):
			print("TestCTime test{} failed {}\n".format(count, res));
			fail = True
		if(fail):
			return self.failResult
		return self.successResult
		

