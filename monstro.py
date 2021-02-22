from random import choice, randint


class Monstro:

    def __init__(self: object,
                 nome: str,
                 vida: int,
                 ataque: int,
                 defesa: int,
                 pocoes_drop,
                 itens_drop,
                 experiencia_drop) -> None:
        self.__nome: str = nome
        self.__vida: int = vida
        self.__ataque: int = ataque
        self.__defesa: int = defesa
        self.__pocoes_drop: list = pocoes_drop
        self.__itens_drop: int = itens_drop
        self.__experiencia_drop: int = experiencia_drop

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def vida(self) -> int:
        return self.__vida

    @vida.setter
    def vida(self, valor) -> None:
        self.__vida = valor

    @property
    def ataque(self) -> int:
        return self.__ataque

    @property
    def defesa(self) -> int:
        return self.__defesa

    @property
    def pocoes_drop(self) -> int:
        return self.__pocoes_drop

    @property
    def itens_drop(self) -> int:
        return self.__itens_drop

    @property
    def experiencia_drop(self) -> int:
        return self.__experiencia_drop


def gerar_monstro():
    monstro_info = {'monstros_facil': ['Aranha',
                                       'Goblin',
                                       'Rato',
                                       'Aranha Venenosa',
                                       'Urso',
                                       'Lobo',
                                       'Cobra'],
                    'monstros_medio': ['Troll',
                                       'Orc',
                                       'Ladrão',
                                       'Esqueleto',
                                       'Zumbi',
                                       'Ciclope',
                                       'Mago',
                                       'Guerreiro',
                                       'Arqueiro'],
                    'monstros_dificil': ['Dragão',
                                         'Demônio',
                                         'Cavaleiro Amaldiçoado',
                                         'Behemoth',
                                         'Beholder',
                                         'Warlock'],
                    'locais_facil': ['Campo',
                                     'Floresta',
                                     'Caverna',
                                     'Esgoto',
                                     'Ruina',
                                     'Pântano'],
                    'locais_medio': ['Motanha',
                                     'Cemitério',
                                     'Fortaleza',
                                     'Floresta Escura',
                                     'Ruina Amaldiçoada,'
                                     'Pântano',
                                     'Caverna profunda'],
                    'locais_dificil': ['Vulcão',
                                       'Topo da montanha',
                                       'Abismo',
                                       'Castelo',
                                       'Biblioteca Amaldiçoada']}

    dificuldade = randint(1, 100)
    # ---------------- DIFICULDADE: FÁCIL ---------------- #
    if dificuldade in range(1, 70):
        monstro_local = choice(monstro_info['locais_facil'])
        monstro_nome = choice(monstro_info['monstros_facil'])
        monstro_vida = randint(4, 6)
        monstro_ataque = randint(0, 1)
        monstro_defesa = randint(0, 1)
        monstro_p_drop_chance = randint(0, 10)
        monstro_i_drop_chance = randint(0, 10)
        monstro_experiencia_drop = randint(10, 20)

        monstro = Monstro(nome=monstro_nome,
                          vida=monstro_vida,
                          ataque=monstro_ataque,
                          defesa=monstro_defesa,
                          pocoes_drop=monstro_p_drop_chance,
                          itens_drop=monstro_i_drop_chance,
                          experiencia_drop=monstro_experiencia_drop)
        return monstro, monstro_local

        # ---------------- DIFICULDADE: MÉDIA ---------------- #
    elif dificuldade in range(71, 90):
        monstro_local = choice(monstro_info['locais_medio'])
        monstro_nome = choice(monstro_info['monstros_medio'])
        monstro_vida = randint(4, 6)
        monstro_ataque = randint(0, 3)
        monstro_defesa = randint(0, 3)
        monstro_p_drop_chance = randint(0, 10)
        monstro_i_drop_chance = randint(0, 10)
        monstro_experiencia_drop = randint(10, 20)

        monstro = Monstro(nome=monstro_nome,
                          vida=monstro_vida,
                          ataque=monstro_ataque,
                          defesa=monstro_defesa,
                          pocoes_drop=monstro_p_drop_chance,
                          itens_drop=monstro_i_drop_chance,
                          experiencia_drop=monstro_experiencia_drop)
        return monstro, monstro_local

    # ---------------- DIFICULDADE: DIFÍCIL ---------------- #
    else:
        monstro_local = choice(monstro_info['locais_dificil'])
        monstro_nome = choice(monstro_info['monstros_dificil'])
        monstro_vida = randint(4, 6)
        monstro_ataque = randint(2, 4)
        monstro_defesa = randint(1, 3)
        monstro_p_drop_chance = randint(0, 10)
        monstro_i_drop_chance = randint(0, 10)
        monstro_experiencia_drop = randint(10, 20)

        monstro = Monstro(nome=monstro_nome,
                          vida=monstro_vida,
                          ataque=monstro_ataque,
                          defesa=monstro_defesa,
                          pocoes_drop=monstro_p_drop_chance,
                          itens_drop=monstro_i_drop_chance,
                          experiencia_drop=monstro_experiencia_drop)
        return monstro, monstro_local
