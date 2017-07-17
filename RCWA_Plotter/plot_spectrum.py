from matplotlib import pyplot as plt
import os
import glob
import sys


def get_spectrum(filename):
    with open(filename) as f:
        lines = f.readlines()
        strings = [x.strip() for x in lines]
        spectrum = list(filter(None, strings))
        float_spectrum = [float(x) for x in spectrum]
    return float_spectrum


def get_wavelength(filename):
    file_only = filename.split('/')[-1]
    spec_x = file_only.split('.')[0]
    return spec_x[4:]

def get_rcwa_data(directory):
    file_list = glob.glob(os.path.join(directory, '*.txt'))
    for file in file_list:
        if 'freq' in file:
            frequency_filename = file
            file_list.remove(file)
            print("File: " + str(file))
    frequency_filename = directory + '/freq.txt'

    spectra = [get_spectrum(filename) for filename in file_list]

    frequency = get_spectrum(frequency_filename)

    legend_labels = [get_wavelength(filename) for filename in file_list]

    return spectra,frequency,legend_labels


plt.show()

if __name__ == '__main__':
    directory = './Spectra'
    graph_name = sys.argv[1]
    #print(graph_name)
    test_directory = '/Users/st659/Documents/RCWA'


    spectra,frequency,legend_labels = get_rcwa_data(file_list)
    print(legend_labels)


    figure = plt.figure()
    ax = figure.add_subplot(111)
    ax.set_ylabel('Reflectance')
    ax.set_xlabel('$\lambda$ (nm)')


    for spectrum, leg in zip(spectra, legend_labels):
        ax.plot(frequency, spectrum, label=leg)
    ax.legend(loc ='upper left')
    plt.savefig(os.path.join(directory, graph_name), dpi=300)
