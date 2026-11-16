N=int(input())

for i in range(1,2*N+1):

    if i%2==0:
        for j in range(N - (i // 2 - 1)):
            print("*", end=" ")
        print()

    else:
        for j in range((i + 1) // 2):
            print("*", end=" ")
        print()



# N=int(input())

# for i in range(2*N):
    
#     if i%2!=0:
#         for j in range(N-(i-1)//2):
#             print("*", end=" ")
#         print()
#     elif i%2==0:
#         for j in range(1+(i//2)):
#             print("*", end=" ")
#         print()