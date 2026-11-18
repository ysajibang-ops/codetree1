N= int(input())

for i in range(N):
    
    for j in range(N):
        if j%2==0:
            print(i+1, end="")
        else:
            print(N-i, end="")
    print()



# 짝수 홀수 판정할 때 i 대신 j로 하면 안되는 이유:
# N= int(input())

# for i in range(N):
    
#     for j in range(N):
#         if j%2==0:
#             print(j+1, end="")
#         else:
#             print(N-j, end="")
#     print()

# 1331
# 1331
# 1331
# 1331
    