##Create Sparse matrices A and B and analyze various functions of sciPy sparse package

import numpy as np
from scipy import sparse

A = sparse.identity(3,dtype='int8',format='array')      
B = sparse.eye(4,4,1,dtype='int8',)       
C = sparse.random(4,4,.1,format ="array",dtype="int8")  
print(A, "\n")
print(B, "\n")

print(sparse.isspmatrix_csr(B))
B = B.tocsr()

print(C, "\n")

print(sparse.find(C))
print(sparse.issparse(B))