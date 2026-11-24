wjdtn=list(map(int, input().split()))

fltmxm=[]

for i in wjdtn:

    if i==0:
        break
    else:
        fltmxm.append(i)

aver=sum(fltmxm)/len(fltmxm)
print(sum(fltmxm),aver)        