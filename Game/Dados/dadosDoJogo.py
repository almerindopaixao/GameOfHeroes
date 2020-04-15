from time import sleep
import json


def carregarJogo(player):
    """
    Função que carrega o jogo
    """
    try:
        jogoSalvo = open('jogoSalvo.json', 'rb')
        jogoSalvo.close()
    except IOError:
        print('\033[1;31mNão foi encontrado nenhum jogo Salvo\033[m')
        return

    with open('jogoSalvo.json', 'rb') as jogoSalvo:
        data = jogoSalvo.readline()
        data.decode()
        objeto = json.loads(data)

        player.nome = objeto['nome']
        player.For = objeto['For']
        player.Def = objeto['Def']
        player.HP = objeto['HP']
        player.SP = objeto['SP']
        player.inimigosMortos = objeto['inimigosMortos']

    print('Carregando Jogo....')
    sleep(3)
    print('\033[1;32mJogo Carregado\033[m')


def salvarJogo(player):
    """
    Função que salva o jogo
    """
    with open('jogoSalvo.json', 'wb') as jogoSalvo:

        data = player.__dict__

        data_string = json.dumps(data)
        jogoSalvo.write(data_string.encode())

    print('Salvando Jogo..')
    sleep(3)
    print('\033[1;32mJogo Salvo\033[m')
