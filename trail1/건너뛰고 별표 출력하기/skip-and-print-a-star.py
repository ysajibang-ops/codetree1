# N=int(input())

# for i in range(N):
#     for j in range(i+1):
#         print("*", end="")
        
#     print()
#     print()
# for i in range(N-1):
#     for j in range(N-i-1):
#         print("*", end="")
#     print()
#     print()


N=int(input())

for i in range(N):
    for j in range(i+1):
        print("*", end="")
    print()
    print()

for x in range(N-1):
    for y in range(N-1-x):
        print("*", end="")
    print()
    print()