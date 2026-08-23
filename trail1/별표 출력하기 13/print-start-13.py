N=int(input())

cnt=1
sep=0

for i in range(1,2*N+1):
    
    if i%2==0:
        for j in range(cnt):
            print("*", end=" ")
        print()
        cnt+=1
    else:
        for j in range(N-sep):
            print("*", end=" ")
        print()
        sep+=1