# N=int(input())

# for i in range(N):
#     for j in range(i+1):
#         print("*", end=" ")
#     print()

N=int(input())

for i in range(N):
    for j in range(1+i):
        print("*", end=" ")
    print()