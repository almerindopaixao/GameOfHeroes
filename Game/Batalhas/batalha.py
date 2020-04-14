import random


class Luta:
    """
    Classe que implementa o combate entre o player e os inimigos
    """
    def __init__(self, player, inimigos):
        self.__player = player
        self.__inimigos = inimigos

    def main(self):
        adversarios = self.criaInimigos()

        while True:
            self.printPlayerInfo()

            while True:
                atk = self.menuCombate()
                if self.veSeAtkValido(atk):
                    break
                else:
                    print('\033[1;31mAtaque não pode ser realizado, escolha novamente.\033[m')

            alvo = self.escolheAlvo(adversarios)

            for inimigo in adversarios:
                if inimigo.num == alvo:
                    break

            if atk == 'lancaDeGelo':
                self.__player.lancaDeGelo(self.__player, inimigo)
            elif atk == 'espadada':
                self.__player.espadada(self.__player, inimigo)
            elif atk == 'flechada':
                self.__player.flechada(self.__player, inimigo)
            else:
                self.__player.curar(self.__player)

            if inimigo.HP <= 0:
                adversarios.remove(inimigo)

            if len(adversarios) == 0:
                venceu = True
                break
            else:
                self.ataqueInimigos(adversarios)
                self.printInimigoInfo(inimigo)

                if self.__player.SP == 0:
                    venceu = False
                    break

        if venceu:
            print('\033[1;32mParabéns Você VENCEU!\033[m\n')

            self.venceu()

            self.__player.inimigosMortos += 1
        else:
            print(f'\033[1;31mVocê sobreviveu a {self.__player.inimigosMortos} combates\033[m')

    def criaInimigos(self):
        """
        Função usada para criar os inimigos de um determinado combate
        """
        from copy import copy

        num_de_inimigos = 2 ** (self.__player.inimigosMortos // 10)

        adversarios = list()

        for i in range(num_de_inimigos):
            inimigo = random.choice(self.__inimigos)
            inimigo.num = i + 1
            adversarios.append(copy(inimigo))

        return adversarios

    def printPlayerInfo(self):
        """
        Imprime as Informações do player
        """
        print(f'\033[1;34m{self.__player.nome:^7}')
        print(f'HP: {self.__player.HP:.2f}')
        print(f'SP: {self.__player.SP:.2f}\033[m')
        print('')

    def printInimigoInfo(self, inimigo):
        """
        Imprime as Informações do inimigo
        """
        print(f'\033[1;31m{inimigo.nome:^7}')
        print(f'HP: {inimigo.HP:.2f}')
        print(f'SP: {inimigo.SP:.2f}\033[m')
        print('')

    def menuCombate(self):
        """
        Função criada para escolher as opções do
        player
        """
        while True:
            comando = input('\033[1;30mDeseja usar Espadada, Flechada, Curar ou lançaDeGelo?\033[m\n').lower()

            if not comando.isalpha():
                print('\033[1;31mDigite apenas letra!\033[m')
            else:
                for key in self.__player.ATKS:
                    if key[0] == comando[0]:
                        return key

                print('\033[1;31mNão entendi seu comando digite novamente.\033[m')

    def veSeAtkValido(self, atk):
        """
        Função usada para verificar se o player tem sp suficiente
        """
        if self.__player.ATKS[atk]['SP'] <= self.__player.SP:
            return True
        else:
            print('\033[1;31mSP Insuficiente\033[m')
            return False

    def escolheAlvo(self, adversarios):
        """
        Função usada para garantir que o player escolha
        um alvo adequado
        """
        while True:
            saida = '\033[1;30mEscolha um alvo dentre: \033[m\n'
            nums = []
            for inimigo in adversarios:
                saida += f'\033[1;34m{inimigo.num} - {inimigo.nome} HP = {inimigo.HP:.2f}/ SP = {inimigo.SP:.2f}\033[m\n'
                nums.append(inimigo.num)

            comando = input(saida)

            if not comando.isdigit():
                print('\033[1;31mDigite o número do inimigo!\033[m')
            else:
                if int(comando) not in nums:
                    print('\033[1;30mDigite um número de inimigo válida\033[m')
                else:
                    return int(comando)

    def ataqueInimigos(self, adversarios):
        for inimigo in adversarios:
            while True:
                atk = self.escolheAtkInimigo(inimigo)

                if inimigo.nome == 'Ogro':
                    if atk == 'clavada':
                        inimigo.clavada(inimigo, self.__player)
                        break
                elif inimigo.nome == 'Globin':
                    if atk == 'espadada':
                        inimigo.espadada(inimigo, self.__player)
                        break
                    if atk == 'flechada':
                        inimigo.flechada(inimigo, self.__player)
                        break
                elif inimigo.nome == 'Esqueleto':
                    if atk == 'espadada':
                        inimigo.espadada(inimigo, self.__player)
                        break
                    if atk == 'curar':
                        inimigo.curar(inimigo)
                        break
                elif inimigo.nome == 'Bruxo':
                    if atk == 'espadada':
                        inimigo.espadada(inimigo, self.__player)
                        break
                    if atk == 'curar':
                        inimigo.curar(inimigo)
                        break
                    if atk == 'relampago':
                        inimigo.relampago(inimigo, self.__player)
                        break
                    if atk == 'bolaDeFogo':
                        inimigo.bolaDeFogo(inimigo, self.__player)
                        break

    def escolheAtkInimigo(self, inimigo):
        while True:
            atk = random.choice(list(inimigo.ATKS.keys()))

            if inimigo.SP >= inimigo.ATKS[atk]['SP']:
                return atk

    def venceu(self):
        """
        Função chamada para quando o player vence o jogo
        """
        while True:
            comando = input('\033[1;30mDeseja restaurar o status(r/restaurar) ou aumentar um atributo (a/aumentar)?\033[m\n').lower()

            if not comando.isalpha():
                print('\033[1;31mDigite apenas letras!\033[m')
            else:
                if comando.startswith('r'):
                    self.__player.HP = 500
                    self.__player.SP = 100
                    return
                elif comando.startswith('a'):
                    self.aumentaAtributo()
                    return
                else:
                    print('\033[1;31mNão entendi seu comando!\033[m')

    def aumentaAtributo(self):
        """
        Permite que o player aumente o valor de um de seus atributos
        """
        while True:
            comando = input('\033[1;30mDeseja aumentar a força(f/for) ou a defesa (d/def)?\033[m\n').lower()

            if not comando.isalpha():
                print('\033[1;31mDigite apenas letras!\033[m')
            else:
                if comando.startswith('f'):
                    self.__player.For += 5
                    break
                elif comando.startswith('d'):
                    self.__player.Def += 5
                    break
                else:
                    print('\033[1;31mNão entendi seu comando!\033[m')

            print(f'\033[1;34mPlayer For: {self.__player.For} \nPlayer Def: {self.__player.Def}\033[m')


