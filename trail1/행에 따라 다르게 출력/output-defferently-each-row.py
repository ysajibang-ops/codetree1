# 내 풀이

N=int(input())

cnt=0

for i in range(N):

    for j in range(N):

        if i%2==0:
            print(cnt+1, end=" ")
            cnt+=1

        else:
            print(cnt+2, end=" ")
            cnt+=2
    print()




# 정석
# N = int(input())
# cnt = 0

# # 1번째 줄부터 N번째 줄까지 직접 세기
# for i in range(1, N + 1):
#     for j in range(N):
#         # 지문 그대로: 홀수 번째 줄이면 1씩 증가
#         if i % 2 == 1:
#             cnt += 1
#             print(cnt, end=" ")
#         # 지문 그대로: 짝수 번째 줄이면 2씩 증가
#         else:
#             cnt += 2
#             print(cnt, end=" ")
#     print()