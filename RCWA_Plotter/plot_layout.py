filename = '/Users/st659/Documents/RCWA/FOx_grating/SiN/SiNGold/layout.txt'
from matplotlib import pyplot as plt
import numpy as np

figure = plt.figure()
ax = figure.add_subplot(111)

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

with open(filename) as f:
    lines = f.readlines()
    strings = [x.strip() for x in lines]
    epsi= list(filter(None, strings))

    floats = [float(x) for x in epsi]
    epsilon = list(chunks(floats, 100))




# x = range(0,10,0.1)
# y = range(0,10,0.1)
#
# x=np.unique(x)
# y=np.unique(y)
#
# #epsilon = np.asarray(floats)
#
# X,Y = np.meshgrid(x,y)
#
# print(X)
#
# print(epsilon)

#E = epsilon.reshape(len(y), len(x))
print(len(floats))
floats_array = np.reshape(np.array(floats), (500, 10))
print(np.array(floats_array).shape)
mesh = ax.pcolor(floats_array)

plt.colorbar(mesh, ax=ax)
plt.show()
