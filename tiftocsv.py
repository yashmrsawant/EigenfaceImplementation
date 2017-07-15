from PIL import Image
from os import listdir
from os.path import isfile, join
from os.path import splitext
import numpy as np


sumarray = np.zeros((188, 140))
mean1 = np.zeros((188, 140))
mean2 = np.zeros((188, 140))
mean3 = np.zeros((188, 140))
mean4 = np.zeros((188, 140))
mean5 = np.zeros((188, 140))
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
for i in range(1, 7):
	mypath = "./S"
	mypath = mypath + str(i)
	onlyTIFFfiles = [f for f in listdir(mypath) if splitext(isfile(join(mypath, f)) and join(mypath, f))[1] == ".tif"]
	for tiffile in onlyTIFFfiles:
		imagePath = join(mypath, tiffile)
		image = Image.open(imagePath)
		image = image.resize((140, 188), Image.ANTIALIAS)
		imarray = np.array(image)
		sumarray = sumarray + imarray
		if i == 1:
			mean1 = mean1 + imarray
		if i == 2:
			mean2 = mean2 + imarray
		if i == 3:
			mean3 = mean3 + imarray
		if i == 4:
			mean4 = mean4 + imarray
		if i == 5:
			mean5 = mean5 + imarray
		if i == 6:
			mean6 = mean6 + imarray
		print(sumarray.shape)
		print(imarray.shape)
		imagecsv = str(splitext(tiffile)[0]) + ".csv"
		imagecsv = join(mypath, imagecsv)
		print("Saved to ", imagecsv)
		np.savetxt(imagecsv, imarray.astype(int), fmt = "%i", delimiter = ",")


sumarray = sumarray / (16 * 5)
mean1 = mean1 / 16
mean2 = mean2 / 16
mean3 = mean3 / 16
mean4 = mean4 / 16
mean5 = mean5 / 16
mean6 = mean6 / 16
np.savetxt("mean.csv", sumarray.astype(float),fmt = "%f", delimiter = ",")
np.savetxt("mean1.csv", mean1.astype(float), fmt = "%f", delimiter = ",")
np.savetxt("mean2.csv", mean2.astype(float), fmt = "%f", delimiter = ",")
np.savetxt("mean3.csv", mean3.astype(float), fmt = "%f", delimiter = ",")
np.savetxt("mean4.csv", mean4.astype(float), fmt = "%f", delimiter = ",")
np.savetxt("mean5.csv", mean5.astype(float), fmt = "%f", delimiter = ",")
np.savetxt("mean6.csv", mean6.astype(float), fmt = "%f", delimiter = ",")



