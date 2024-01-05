import numpy as np

x = np.array([2,3,5,6,8,7,7,9,8,10])
y = np.array([2,4,6,5,6,7,8,8,9,10])

n = x.size

xy = np.multiply(x,y)

xx = np.multiply(x,x)

mean_x = x.mean()
mean_y = y.mean()


a = (np.sum(xy) - ((sum(x)*sum(y))/n)) / (sum(xx) - ((sum(x)**2)/n))

b = mean_y - (a * mean_x)

print(f'y={a}x+{b}')