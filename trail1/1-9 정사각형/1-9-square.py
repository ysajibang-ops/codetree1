N=int(input())

cnt=1

for i in range(1,N+1):

    for j in range(1,N+1):
        print(cnt, end="")
        cnt+=1
        if cnt==10:
            cnt=1

    print()

# 다시한번보기
# 나머지 연산자(%) 활용하기 (추천)
# N = int(input())

# cnt = 0

# for i in range(1, N + 1):
#     for j in range(1, N + 1):
#         print((cnt % 9) + 1, end="")
#         cnt += 1
#     print()