import scipy.misc
import numpy as np


img = np.genfromtxt("./S1/1.csv").astype(np.uint8)

scipy.misc.imsave("1.png", img)
