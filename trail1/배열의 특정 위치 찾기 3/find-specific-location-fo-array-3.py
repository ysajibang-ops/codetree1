wjdtn=list(map(int, input().split()))

fltmxm=[]

for i in wjdtn:

    if i==0:
        fltmxm.append(i)
        break

    else:
        fltmxm.append(i)

print(fltmxm[-2]+fltmxm[-3]+fltmxm[-4])