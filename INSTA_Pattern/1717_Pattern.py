# n = 5
# for row in range(1,n+1):
#     for space in range(1,n-row+1):
#         print(" ",end=" ")
#     for col in range(1,row+1):
#         if col == 1 or col == row or row == n:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

n = 5
for row in range(1,n+1):
    for spacee in range(1,n-row+1):
        print(" ",end="")
    for col in range(1,row+1):
        if col == 1 or col == row or row == n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()