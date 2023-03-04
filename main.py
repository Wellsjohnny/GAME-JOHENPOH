# Regras de negócios

# tesoura ganha de papel
# tesoura empata com tesoura
# tesoura perde para pedra
# ***************************
# papel ganha de pedra 
# papel empata com papel
# papel perde para tesoura
#****************************
# pedra ganha de tesoura 
# pedra empata com pedra 
# pedra perde para papel
#****************************
from os import system as sys
from time import sleep as slp 
from random import randint
jogar = True
pedra = 1
papel = 2
tesoura = 3
sys('cls')
print('''
            *******************
            *    JO-KEN-POH   *
            *       GAME      *
            *******************

''')
nome = input('Olá, vamos jogar JO-KEN-POH ? Qual o seu nome: ').upper().strip()
sys('cls')
while jogar:
    print('''
                    ESCOLHA UMA DAS OPÇÕES:

                        *****************
                        *  [1] PEDRA    *
                        *  [2] PAPEL    *
                        *  [3] TESOURA  *
                        *****************
    ''')
    jogador = int(input('Qual é a sua jogada ? '))
    sys('cls')
    print('JO...')
    slp(1)
    print('KEN...')
    slp(1)
    print('POHHHHHHH!!!')
    slp(2)
    sys('cls')
    pc = randint(1,3)

    if jogador == 1 and pc == 3:
        print(f'{nome} jogou: {jogador} (PEDRA)')
        print(f'COMPUTADOR jogou: {pc} (TESOURA)')
        print('')
        print('YESSSSS, você ganhou!!!')

    elif jogador == 1 and pc == 1:
        print(f'{nome} jogou: {jogador} (PEDRA)')
        print(f'COMPUTADOR jogou: {pc} (PEDRA)')
        print('')
        print('WOW, EMPATOU !!!')

    elif jogador == 1 and pc == 2:
        print(f'{nome} jogou: {jogador} (PEDRA)')
        print(f'COMPUTADOR jogou: {pc} (PAPEL)')
        print('')
        print('Ah não! você perdeu.')

    elif jogador == 2 and pc == 1:
        print(f'{nome} jogou: {jogador} (PAPEL)')
        print(f'COMPUTADOR jogou: {pc} (PEDRA)')
        print('')
        print('YESSSSS, você ganhou!!!')

    elif jogador == 2 and pc == 2:
        print(f'{nome} jogou: {jogador} (PAPEL)')
        print(f'COMPUTADOR jogou: {pc} (PAPEL)')
        print('')
        print('WOW, EMPATOU !!!')

    elif jogador == 2 and pc == 3:
        print(f'{nome} jogou: {jogador} (PAPEL)')
        print(f'COMPUTADOR jogou: {pc} (TESOURA)')
        print('')
        print('Ah não! você perdeu.')

    elif jogador == 3 and pc == 2:
        print(f'{nome} jogou: {jogador} (TESOURA)')
        print(f'COMPUTADOR jogou: {pc} (PAPEL)')
        print('')
        print('YESSSSS, você ganhou!!!')

    elif jogador == 3 and pc == 3:
        print(f'{nome} jogou: {jogador} (TESOURA)')
        print(f'COMPUTADOR jogou: {pc} (TESOURA)')
        print('')
        print('WOW, EMPATOU !!!')

    elif jogador == 3 and pc == 2:
        print(f'{nome} jogou: {jogador} (TESOURA)')
        print(f'COMPUTADOR jogou: {pc} PAPEL')
        print('')
        print('Ah não! você perdeu.')
    print('')    
    continuar = input('Jogar mais uma partida ?: tecle S para (Sim) ou N para (Não): ').upper().strip()   
    if continuar == 'S':
        jogar = True
        sys('cls')
        continue
    else:
        sys('cls')
        jogar = False
        print('Jogo finalizado!!!')
        break

else:
    jogar = False
    print('Jogo finalizado!!!')
  


