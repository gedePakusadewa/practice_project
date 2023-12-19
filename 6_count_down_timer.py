#https://www.freecodecamp.org/news/python-projects-for-beginners#countdown-timer-python-project
# buat command lind count down berdasarkan input waktu dari user


# ----- first version
# import time
# import sys

# inputUser = int(input("Masukkan durasi timer -> "))

# def changeFormat(value):
# 	if value < 10:
# 		return "00:0" + str(value)
# 	elif value >= 10  and value < 60:
# 		return "00:" + str(value)

# for x in range(inputUser, 0, -1):
# 	sys.stdout.flush()
# 	time.sleep(1)
# 	print(changeFormat(x), end="\r")


# --- second version

# import time
# import sys

# class CountDown():
# 	def __init__(self):
# 		pass

# 	def changeFormat(self, value):
# 		if value < 10:
# 			return "00:0" + str(value)
# 		elif value >= 10  and value < 60:
# 			return "00:" + str(value)

# 	def run(self):
# 		inSec = int(input("Masukkan durasi timer detik -> "))

# 		for x in range(inSec, -1, -1):
# 			sys.stdout.flush()
# 			time.sleep(1)
# 			print(self.changeFormat(x), end="\r")

# tes1 = CountDown()
# tes1.run()

# --- third version

import time

class CountDown():
	def __init__(self):
		pass

	def timer(self, t):
		while t:
			mins, secs = divmod(t, 60)
			text = '{:02d}:{:02d}'.format(mins, secs)
			print(text, end="\r")
			time.sleep(1)
			t -= 1

	def run(self):
		inSec = int(input("Masukkan durasi timer detik -> "))

		self.timer(inSec)

tes1 = CountDown()
tes1.run()
