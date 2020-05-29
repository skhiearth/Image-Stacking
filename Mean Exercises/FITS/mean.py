from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt

def mean_fits(files):
    n = len(files)

    if n > 0:
        hdulist = fits.open(files[0])
        data = hdulist[0].data
        hdulist.close()
        
        for i in range(1, n):
            hdulist = fits.open(files[i])
            data += hdulist[0].data
            hdulist.close()
        
        mean = data / n
        return mean

if __name__ == '__main__':
    root = 'Mean Exercises/FITS/images/'
    data = mean_fits([root + 'image0.fits', root + 'image1.fits', root + 'image2.fits'])
    print(data[100, 100])

    plt.imshow(data.T)
    plt.colorbar()
    plt.show()