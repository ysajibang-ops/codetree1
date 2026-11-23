start, end = map(int, input().split())

wjdekq=0

for i in range(start, end+1):
    fltmxm=[]

    for j in range(1,i+1):

        if i%j==0:
            fltmxm.append(j)

    if len(fltmxm)==3:
            wjdekq+=1

print(wjdekq)

            