"""
* * * * * 
* * * * 
* * * 
* * 
* 
"""

n = 5
for row in range(1,n+1):
    for cols in range(1,n-row+2):
        print("*",end= " ")
    print()