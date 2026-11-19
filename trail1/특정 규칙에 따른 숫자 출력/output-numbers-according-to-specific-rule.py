# My style

# N= int(input())

# gkq=0

# for i in range(N):

#     for j in range(i):
#         print(" ", end=" ")
    
#     for j in range(N-i,0,-1):

#         print(gkq+1, end=" ")
#         gkq+=1

#         if gkq==9:
#             gkq=0
#     print()

N = int(input())

gkq = 0

for i in range(N):
  for j in range(i):
    print(" ", end=" ")

  for j in range(N - i, 0, -1):
    print((gkq % 9) + 1, end=" ")
    gkq += 1
  print()



