"""
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1
"""



n = 5
for row in range(1,n*2):
    if row <= n:
        for col in range(1,row+1):
            print(col,end=" ")
    else:
        for col in range(1,2*n-row+1):
            print(col,end=" ")
    print()