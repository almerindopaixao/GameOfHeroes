def inicio():
    print('\033[1;30m=\033[m' * 79)
    print(f'\033[1;31m{"G  A  M  E    O  F    H  E  R  O  E  S":^79}\033[m')
    print('\033[1;30m=\033[m' * 79)
    print('')


def menuInicial():
    while True:

        comando = input('\033[1;30mDeseja iniciar novo jogo(n/novo), carregar um jogo(c/carregar) ou sair(s/sair)?\n\033[m').lower()
        if not comando.isalpha():
            print('\033[1;31mDigite apenas letra!\033[m')
        else:
            if comando.startswith('c') or comando.startswith('n') or comando.startswith('s'):
                return comando
            else:
                print('\033[1;31mNão entendi seu comando digite novamente.\033[m')


def novoJogo(player):
    player.nome = input('\033[1;30mDigite o nome do héroi:\033[m\n')
    print(f'\033[1;32mBom {player.nome}, o jogo é simples\n')
    print('A cada rodada você pode escolher entre salvar o jogo, entrar em combate ou sair')
    print('Uma vez que você entre em combate terá de enfrentar inimigos')
    print('Se morrer acabou pra você')
    print('Se você sobreviver poderá escolher aumentar os atributos do seu personagem ou se curar')
    print('A cada 10 inimigos vencidos o número de inimigos a enfrentar dobra')
    print('Boa sorte\033[m\n')


def menuJogo():
    while True:

        comando = input('\033[1;30mDeseja salvar(s/salvar), enfentrar novo inimigo(c/combate) ou sair(e/exit)?\n\033[m').lower()
        if not comando.isalpha():
            print('\033[1;31mDigite apenas letra!\033[m')
        else:
            if comando.startswith('c') or comando.startswith('s') or comando.startswith('e'):
                return comando
            else:
                print('\033[1;31mNão entendi seu comando digite novamente.\033[m')



