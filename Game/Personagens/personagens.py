class Personagem(object):
    def __init__(self, Nome, For, Def, HP, SP):
        self.nome = Nome
        self.For = For
        self.Def = Def
        self.HP = HP
        self.SP = SP
        self.ATKS = {'espadada': {'SP': 0},
                     'flechada': {'SP': 2},
                     'curar': {'SP': 10},
                     'lancaDeGelo': {'SP': 10},
                     'clavada': {'SP': 0},
                     'relampago': {'SP': 5},
                     'bolaDeFogo': {'SP': 10}
                     }
        self.inimigosMortos = 0

    @staticmethod
    def calc_dano(atacante, atacado, x):
        from random import random

        return max((atacante.For - atacado.Def / x) * random(), 1)

    def espadada(self, atacante, atacado):
        """
        Função que implementa o ataque da espada
        """
        dano = Personagem.calc_dano(atacante, atacado, 1)

        atacado.HP -= dano

        print(f'\033[1;34m{atacante.nome} usou Ataque de Espada em {atacado.nome}')
        print(f'{atacante.nome} causou {dano:.2f} de dano\033[m')
        print('')

    def flechada(self, atacante, atacado):
        """
        Função que implementa o ataque de Flexa
        """
        dano = Personagem.calc_dano(atacante, atacado, 2)

        atacado.HP -= dano
        atacante.SP -= 2

        print(f'\033[1;34m{atacante.nome} usou Ataque de Flexa em {atacado.nome}')
        print(f'{atacante.nome} causou {dano:.2f} de dano\033[m')
        print('')

    def clavada(self, atacante, atacado):
        """
        Função que implementa o ataque de Clava
        """
        dano = Personagem.calc_dano(atacante, atacado, 1)

        atacado.HP -= dano

        print(f'\033[1;31m{atacante.nome} usou Ataque de Espada em {atacado.nome}')
        print(f'{atacante.nome} causou {dano:.2f} de dano\033[m')
        print('')

    def relampago(self, atacante, atacado):
        """
        Função que implementa o ataque de Relâmpago
        """
        dano = Personagem.calc_dano(atacante, atacado, 3)

        atacado.HP -= dano
        atacante.SP -= 5

        print(f'\033[1;31m{atacante.nome} usou Relâmpago em {atacado.nome}')
        print(f'{atacante.nome} causou {dano:.2f} de dano\033[m')
        print('')

    def bolaDeFogo(self, atacante, atacado):
        """
        Função que implementa o ataque de Bola de Fogo
        """
        dano = Personagem.calc_dano(atacante, atacado, 1)

        atacado.HP -= dano
        atacante.SP -= 10

        print(f'\033[1;31m{atacante.nome} usou Bola de Fogo em {atacado.nome}')
        print(f'{atacante.nome} causou {dano:.2f} de dano\033[m')
        print('')

    def lancaDeGelo(self, atacante, atacado):
        """
        Função que implementa o ataque Lança de Gelo
        """
        dano = Personagem.calc_dano(atacante, atacado, 1)

        atacado.HP -= dano
        atacante.SP -= 10

        print(f'\033[1;34m{atacante.nome} usou Lança de Gelo em {atacado.nome}')
        print(f'{atacante.nome} causou {dano:.2f} de dano\033[m')
        print('')

    def curar(self, usuario):
        """
        Função que implementa Curar
        """
        usuario.HP += 10
        usuario.SP -= 10

        print(f'\033[1;32m{usuario.nome} usou curar\033[m')
        print('')


