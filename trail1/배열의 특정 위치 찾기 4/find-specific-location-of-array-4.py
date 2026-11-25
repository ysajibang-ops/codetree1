wjdtn=list(map(int, input().split()))

rotn=0
fltmxm=[]

for i in wjdtn:

    if i==0:
        break

    elif i%2==0:
        fltmxm.append(i)
        rotn+=1

print(f"{rotn} {sum(fltmxm)}")

        