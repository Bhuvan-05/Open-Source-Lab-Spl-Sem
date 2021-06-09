#Create two matrices with 2x2 dimensions. Initialize them with values [4,5], [3,2]. Calculate
#determinant of a two-dimensional matrix using scipy.linalg. Calculate the inverse of a matrix
#in 3.

from scipy import linalg
import numpy as np
matrix = np.array([ [4,5], [3,2] ])
print("matrix : \n",matrix)
print("determinant : ",linalg.det(matrix))
print("inverse matrix : \n",linalg.inv(matrix))