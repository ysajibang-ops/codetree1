N=int(input())

num=1

for i in range(N):
    row=[]
    for j in range(N):
        row.append(num)
        num+=1
    if i%2==1:
        row.reverse()
    print(*row)

            