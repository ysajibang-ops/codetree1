start, end = map(int, input().split())

dhkswjstn=0
for i in range(start, end+1):
    fltmxm=[]

    for j in range(1,i):

        if i%j==0:
            fltmxm.append(j)

    if i>1 and sum(fltmxm)==i:
        dhkswjstn+=1


print(dhkswjstn)

    


        
