import numpy as np

n = 3
m = 3
matrix = [[input() for i in range(n)] for j in range(m)]
print(matrix)
transpose = np.transpose(matrix)
print(transpose)
