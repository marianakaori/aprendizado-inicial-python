top = input()
bottom = input()
left = input()
right = input()
direcao = input().lower()
rodada = [top, bottom, left, right]
letras_possiveis_tabuleiro = ['T', 'B', 'L', 'R', 'E']
teclado = ['w','s','a','d']
yes = True
if(rodada.count('E') == 1):
    if(teclado[rodada.index('E')] == direcao):
        for i, letra in enumerate(rodada):
            if((letra != letras_possiveis_tabuleiro[i] and letra != 'E') or rodada.count(letra) != 1):
                yes = False
        print('yes!' if yes else "next player...")
    else:
        print("next player...")        
else:
    print("next player...")        
