N=int(input())

cnt=1

for i in range(N):

    for j in range(N):

        print(2*cnt, end=" ")

        if cnt==4:
            cnt=1
        else:
            cnt+=1

        
    
    print()