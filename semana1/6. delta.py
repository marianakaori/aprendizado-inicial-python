a = int(input())
b = int(input())
c = int(input())

delta = b**2 - 4*a*c

if(delta > 0):
    print(2)
elif(delta == 0):
    print(1)
else:
    print(0)