wjdtn=list(map(int, input().split()))

fltmxm=[]

for i in wjdtn:

    if i==0:
        break
    else:
        fltmxm.append(i)

gkq=sum(fltmxm)
aver=sum(fltmxm)/len(fltmxm)
print(f"{gkq} {aver:.1f}")        