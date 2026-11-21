N=int(input())

gkq=65

for i in range(1,N+1,1):
    
    for j in range(i):

        print(chr(gkq), end="")
        gkq+=1

        if gkq==91:
            gkq=65
    print()