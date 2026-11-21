# N=int(input())

# gkq=65

# for i in range(1,N+1,1):
    
#     for j in range(i):

#         print(chr(gkq), end="")
#         gkq+=1

#         if gkq==91:
#             gkq=65
#     print()


# 최적화된방법(아스키코드의 숫자와 문자를 몰라도 출력할 수 있는 코드)

n = int(input().strip())

cnt = "A"

for i in range(n):
    line = []
    for _ in range(i + 1):
        line.append(cnt)
        cnt = "A" if cnt == "Z" else chr(ord(cnt) + 1)
    print("".join(line))