N=int(input())

xhdrhk=0

for i in range(N):
    student=list(map(int, input().split()))
    aver=sum(student)/len(student)

    if aver>=60:
        print("pass")
        xhdrhk+=1

    else:
        print("fail")

print(xhdrhk)