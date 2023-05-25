import numpy as np
import matplotlib.pyplot as plt

def linear_coefficient(sum_x, sum_y, n, xy, xx):
  return (np.sum(xy) - ((sum_x*sum_y)/n)) / (np.sum(xx) - ((sum_x**2)/n))

def angular_coefficient(mean_y, linear_coefficient, mean_x):
  return  mean_y - (linear_coefficient * mean_x)

def liner_equation(point):

  n = point.size
  
  xy = np.multiply(point[0],point[1])

  xx = np.multiply(point[0],point[0])

  mean_x = np.mean(point[0])
  mean_y = np.mean(point[1])

  a = linear_coefficient(sum(point[0]), sum(point[1]), n, xy, xx)
  b = angular_coefficient(mean_y, a, mean_x)

  return a, b

def main():
  
  point_x= np.array([2.4,5.0,1.5,3.8,8.7,3.6,1.2,8.1,2.5,5,1.6,1.6,2.4,3.9,5.4])
  point_y = np.array([2.1,4.7,1.7,3.6,8.7,3.2,1.0,8.0,2.4,6,1.1,1.3,2.4,3.9,4.8])
  
  #format [[x1,x2,x3,...,xn][y1,y2,y3,...,yn]]
  point = np.vstack((point_x, point_y))
  
  # a = linear coefficient, b = angular coefficient 
  a, b = liner_equation(point)

  fig = plt.figure(figsize=(16, 9))

  x = np.linspace(np.min(point_x), np.max(point_x), 100)
  
  y = a*x+b

  plt.title('Linear Regression')
  plt.plot(point_x, point_y, 'ob', label='(xi, yi)')
  plt.plot(x, y, '-r', label=f'{a:.2f}x+{b:.2f}')
  plt.legend()
  plt.show()

if __name__ == '__main__':
  main()