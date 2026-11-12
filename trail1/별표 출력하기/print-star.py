# N=int(input())

# for i in range(N):
#     for j in range(i+1):
#         print("*", end=" ")
#     print()

# for x in range(N-1,0,-1):
#     for y in range(x):
#         print("*", end=" ")
#     print()



# N = int(input())

# # 총 줄 수는 2*N - 1 줄입니다.
# for i in range(1, 2 * N):
#   # N을 기준으로 위쪽은 증가, 아래쪽은 감소하도록 별의 개수(k)를 계산
#   k = 2 * N - i if i > N else i

#   for j in range(k):
#     print('*', end=' ')
#   print()




N= int(input())

for i in range(N):
    for j in range(i+1):
        print("*", end=" ")
    print()
    
for x in range(N-1,0,-1):
    for y in range(x):
        print("*", end=" ")
    print()
