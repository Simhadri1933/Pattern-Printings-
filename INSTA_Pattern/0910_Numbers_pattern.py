""""
1 1 1 1 1 
  2 2 2 2 
    3 3 3 
      4 4 
        5
"""

n = 5
for row in range(1,n+1):
    for space in range(1,row):
        print(" ",end=" ")
    for col in range(1,n-row+2):
        print(row,end=" ")
    print()



# 10th pattern
"""
1 2 3 4 5 
  1 2 3 4 
    1 2 3 
      1 2 
        1 
"""

n = 5
for row in range(1,n+1):
    for space in range(1,row):
        print(" ",end=" ")
    for col in range(1,n-row+2):
        print(col,end=" ")
    print()