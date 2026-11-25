#인덱스값으로 계산할것
wjdtn=list(map(int, input().split()))
gkq=[]
aver=[]
rotn=0
for i in range(len(wjdtn)):
    
    order=i+1

    if order%2==0:
        gkq.append(wjdtn[i])

for j in range(len(wjdtn)):
    order1=j+1

    if order1%3==0:
        aver.append(wjdtn[j])
        rotn+=1

gkq1=sum(gkq)
aver1=sum(aver)/len(aver)

print(f"{gkq1} {aver1:.1f}")


# wjdtn = list(map(int, input().split()))

# gkq = []
# aver = []
# rotn = 0

# for idx in range(len(wjdtn)):
#     # 1번째부터 세는 순서
#     order = idx + 1

#     # 1. 짝수 번째로 입력된 값
#     if order % 2 == 0:
#         gkq.append(wjdtn[idx])

#     # 2. 3의 배수 번째로 입력된 값 (6번째처럼 둘 다 해당할 수 있으므로 별도 if 사용)
#     if order % 3 == 0:
#         aver.append(wjdtn[idx])
#         rotn += 1

# gkq1 = sum(gkq)
# aver1 = sum(aver) / rotn

# print(f"{gkq1} {aver1:.1f}")