"""
A 
B B 
C C C
D D D D
E E E E E
"""
n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(i+64),end=" ")
    print()

"""


A 
A B 
A B C 
A B C D 
A B C D E 
"""

n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(j+64),end=" ")
    print()