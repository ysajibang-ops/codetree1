M=int(input())

for i in range(1,M+1):
    N=int(input())
    rotn=0

    while N!=1:
        if N%2==0:
            N=N//2
            rotn+=1

        elif N%2==1:
            N=3*N+1
            rotn+=1
    print(rotn)




