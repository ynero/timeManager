
from src.Clock import Clock


def main():
	cl = Clock()
	t = cl.GetCurrTime()
	print(t.GetHH12(),t.GetMM(),t.GetSS())
	print(cl.GetWeekDay())
	print(t.GetAmPm())
if __name__=='__main__':
	main()
