a=[4,12,7,5,24,3,11,26,10] 
print(sum(a))

i = 0
if (a[i] % 2 == 0): prod = 1
else: prod = a[i]
while i < len(a):
  if not a[i] % 2 == 0:
    prod = prod * a[i]
  i += 1
print(prod)
