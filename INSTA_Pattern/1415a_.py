"""
        * 
      * * 
    * * * 
  * * * * 
* * * * * 
* * * * 
* * * 
* * 
* 
"""

n = 5
for rows in range(1,n*2):
    for spac in range(1,n-rows+1):
        print(" ",end=" ")
    if rows <= n:
        for col in range(1,rows+1):
            print("*",end=" ")
    else:
        for space in range(1,n-rows+1):
            print(" ",end=" ")
        for col in range(1,2*n-rows+1):print("*",end=" ")
    print()