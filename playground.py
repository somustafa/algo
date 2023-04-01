print("A","B","C",sep=".")
print("\n")

print(10,20,30,40,sep="+\n",end="*")
print("\n")

# B,I,M=10,20,50
# B,I,M=I+M,B+M,B+I
# print(B,I,M)
# print("\n")

B,I,M=10,20,50
B=I+M
I=B+M
M=B+I
print(B,I,M)
print("\n")
# [a-zA-Z_][a-zA-Z_0-9]*

print("S","O","\nN","A",sep="_")
print("\n")

print(1,2,3,4,5,sep="-ci cerge \n")
print("\n")


a,b,c = 12,13,14
a,b = a+b,a+c
b,c = b+a, b+c
print(a,b,c)
print("\n")


a = 3
b = 4
c = 7
b , c = a , b 
a , c = c , b 
b = a 
c = b
a = c 
# c = b 
print(a+b+c)
print("\n")

B,C=30,40
print("30+40")
print("\n")

a,b,c=10,12,13
a=b+c 
z=a+b 
b=a+c 
c=a+z 
z=a+b+c 
print(z)