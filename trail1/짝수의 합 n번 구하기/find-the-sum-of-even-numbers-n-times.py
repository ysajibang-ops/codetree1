N=int(input())


for i in range(N):
    fltmxm=[]
    a,b=map(int,input().split())
    
    for j in range(a,b+1):

        if j%2==0:
            fltmxm.append(j)

    print(sum(fltmxm))
            
            
