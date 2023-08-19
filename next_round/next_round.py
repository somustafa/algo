n, k = [int(i) for i in input().split(' ')]
scores = [int(i) for i in input().split(' ')]
k -= 1
count = 0
for i in range(n):
    if (scores[i] < scores[k] or scores[i] == 0):
        break
    count += 1
print(count)