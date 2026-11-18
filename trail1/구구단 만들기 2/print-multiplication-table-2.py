A, B=map(int, input().split())


for i in range(2,10,2):
    list_rhq=[]

    if i%2==0:

        for j in range(B,A-1,-1):
            list_rhq.append(f"{j} * {i} = {j*i}")
        
    print(" / ".join(list_rhq))
        



# 리스트를 안쓰고 푼 풀이
# A, B = map(int, input().split())

# for i in range(2, 9, 2):
#     for j in range(B, A - 1, -1):
#         print(f"{j} * {i} = {j * i}", end="")
# "만약 현재 단(i)이 마지막 단(A)이 아니라면, 뒤에 ' / '를 붙여줘라"
#         if j != A:
#             print(" / ", end="")

#     print()
