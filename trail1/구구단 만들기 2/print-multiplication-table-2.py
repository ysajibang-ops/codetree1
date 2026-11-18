A, B=map(int, input().split())


for i in range(2,10,2):
    list_rhq=[]

    if i%2==0:

        for j in range(B,A-1,-1):
            list_rhq.append(f"{j} * {i} = {j*i}")
        
    print(" / ".join(list_rhq))
        