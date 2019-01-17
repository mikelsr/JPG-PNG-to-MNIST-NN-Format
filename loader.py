import gzip
import numpy as np

width = 96
height = 96
channels = 3

files = [
  './custom/train-labels-idx1-ubyte.gz',
	'./custom/train-images-idx3-ubyte.gz',
	'./custom/test-labels-idx1-ubyte.gz',
	'./custom/test-images-idx3-ubyte.gz'
]

# https://github.com/tensorflow/tensorflow/blob/9088cf61c564bba09c6c025c9383f38142326ef3/tensorflow/python/keras/datasets/fashion_mnist.py
with gzip.open(files[0], 'rb') as lbpath:
  labels_train = np.frombuffer(lbpath.read(), np.uint8, offset=8)

with gzip.open(files[1], 'rb') as imgpath:
	images_train = np.frombuffer(
	imgpath.read(), np.uint8, offset=16).reshape(len(labels_train), width, height, channels)

with gzip.open(files[2], 'rb') as lbpath:
	labels_test = np.frombuffer(lbpath.read(), np.uint8, offset=8)

with gzip.open(files[3], 'rb') as imgpath:
	images_test = np.frombuffer(
	imgpath.read(), np.uint8, offset=16).reshape(len(labels_test), width, height, channels)

images_train = np.expand_dims(images_train, axis=3) / 255.0
images_test = np.expand_dims(images_test, axis=3) / 255.0
labels_train = np.expand_dims(labels_train, axis=1)
unique_train_label = np.unique(labels_train)
map_train_label_indices = {label: np.flatnonzero(labels_train == label) for label in unique_train_label}
print("Images train :", images_train.shape)
print("Labels train :", labels_train.shape)
print("Images test  :", images_test.shape)
print("Labels test  :", labels_test.shape)
print("Unique label :", unique_train_label)
