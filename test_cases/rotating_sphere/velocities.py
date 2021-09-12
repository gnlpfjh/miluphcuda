import numpy as np
import matplotlib.pyplot as plt
import sys

x,y,z, vx,vy,vz = np.loadtxt("sphere.%04d"%int(sys.argv[1]), unpack=True, usecols=(0,1,2,3,4,5))

plt.quiver(x,y, vx,vy, z)

plt.show()