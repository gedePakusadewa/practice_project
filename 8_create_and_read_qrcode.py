# https://www.freecodecamp.org/news/python-projects-for-beginners#qr-code-encoder-decoder-python-project
# bikin gambar qrcode dan ngeread gambar qrcode

# ---- first version

# def create_qrcode(textContent, filename):
# 	import qrcode as qr
# 	img = qr.make(textContent)
# 	img.save(filename + ".png")

# def read_qrcode(filename):
# 	# https://stackoverflow.com/a/68551577
# 	import cv2

# 	image = cv2.imread(filename + ".png")
# 	detector = cv2.QRCodeDetector()
# 	data, vertices_array, binary_qrcode = detector.detectAndDecode(image)

# 	if vertices_array is not None:
# 	  print(f"QRCode data: {data}")
# 	else:
# 	  print("There was some error")

# isStop = False
# while isStop == False:
# 	print("\n")
# 	print("Type 'Generate' to generate image in png format")
# 	print("Type 'Read' to read image in png format")
# 	print("Type 'Stop/stop' to exit")

# 	inp = input("Your answer -> ")

# 	if inp.lower() == 'generate':
# 		content = input("The qr code content -> ")
# 		filename = input("The qr code image filename -> ")
# 		create_qrcode(content, filename)

# 		print("please check the generated image")
# 	elif inp.lower() == "read":
# 		filename = input("The qr code image filename -> ")

# 		read_qrcode(filename)
# 	elif inp.lower() == "stop":
# 		isStop = True

# --- second version

class SimpleQRCode():

	def __init__(self):
		self.filename = ""
		self.content = ""
		self.isStop = False

	def create_qrcode(self):
		import qrcode as qr

		img = qr.make(self.content)
		img.save(self.filename + ".png")

		print("----Success Create Image QRCode---- \n")

	def read_qrcode(self):
		# https://stackoverflow.com/a/68551577
		import cv2

		image = cv2.imread(self.filename + ".png")
		detector = cv2.QRCodeDetector()
		data, vertices_array, binary_qrcode = detector.detectAndDecode(image)

		if vertices_array is not None:
			print(f"QRCode data-> {data}")
		else:
		 	print("There was some error")

	def start(self):
		while self.isStop == False:
			print("\n")
			print("Type 'Generate' to generate image in png format")
			print("Type 'Read' to read image in png format")
			print("Type 'Stop/stop' to exit")

			inp = input("Your choice -> ")

			if inp.lower() == 'generate':
				self.content = input("The qr code content -> ")
				self.filename = input("The qr code image filename -> ")
				
				self.create_qrcode()

				print("please check the generated image")
			elif inp.lower() == "read":
				self.filename = input("The qr code image filename -> ")

				self.read_qrcode()
			elif inp.lower() == "stop":
				self.isStop = True


tes1 = SimpleQRCode()
tes1.start()