import numpy as np

def multiply_matrices(a, b):
  
  if a.shape[1] != b.shape[0]:
    print('it is not possible to multiply matrices of different shape')
    return None
  
  c = np.zeros((a.shape[0], b.shape[1]), dtype=int)
  
  for i in range(a.shape[0]):
    sum = 0
    for j in range(b.shape[1]):
      for k in range(a.shape[1]):
        sum += a[i][k] * b[k][j]
      c[i][j] = sum
      sum = 0

  return c

def main():
  a = np.array([[1, 2, 3],
                [4, 5, 6]])
  b = np.array([[7, 8],
                [9, 10],
                [11, 12]])
  
  c = multiply_matrices(a, b)
  if not c is None:
    print(c)

  #numpy
  print(np.matmul(a, b))

if __name__ == '__main__':
  main()