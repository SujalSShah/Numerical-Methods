# Finding inverse using Partition Method

# Matrix A
A = [
    [3, 2, 1],
    [2, 3, 2],
    [1, 2, 3]
]

n = 3

# Add Identity Matrix to A
for i in range(n):
    A[i] = A[i] + [1 if i == j else 0 for j in range(n)]

# Gauss-Jordan operations
for i in range(n):

    # Make diagonal element 1
    pivot = A[i][i]

    for j in range(2 * n):
        A[i][j] = A[i][j] / pivot

    # Make other elements in this column zero
    for k in range(n):
        if k != i:
            factor = A[k][i]

            for j in range(2 * n):
                A[k][j] = A[k][j] - factor * A[i][j]

# Display inverse
print("Inverse of the matrix is:")

for i in range(n):
    for j in range(n, 2 * n):
        print(round(A[i][j], 3), end=" ")
    print()
