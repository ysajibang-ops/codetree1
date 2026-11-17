# N=int(input())

# cnt=1

# for i in range(N):

#     for j in range(N):

#         print(10-cnt, end="")

#         if cnt==9:
#             cnt=1
#         else:
#             cnt+=1

        
#     print()

N= int(input())

cnt=9

for i in range(N):
    
    for j in range(N):

        print(cnt, end="")
        cnt-=1

        if cnt==0:
            cnt=9


    print()
