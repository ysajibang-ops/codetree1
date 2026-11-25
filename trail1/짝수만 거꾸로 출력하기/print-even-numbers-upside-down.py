N=int(input())
wjdtn=list(map(int,input().split()))
fltmxm=[]
for i in wjdtn:

    if i%2==0:
        fltmxm.append(i)
    
    else:
        pass
fltmxm.reverse()

for j in fltmxm:
    print(j, end=" ")