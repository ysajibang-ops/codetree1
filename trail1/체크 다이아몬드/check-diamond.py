# N=int(input())

# for i in range(N):

#     for j in range(N-i-1):
#         print(" ", end="")

#     for j in range(i+1):
#         print("*", end=" ")
#     print()

# for i in range(N-1):

#     for j in range(i+1):
#         print(" ", end="")

#     for j in range(N-i-1):
#         print("*", end=" ")
#     print()

N=int(input())

for i in range(N):

    for j in range(N-1-i):
        print(" ", end="")

    for j in range(i+1):
        print("*", end=" ")
    print()

for x in range(N-1):
    for y in range(x+1):
        print(" ", end="")


    for y in range(N-1-x):
        print("*", end=" ")
    print()