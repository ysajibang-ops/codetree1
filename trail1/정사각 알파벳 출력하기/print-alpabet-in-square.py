N=int(input())

gkq=0

for i in range(N):
    
    for j in range(N):

        print(chr(65+gkq), end="")
        gkq+=1
    print()