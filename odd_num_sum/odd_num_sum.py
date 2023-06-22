n = 50

# O(n), S(1), not that good
i = 0
accum = 0
while i < n:
  if not i % 2 == 0:
    accum += i
  i += 1
print(accum)


# O(n), S(n), slow
nums = list(range(1, n))
print(sum(nums))
