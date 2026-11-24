gkqvudrbs = list(map(int, input().split()))
sub = gkqvudrbs

for i in range(len(gkqvudrbs)):
  if gkqvudrbs[i] >= 250:
    sub = gkqvudrbs[:i]
    break

print(f"{sum(sub)} {sum(sub) / len(sub):.1f}")



# 직관적인 방법
# gkqvudrbs = list(map(int, input().split()))

# total = 0
# cnt = 0

# for x in gkqvudrbs:
#   if x >= 250:
#     break  # 250 이상을 만나면 그 수는 더하지 않고 즉시 종료
#   total += x
#   cnt += 1

# print(f"{total} {total / cnt:.1f}")