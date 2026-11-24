N=int(input())

N_score=list(map(float, input().split()))

print(f"{sum(N_score)/N:.1f}")

if sum(N_score)/N > 4.0:
    print("Perfect")

elif sum(N_score)/N >= 3.0:
    print("Good")

else:
    print("Poor")