from RCWA_Plotter.plot_spectrum import get_rcwa_data
from matplotlib import pyplot as plt
import glob
import os

directory = '/Users/st659/Documents/RCWA/FOx_Grating/ITO/FinalGraph'
plt.style.use(['seaborn-white', 'seaborn-notebook'])

frequency_filename = directory + '/freq.txt'
#file_list = glob.glob(os.path.join(directory, '*.txt'))

spectra, frequency, default_labels = get_rcwa_data(directory)

figure = plt.figure()
ax = figure.add_subplot(111)
ax.set_ylabel('Reflectance')
ax.set_xlabel('$\lambda$ (nm)')

labels= ['300nm Period ITO', '300nm Period SIN ITO','400nm Period ITO', '400nm Period SIN ITO','500nm Period ITO', '500nm Period SiN ITO']
linestyle = ['-', '--','-', '--','-', '--']
for style,spectrum, leg, in zip(linestyle, spectra, labels, ):
    ax.plot(frequency, spectrum, style, label=leg)
ax.legend(loc ='upper left')
plt.savefig(os.path.join(directory, 'SiN ITO ITO Only Comp'), dpi=300)
plt.show()