N=int(input())

cnt="A"

for i in range(N):

    line=[]

    for j in range(i):
        print(" ", end=" ")

    for j in range(N-i):
        line.append(cnt)
        cnt= "A" if cnt=="Z" else chr((ord(cnt)+1))
    print(" ".join(line))