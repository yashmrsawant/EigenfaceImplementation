import numpy as np

At = np.genfromtxt("./At.csv", delimiter = ",")
print("At Loaded")
L = np.dot(At, At.transpose())
from numpy import linalg
w, v = linalg.eig(L)
v = v.transpose()

mean = np.genfromtxt("./mean.csv", delimiter = ",")
m, n = mean.shape[0], mean.shape[1]
mean = mean.reshape((m * n), 1)
mean1 = np.genfromtxt("./mean1.csv", delimiter = ",")
mean2 = np.genfromtxt("./mean2.csv", delimiter = ",")
mean3 = np.genfromtxt("./mean3.csv", delimiter = ",")
mean4 = np.genfromtxt("./mean4.csv", delimiter = ",")
mean5 = np.genfromtxt("./mean5.csv", delimiter = ",")
mean6 = np.genfromtxt("./mean6.csv", delimiter = ",")

mean1 = mean1.reshape(m * n, 1)
mean2 = mean2.reshape(m * n, 1)
mean3 = mean3.reshape(m * n, 1)
mean4 = mean4.reshape(m * n, 1)
mean5 = mean5.reshape(m * n, 1)
mean6 = mean6.reshape(m * n, 1)

class1 = np.zeros((7, 1))
class2 = np.zeros((7, 1))
class3 = np.zeros((7, 1))
class4 = np.zeros((7, 1))
class5 = np.zeros((7, 1))
class6 = np.zeros((7, 1))

z = np.array(v[0 : 7,]) # Top eigenvectors

u = np.dot(At.transpose(), z.transpose())
u = u.transpose()
print(u)
datatest = np.genfromtxt("./S4/1.csv", delimiter = ",")
datatest = datatest.reshape((m * n), 1)
classtest = np.zeros((7, 1))

for i in range(u[:, 0].size):
	class1[i] = np.dot(u[i].transpose(), (mean1 - mean))
	class2[i] = np.dot(u[i].transpose(), (mean2 - mean))
	class3[i] = np.dot(u[i].transpose(), (mean3 - mean))
	class4[i] = np.dot(u[i].transpose(), (mean4 - mean))
	class5[i] = np.dot(u[i].transpose(), (mean5 - mean))
    class6[i] = np.dot(u[i].transpose(), (mean6 - mean))
	classtest[i] = np.dot(u[i].transpose(), (datatest - mean))

print(class1)
print(classtest)
def euclidean(classtest, classi):
	z = 0
	for i in range(classi[:, 0].size):
		z = z + abs(classtest[i] - classi[i])
	return z
print("Class 1 distance ", euclidean(classtest, class1))
print("Class 2 distance ", euclidean(classtest, class2))
print("Class 3 distance ", euclidean(classtest, class3))
print("Class 4 distance ", euclidean(classtest, class4))
print("Class 5 distance ", euclidean(classtest, class5))
print("Class 6 distance ", euclidean(classtest, class6))

def cmp(elemnt):
	return elemnt[1]
distanceVector = [[1,euclidean(classtest, class1)], [2, euclidean(classtest, class2)], [3, euclidean(classtest, class3)], [4, euclidean(classtest, class4)], [5, euclidean(classtest, class5)]]
distanceVector = sorted(distanceVector, key = cmp)
print(distanceVector)
count = 0
total = 0
for i in range(1, 7):

	for j in range(1, 17):
		path = "./S" + str(i) + "/" + str(j) + ".csv"
		datatest = np.genfromtxt(path, delimiter = ",")
		datatest = datatest.reshape((m * n), 1)
		mindistance = 0.0
		mini = -1
		for k in range(u[:, 0].size):
			classtest[k] = np.dot(u[k].transpose(), (datatest - mean))
		euclideans = [[1, euclidean(classtest, class1)], [2, euclidean(classtest, class2)], [3, euclidean(classtest, class3)], [4, euclidean(classtest, class4)], [5, euclidean(classtest, class5)]]
		euclideans = sorted(euclideans, key = cmp)
		if euclideans[0][0] == i:
			print("Correctly Classified", str(path))
			count = count + 1
		total = total + 1
print("Correctly Classified ", count, "times")
print("Accuracy ", str(count * 100.0 / total), "%")
