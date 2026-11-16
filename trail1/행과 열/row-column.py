# A, B= map(int,input().split())\

# for i in range(1,A+1):
    
#     for j in range(1,B+1):
#         print(i*j, end=" ")
#     print()


A, B= map(int, input().split())

for i in range(1,A+1):

    for j in range(1,B+1):

        print(f"{i*j}", end=" ")
    print()



# 다른 아이디어
# a, b = map(int, input().split())

# for row in range(1, a+1):
#     num = row
#     for col in range(b):
        
#         print(row, end=' ')
#         row += num
#     print()
