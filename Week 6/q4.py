##Define two-dimensional array with values {(5,4),(6,3)}. Output eigen values and
##eigenvectors of the matrix.

from scipy import linalg
import numpy as np
arr = np.array([[5,4],[6,3]])

eig_val, eig_vect = linalg.eig(arr)

print("Eigen Values : ",eig_val)
print("Eigen Vectors : \n",eig_vect)