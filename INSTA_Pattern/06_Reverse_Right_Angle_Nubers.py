"""
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 
"""
n = 5
for row in range(n,0,-1):
    for col in range(1,row+1):
        print(col,end=" ")
    print()
"""
just exchange the row or colum in print fuction can change the direction of the itreation"""

"""
5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1 
"""
n = 5
for row in range(n,0,-1):
    for col in range(1,row+1):
        print(row,end=" ")
    print()