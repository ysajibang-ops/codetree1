# N=int(input())

# for i in range(N):

#     for j in range(i):
#         print(" ", end=" ")
    
#     for j in range((2*N)-(2*i)-1):
#         print("*", end=" ")
#     print()


# for x in range(N-1):

#     for j in range(N-x-2):
#         print(" ", end=" ")

#     for j in range(2*x+3):
#         print("*", end=" ")
#     print()



N=int(input())

for i in range(N):
    
    for j in range(i):
        print(" ", end=" ")

    for j in range(2*(N-i)-1):
        print("*", end=" ")
    print()

for x in range(N-1):

    for y in range(N-x-2):
        print(" ", end=" ")

    for y in range(2*x+3):
        print("*", end=" ")
    print()