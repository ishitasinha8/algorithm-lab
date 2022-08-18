import time
import random

def strassen(A,B,C):
    p1 = (A[0][0]+A[1][1])*(B[0][0]+B[1][1])
    p2 = B[0][0]*(A[1][0]+A[1][1])
    p3 = A[0][0]*(B[0][1]-B[1][1])
    p4 = A[1][1]*(B[1][0]-B[0][0])
    p5 = B[1][1]*(A[0][0]+A[0][1])
    p6 = (B[0][0]+B[0][1])*(A[1][0]-A[0][0])
    p7 = (B[1][0]+B[1][1])*(A[0][1]-A[1][1])

    C[0][0] = p1+p4-p5+p7
    C[0][1] = p3+p5
    C[1][0] = p2+p4
    C[1][1] = p1+p3-p2+p6

def trivial(A,B,D):
    for i in range(2):
        for j in range(2):
            for k in range(2):
                D[i][j] = D[i][j] + A[i][k]*B[k][j]

A = [[random.randrange(1,10) for i in range(2)],[random.randrange(1,10) for i in range(2)]]
B = [[random.randrange(1,10) for i in range(2)],[random.randrange(1,10) for i in range(2)]]
C = [[0,0],[0,0]]
D = [[0,0],[0,0]]

print("Matrix 1 = ",A)
print("Matrix 2 = ",B)

start = time.time()
trivial(A,B,D)
end = time.time()
print("Multiplying using trivial method: ",D)
print("Time = ",end-start)

start = time.time()
strassen(A,B,C)
end = time.time()
print("Multiplying using Strassen's method: ",C)
print("Time = ",end-start)

