"""
        1 
      2 2 2 
    3 3 3 3 3 
  4 4 4 4 4 4 4 
5 5 5 5 5 5 5 5 5 
"""
1
n = 5
for row in range(1,n+1):
    for space in range(1,n-row+1):
        print(" ",end=" ")
    for col in range(1,2*row):
        print(row,end=" ")
    print()



"""
        1 
      1 2 3 
    1 2 3 4 5 
  1 2 3 4 5 6 7 
1 2 3 4 5 6 7 8 9"""

#2
n = 5
for row in range(1,n+1):
    for space in range(1,n-row+1):
        print(" ",end=" ")
    for col in range(1,2*row):
        print(col,end=" ")
    print()



"""
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * *
"""
n = 5
for row in range(1,n+1):
    for space in range(1,n-row+1):
        print(" ",end=" ")
    for col in range(1,2*row):
        print("*",end=" ")
    print()