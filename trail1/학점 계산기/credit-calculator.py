N=int(input())
N_score=list(map(float, input().split()))

aver=sum(N_score)/N

print(f"{aver:.1f}")

if aver >= 4.0:
    print("Perfect")

elif aver >= 3.0:
    print("Good")

else:
    print("Poor")