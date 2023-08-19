n, k = [int(i) for i in input().split(' ')]
scores = [int(i) for i in input().split(' ')]
i = 0
k -= 1
while i < n and scores[i] >= scores[k] and scores[i] > 0:
    i += 1
print(i)