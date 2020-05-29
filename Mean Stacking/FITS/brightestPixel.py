from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np

def load_fits(filename):
  hdulist = fits.open(filename)
  data = hdulist[0].data

  arg_max = np.argmax(data)  
  max_pos = np.unravel_index(arg_max, data.shape)
  
  return max_pos

if __name__ == '__main__':
  bright = load_fits('Mean Exercises/FITS/images/image1.fits')
  print(bright)

  # Visual Verification
  hdulist = fits.open('Mean Exercises/FITS/images/image1.fits')
  data = hdulist[0].data

  plt.imshow(data.T)
  plt.colorbar()
  plt.show()
