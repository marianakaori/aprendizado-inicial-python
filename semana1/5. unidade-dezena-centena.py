a = int(input())

if(0 <= a and a <= 99999):
    print(a%10)
    print(a%100)
    print(a%1000)
    print(a%10000)
else:
    print("valor inválido")