import numpy as np
import numpy.polynomial as p

import matplotlib.pyplot as plt



fig, (ax, ax2) = plt.subplots(1,2)
file = '/Users/st659/Downloads/RefractiveIndexINFO.csv'

wavelength, ref, ex = np.genfromtxt(file, unpack=True,skip_header=1, delimiter=',')
wavelength_nm = [x*1000 for x in wavelength]
ref_coeff = p.Polynomial.fit(wavelength_nm,ref, 12 )
ex_coeff = p.Polynomial.fit(wavelength_nm, ex, 6)
#ref_poly = p.polynomial(ref_coeff)
#ex_poly = p.polynomial(ex_coeff)

ref_x, ref_y = ref_coeff.linspace()
ex_x, ex_y = ex_coeff.linspace()
print(ref_x)

print(ref_coeff)


ax.plot(wavelength_nm,ref, 'o')
ax.plot(ref_x, ref_y)

ax2.plot(wavelength_nm,ex, 'o')
ax2.plot(ex_x, ex_y)
ax.set_xlim([0,1000])
ax.set_ylim([0,2])
plt.show()




