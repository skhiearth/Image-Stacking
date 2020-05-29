from statistics import mean, median

def list_stats(list):
    return median(list), mean(list)

if __name__ == '__main__':
  m = list_stats([1.3, 2.4, 20.6, 0.95, 3.1, 5.5])
  print(m)