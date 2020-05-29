import numpy as np

def calc_stats(filename):
  data = np.loadtxt(filename, delimiter=',')
 
  mean = np.mean(data)
  median = np.median(data)

  return np.round(mean, 1), np.round(median, 1)

if __name__ == '__main__':
  mean = calc_stats('Mean Exercises/1D Array/data.csv')
  print(mean)
