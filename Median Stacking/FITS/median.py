import sys
import time
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits

def median_fits(fitsArray):
    pixelsArray = []
   
    start = time.perf_counter()
  
    for fitsFile in fitsArray:
        hdulist = fits.open(fitsFile)
        pixelsArray.append(hdulist[0].data)
       
    pixelsNumpyArray = np.array(pixelsArray)
    medianMatrix = np.median(pixelsNumpyArray, axis=0)
  
    seconds = time.perf_counter() - start
    memoryUsage = sys.getsizeof(pixelsNumpyArray) / 1024
  
    return (medianMatrix, seconds, memoryUsage)

if __name__ == '__main__':
    result = median_fits(['Median Stacking/FITS/images/image{}.fits'.format(str(i)) for i in range(3)])
    print(result[0][100, 100], result[1], result[2])

    plt.imshow(result[0].T)
    plt.colorbar()
    plt.show()
