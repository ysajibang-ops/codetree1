# N = int(input())

# for i in range(N):
#     # 1. 왼쪽 별 출력 (N-i 개)
#     for j in range(N - i):
#         print("*", end="")
    
#     # 2. 가운데 공백 출력 (2*i 개)
#     for j in range(2 * i):
#         print(" ", end="")
    
#     # 3. 오른쪽 별 출력 (N-i 개)
#     for j in range(N - i):
#         print("*", end="")
    
#     # 한 줄 출력이 끝났으므로 줄바꿈
#     print()



N= int(input())

for i in range(N):
    
    for j in range(N-i):
        print("*", end="")

    for x in range(2*i):
        print(" ", end="")

    for j in range(N-i):
        print("*", end="")
    print()
    