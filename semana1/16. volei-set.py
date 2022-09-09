time_a = int(input())
time_b = int(input())

menor = time_a
if(time_b < time_a):
    menor = time_b
    
if(menor >= 24):
    print('N')
else:
    print('S')