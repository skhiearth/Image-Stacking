from statistics import mean

def calculate_mean(list):
  return(mean(list))

if __name__ == '__main__':
  mean = calculate_mean([1,2.2,0.3,3.4,7.9])
  print(mean)
  