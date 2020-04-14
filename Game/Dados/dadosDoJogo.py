from time import sleep


def carregarJogo(player):
    """
    Função que carrega o jogo
    """
    try:
        jogoSalvo = open('jogoSalvo.txt', 'r')
        jogoSalvo.close()
    except FileNotFoundError:
        print('\033[1;31mNão foi encontrado nenhum jogo Salvo\033[m')
        return

    with open('jogoSalvo.txt', 'r') as jogoSalvo:
        dados = jogoSalvo.read().split('\n')

        player.nome = dados[0]
        player.For = int(dados[1])
        player.Def = int(dados[2])
        player.HP = float(dados[3])
        player.SP = float(dados[4])
        player.inimigosMortos = int(dados[5])

    print('Carregando Jogo....')
    sleep(3)
    print('\033[1;32mJogo Carregado\033[m')


def salvarJogo(player):
    """
    Função que salva o jogo
    """
    jogoSalvo = open('jogoSalvo.txt', 'w')

    jogoSalvo.write(f'{player.nome}\n')
    jogoSalvo.write(f'{player.For}\n')
    jogoSalvo.write(f'{player.Def}\n')
    jogoSalvo.write(f'{player.HP}\n')
    jogoSalvo.write(f'{player.SP}\n')
    jogoSalvo.write(f'{player.inimigosMortos}')

    jogoSalvo.close()

    print('Salvando Jogo..')
    sleep(3)
    print('\033[1;32mJogo Salvo\033[m')
