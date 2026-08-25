N= int(input())

for i in range(N):

    for j in range(N):
        print(f"({N-i},{N-j})",end=" ")
    print()



# 다른아이디어
# n= int(input())

# for i in range(n,0,-1):
#     for j in range(n,0,-1):
#         print(f'({i},{j})', end=' ')
#     print()
