"""


	Compute Eigenface :

		a) We have dataset of each subject having 16 image of different style
		b) Each image is a point in N - dimensional space.
		c) We are required to compute a vector in N - dimensional space where a point on projecting a line from mean along this vector
			variance would be maximum.
"""

"""

	Computing Matrix A
"""
from PIL import Image
from os import listdir
from os.path import isfile, join
from os.path import splitext
import numpy as np

mean = np.genfromtxt("./mean.csv", delimiter = ",")
m, n = mean.shape[0], mean.shape[1]

mean = mean.reshape(m * n, 1)
At = np.zeros((5 * 16, m * n))
count = 0
for i in range(1, 6):
	mypath = "./S"
	mypath = mypath + str(i)
	for j in range(1, 17):
		z = mypath + "/" + str(j) + ".csv"
		imarray = np.genfromtxt(z, delimiter = ",")
		imarray = imarray.reshape(m * n)
		At[count] = imarray - mean
		print("Computed", At[count].shape)

		count = count + 1
np.savetxt("At.csv", At.astype(float), fmt = "%f", delimiter = ",")
L = np.dot(At, At.transpose())
from numpy import linalg
w, v = linalg.eig(L)
v = v.transpose()

mean1 = np.genfromtxt("./mean1.csv", delimiter = ",")
mean2 = np.genfromtxt("./mean2.csv", delimiter = ",")
mean3 = np.genfromtxt("./mean3.csv", delimiter = ",")
mean4 = np.genfromtxt("./mean4.csv", delimiter = ",")
mean5 = np.genfromtxt("./mean5.csv", delimiter = ",")

mean1 = mean.reshape(m * n, 1)
mean2 = mean.reshape(m * n, 1)
mean3 = mean.reshape(m * n, 1)
mean4 = mean.reshape(m * n, 1)
mean5 = mean.reshape(m * n, 1)


class1 = np.zeros((7, 1))
class2 = np.zeros((7, 1))
class3 = np.zeros((7, 1))
class4 = np.zeros((7, 1))
class5 = np.zeros((7, 1))

z = np.array(v[0 : 7,]) # Top eigenvectors

u = np.dot(At.transpose(), z.transpose())
u = u.transpose()
project = np.dot(At.transpose(), u.transpose())



datatest = np.genfromtxt("./S1/1.csv", delimiter = ",")
datatest = data1.reshape((m * n), 1)
classtest = np.zeros((7, 1))

for i in range(u[:, 0].size):
	class1[i] = np.dot(u[i].transpose(), (mean1 - mean))
	class2[i] = np.dot(u[i].transpose(), (mean2 - mean))
	class3[i] = np.dot(u[i].transpose(), (mean3 - mean))
	class4[i] = np.dot(u[i].transpose(), (mean4 - mean))
	class5[i] = np.dot(u[i].transpose(), (mean5 - mean))
	classtest = np.dot(u[i].transpose(), (datatest - mean))

def euclidean(classtest, classi):
	z = 0
	for i in range(classi[:, 0].size):
		z = z + abs(classtest[i] - classi[i])
	return z

def cmp(elemnt):
	return elemnt[1]
distanceVector = [(1,euclidean(classtest, class1)), (2, euclidean(classtest, class2), (3, euclidean(classtest, class3)), (4, euclidean(classtest, class4)), (5, euclidean(classtest, class5))]
distanceVector = sorted(distanceVector, key = cmp)
print("Class 1 distance ", euclidean(classtest, class1))
print("Class 2 distance ", euclidean(classtest, class2))
print("Class 3 distance ", euclidean(classtest, class3))
print("Class 4 distance ", euclidean(classtest, class4))
print("Class 5 distance ", euclidean(classtest, class5))
print(distanceVector)
