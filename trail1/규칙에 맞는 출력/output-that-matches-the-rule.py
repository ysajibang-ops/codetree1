N= int(input())

for i in range(N):

    for j in range(i+1):
        print(N-i+j, end=" ")
    print()

# range(시작값, 끝값) 범위 자체를 활용하기
# N = int(input())

# for i in range(N):
#   for j in range(N - i, N + 1):
#     print(j, end=" ")
#   print()