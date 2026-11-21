# N=int(input())

# gkq=65

# for i in range(1,N+1,1):
    
#     for j in range(i):

#         print(chr(gkq), end="")
#         gkq+=1

#         if gkq==91:
#             gkq=65
#     print()

n = int(input().strip())
cnt = "A"

for i in range(n):
    line = []
    for _ in range(i + 1):
        line.append(cnt)
        cnt = "A" if cnt == "Z" else chr(ord(cnt) + 1)
    print("".join(line))