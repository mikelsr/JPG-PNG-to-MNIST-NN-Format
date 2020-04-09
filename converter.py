import numpy, imageio, os
from random import shuffle

WIDTH = 28
HEIGHT = 28
CHANNELS = 1  # 3 for RGB

def write_labeldata(labeldata, outputfile):
	header = numpy.array([0x0801, len(labeldata)], dtype='>i4')
	with open(outputfile, "wb") as f:
		f.write(header.tobytes())
		f.write(labeldata.tobytes())

def write_imagedata(imagedata, outputfile):
	header = numpy.array([0x0803, len(imagedata), WIDTH, HEIGHT], dtype='>i4')
	with open(outputfile, "wb") as f:
		f.write(header.tobytes())
		f.write(imagedata.tobytes())

# Load from and save to
Names = [('./training-images','./custom/train'), ('./test-images','./custom/test')]

# Create save-to directory
try:
	os.makedirs('custom')
except FileExistsError:
	pass

for name in Names:
	rawImage = []
	rawLabel = []

	FileList = []
	for dirname in os.listdir(name[0]): # [1:] Excludes .DS_Store from Mac OS
		path = os.path.join(name[0], dirname)
		print("Get files in %s dir" % (path))
		for filename in os.listdir(path):
			if filename.endswith(".jpg") or filename.endswith(".png"):
				FileList.append(os.path.join(name[0],dirname,filename))

	shuffle(FileList) # Usefull for further segmenting the validation set

	for filename in FileList:
		label = int(filename.split('/')[2])
		image = imageio.imread(filename)
		print("Read data of %s" % (label))
		rawImage.append(image)
		rawLabel.append(label) # labels start (one unsigned byte each)

	# https://github.com/davidflanagan/notMNIST-to-MNIST/blob/17823f4d4a3acd8317c07866702d2eb2ac79c7a0/convert_to_mnist_format.py#L83-L90
	count = len(rawImage)
	if CHANNELS == 3:
		imagedata = numpy.zeros((count, WIDTH, HEIGHT, CHANNELS), dtype=numpy.uint8)
	else:
		imagedata = numpy.zeros((count, WIDTH, HEIGHT), dtype=numpy.uint8)

	labeldata = numpy.zeros(count, dtype=numpy.uint8)
	for i in range(0, len(FileList)):
		try:
			imagedata[i] = rawImage[i]
		except ValueError as err:
			print(f"Check that '{FileList[i]}' isn't a grayscale image")
			raise err
		labeldata[i] = rawLabel[i]
	write_imagedata(imagedata, name[1] + '-images-idx3-ubyte')
	write_labeldata(labeldata, name[1] + '-labels-idx1-ubyte')

# gzip resulting files
for name in Names:
	os.system('gzip ' + name[1] + '-images-idx3-ubyte')
	os.system('gzip ' + name[1] + '-labels-idx1-ubyte')
