coord = int(input())
our_way = coord // 5
if coord % 5 != 0:
    our_way += 1
print(our_way)

