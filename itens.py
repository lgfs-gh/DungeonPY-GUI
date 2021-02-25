from random import randint, choice


class Item:

    def __init__(self, nome, tipo):
        self.__nome = nome
        self.__tipo = tipo

    def __str__(self):
        return self.__nome

    @property
    def nome(self):
        return self.__nome

    @property
    def tipo(self):
        return self.__tipo


def gen_item():
    tipo = randint(0, 1)
    nomes_ataque = ['Espada',
                    'Machado',
                    'Clava',
                    'Adaga',
                    'Cajado',
                    'Espada Longa',
                    'Espada enferrujada',
                    'Amuleto',
                    'Anel',
                    'Cordão']
    nomes_defesa = ['Escudo',
                    'Anel',
                    'Amuleto',
                    'Cordão',
                    'Elmo',
                    'Armadura']
    adjetivos = ['das Trevas',
                 'das Profundezas',
                 'da Escuridão',
                 'da Luz',
                 'com Maldição',
                 'da Destreza',
                 'da Velocidade',
                 'do Sábio',
                 'da Inquietude',
                 'da Força',
                 'do Sangue',
                 'do Cavaleiro',
                 'do Mago',
                 'do Vácuo']

    if tipo == 1:
        item = Item(f'{choice(nomes_ataque)} {choice(adjetivos)} | ATK + 1', 'ataque')
        return item
    else:
        item = Item(f'{choice(nomes_defesa)} {choice(adjetivos)} | DEF + 1', 'defesa')
        return item
