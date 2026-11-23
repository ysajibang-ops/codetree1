N=int(input())

fltmxm=[]

for i in range(1,N+1,1):
    thtn=0

    for j in range(1,i+1):

        if i%j==0:
            thtn+=1
            
    if thtn==2:
        fltmxm.append(i)
        
print(" ".join(map(str, fltmxm)))



# 내 아이디어로 구현한 코드 

# N = int(input())

# fltmxm = []

# for i in range(2, N + 1):
#     rotn = True  # 소수라고 가정하고 시작

#     for j in range(2, i):  # 1과 자기 자신(i) 사이는 제외
#         if i % j == 0:
#             rotn = False  # 하나라도 나눠떨어지면 소수가 아님
#             break

#     if rotn==True:
#         fltmxm.append(i)

# print(" ".join(map(str, fltmxm)))