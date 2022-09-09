g1_1 = int(input())
g2_1 = int(input())
g1_2 = int(input())
g2_2 = int(input())

if((g1_1 + g1_2) == (g2_1 + g2_2)):
    print("empate")
else:
    print(max([g1_1, g1_2, g2_1, g2_2]))