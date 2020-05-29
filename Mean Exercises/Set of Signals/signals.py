import numpy as np

def mean_datasets(filenames):
    n = len(filenames)
    if n >= 1:
      data = np.loadtxt(filenames[0], delimiter=',')
      for i in range(1,n):
        data += np.loadtxt(filenames[i], delimiter=',')
    
    data_mean = data/n
     
    return np.round(data_mean, 1)

if __name__ == '__main__':
    root = 'Mean Exercises/Set of Signals/data/'
    print(mean_datasets([root + 'data1.csv', root + 'data2.csv', root + 'data3.csv']))
