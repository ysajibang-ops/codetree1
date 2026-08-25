N=int(input())

cnt=1

for i in range(1,N+1):

    for j in range(1,N+1):
        print(i, end="")
    print()

# 더 간단한 방법
# N = int(input())

# for i in range(1, N+1):
#     print(str(i) * N)