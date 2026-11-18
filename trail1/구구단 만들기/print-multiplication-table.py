# 내가 시도해본 방법
# A, B= map(int, input().split())

# gkq=[]


# for i in range(1,10):

#     for j in range(1,10):

#         if A<= i <= B and i%2==0:
#             gkq.append(i)
#             gkq.reverse()
            
#             for x in gkq:
#                 print(f"{x} * {i} = {x*i}", end="/")
#     print()




A, B= map(int, input().split())



for i in range(1,10):
    list_rhq=[]

    for j in range(B,A-1,-1):

        if j%2==0:
            list_rhq.append(f"{j} * {i} = {i * j}")
    
    print(" / ".join(list_rhq))


