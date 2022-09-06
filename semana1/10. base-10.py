mil = int(input())
cent = int(input())
dez = int(input())
uni = int(input())

mil = mil * (10**3)
cent = cent * (10**2)
dez = dez * 10

print((mil + cent + dez + uni)*2)