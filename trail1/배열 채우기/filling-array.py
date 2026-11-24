wjdtn=list(map(int, input().split()))

fltmxm=[]

for i in wjdtn:

    if i==0:
        break
        

    else:
        fltmxm.append(i)

fltmxm.reverse()

for i in fltmxm:
    print(i, end=" ")

# 간결한버전
# wjdtn = list(map(int, input().split()))
# fltmxm = []

# for i in wjdtn:
#   if i == 0:
#     break
#   fltmxm.append(i)

# fltmxm.reverse()
# for i in fltmxm:
#   print(i, end=" ")


