import numpy
import matplotlib.pyplot as plt


train_file = open("neutralNetwork/train.csv", "r")
train_data = train_file.readlines()
train_file.close()
all_values = train_data[0].split(',')
image_array = numpy.asfarray(all_values[1:]).reshape((28, 28))
plt.imshow(image_array, cmap='Greys', interpolation='None')

