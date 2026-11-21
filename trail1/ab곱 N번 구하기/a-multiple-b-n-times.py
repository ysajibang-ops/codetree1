N=int(input())


for i in range(N):
    a, b= map(int, input().split())
    rhq=1
    
    for j in range(a,b+1):
        rhq=j*rhq
    print(rhq)