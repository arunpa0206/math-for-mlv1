import numpy as np
from scipy.sparse import csc_matrix

from scipy.sparse import random

def get_sparse_size(matrix):
    # get size of a sparse matrix
    return int((matrix.data.nbytes + matrix.indptr.nbytes + matrix.indices.nbytes) / 1024.)

# create a sparse matrix, 1000 x 100000
sparse_mat = random(10 ** 3, 10 ** 5, format='csr')

# get size of a sparse matrix
sparse_size = get_sparse_size(sparse_mat)

# convert sparse matrix to a regular matrix and get its size
regular_size = sparse_mat.toarray().nbytes / 1024.
print("The size of sparse matrix is %s KiB" % sparse_size)
print("The size of regular matrix is %s KiB" % regular_size)
print("Data compression ratio is %s" % (regular_size / sparse_size))
