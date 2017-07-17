from RCWA_Plotter.plot_spectrum import get_rcwa_data
from matplotlib import pyplot as plt
import glob
import os

directory = '/Users/st659/Documents/RCWA/FOx_Grating/ITO/ITOOnly'
plt.style.use(['seaborn-white', 'seaborn-notebook'])

frequency_filename = directory + '/freq.txt'
#file_list = glob.glob(os.path.join(directory, '*.txt'))

spectra, frequency, default_labels = get_rcwa_data(directory)

figure = plt.figure()
ax = figure.add_subplot(111)
ax.set_ylabel('Reflectance')
ax.set_xlabel('$\lambda$ (nm)')



for spectrum, leg in zip(spectra, default_labels):
    ax.plot(frequency, spectrum, label=leg)
ax.legend(loc ='upper left')
#plt.savefig(os.path.join(directory, graph_name), dpi=300)
plt.show()