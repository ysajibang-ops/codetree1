# N=int(input())

# for i in range(N):
#     for j in range(N-i):
#         for x in range(N-i):
#             print("*", end="")
#         print(" ", end="")
#     print()

N=int(input())

for i in range(N):
    for j in range(N-i):
        for x in range(N-i):
            print("*", end="")
        print(" ", end="")
    print()