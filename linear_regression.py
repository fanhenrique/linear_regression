import numpy as np
import matplotlib.pyplot as plt

def liner_equation(point):

  n = point.size
  
  xy = np.multiply(point[0],point[1])

  xx = np.multiply(point[0],point[0])

  mean_x = point[0].mean()
  mean_y = point[1].mean()

  a = (np.sum(xy) - ((sum(point[0])*sum(point[1]))/n)) / (sum(xx) - ((sum(point[0])**2)/n))

  b = mean_y - (a * mean_x)

  return a, b

def main():
  
  point_x = np.array([2,3,5,6,8,7,7,9,8,10])
  point_y = np.array([2,4,6,5,6,7,8,8,9,10])

  point = np.vstack((point_x, point_y))
  
  a, b = liner_equation(point)

  fig = plt.figure(figsize=(16, 9))

  x = np.linspace(min(point_x), max(point_y), 100)
  
  y = a*x+b

  plt.plot(point_x, point_y, 'ob')
  plt.plot(x, y, '-r')

  plt.show()

if __name__ == '__main__':
  main()