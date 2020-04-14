from Game.Personagens.personagens import *
from Game.Interface.interface import *
from Game.Dados.dadosDoJogo import *
from Game.Batalhas.batalha import Luta


def main():
    player = Personagem('Player', 20, 20, 500, 100)
    ogro = Personagem('Ogro', 30, 5, 100, 5)
    globin = Personagem('Globin', 15, 10, 70, 10)
    esqueleto = Personagem('Esqueleto', 20, 20, 80, 20)
    bruxo = Personagem('Bruxo', 10, 30, 80, 20)

    inimigos = [ogro, globin, esqueleto, bruxo]

    inicio()

    while True:
        com = menuInicial()

        if com.startswith('c'):
            carregarJogo(player)
        elif com.startswith('s'):
            break
        else:
            novoJogo(player)

        while True:
            com = menuJogo()

            if com.startswith('c'):
               luta = Luta(player, inimigos)
               luta.main()
            elif com.startswith('s'):
                salvarJogo(player)
            else:
                break

    print('\033[1;30mOBRIGADO POR JOGAR GAME OF HEROES\033[m')


if __name__ == '__main__':
    main()
