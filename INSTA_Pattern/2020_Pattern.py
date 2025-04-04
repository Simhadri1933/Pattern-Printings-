n= 5
for i in range(1,n+1):
    for space in range(1,n-i+1):
        print(" ",end=" ")
    for col in range(1,i+1):
        print(col,end=" ")
    for col in range(i-1,0,-1):
        print(col,end=" ")
    print()
"""
        1 
      1 2 1
    1 2 3 2 1
  1 2 3 4 3 2 1
1 2 3 4 5 4 3 2 1
"""

n = 5
for i in range(1, n+1):
    for space in range(1, n-i+1):
        print(" ", end=" ")
    for col in range(1, i+1):
        print(col, end=" ")
    for col in range(i-1, 0, -1):
        print(col, end=" ")
    print()

# Nivas answer
n=5
for i in range(1,n+1):
    for s in range(1,n-i+1):
        print(' ',end=' ')
    for j in range(1,i):
        print(j,end=' ')
    for j in range(i,0,-1):
        print(j,end=' ')
    print()