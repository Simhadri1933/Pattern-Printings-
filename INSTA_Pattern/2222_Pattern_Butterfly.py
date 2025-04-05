# # n = 5
# # tc = 2*n -1
# # for i in range(1,n+1):
# #     for j in range(1,tc+1):
# #         if j <= i or j > tc-i:
# #             print("*",end=" ")
# #         else:
# #             print(" ",end=" ")
# #     print()
# # for i in range(1,n+1):
# #     for j in range(1,tc+1):
# #         if j <= n-i or j >= n+i:
# #             print("*",end=" ")
# #         else:
# #             print(" ",end=" ")
# #     print()
# """
#   1 2 3 4 5 6 7 8 9
# 1 *               *
# 2 * *           * *
# 3 * * *       * * *
# 4 * * * *   * * * *
# 5 * * * * * * * * *
# 6 * * * *   * * * *
# 7 * * *       * * *
# 8 * *           * *
# 9 *               *
# """


# # Practice


# n = 5
# TC = 2*n-1
# for i in range(1,n+1):
#     for j in range(1,TC+1):
#         if j <= i or j > TC-i:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# for i in range(1,n):
#     for j in range(1,TC+1):
#         if j <=n-i or j >=n+i or j==n:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()



# 2nd practice

n =5
totalcolumn = 2*n-1
for i in range(1,n+1):
    for j in range(1,totalcolumn+1):
        if j <=i or j>totalcolumn-i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
for i in range(1,n):
    for j in range(1,totalcolumn+1):
        if j <=n-i or j >= n+i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()









