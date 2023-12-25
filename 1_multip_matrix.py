import numpy as np

def brute_force(A, B):
    n, m, p = A.shape[0], A.shape[1], B.shape[1]
    print (n, m, p)
    C = np.array([[0]*p for i in range(n)])
    for i in range(n): 
        for j in range(p): 
            for k in range(m): 
                C[i][j] += A[i][k]*B[k][j]
    return C

A = np.array([
    [1, 2, 5, 4],
    [2, 2, 0, 4],
    [3, 1, 1, 5],
    [2, 2, 2, 4]
])

B = np.array([
    [0, 1, 3],
    [1, 1, 1],
    [4, 2, 3],
    [3, 2, 4]
])

# print ()

print(brute_force(A, B))


