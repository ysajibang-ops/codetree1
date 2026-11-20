N= int(input())

gkq=0

for i in range(1,N+1,1):
    

    for j in range(1,N+1,1):
        
        
        if j==N-gkq:
            print(f"{i} * {j} = {i*j}", end="\n")
            gkq+=1
            break

        else:
            print(f"{i} * {j} = {i*j}", end=" / ")
