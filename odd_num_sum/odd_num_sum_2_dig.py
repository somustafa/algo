n = 100

i = 10
accum = 0
while i < n:
  if not i % 2 == 0:
    accum += i
  i += 1
print(accum)
