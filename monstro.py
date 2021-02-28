from random import choice, randint


class Monstro:

    def __init__(self: object,
                 nome: str,
                 vida: int,
                 ataque: int,
                 defesa: int,
                 pocoes_drop,
                 itens_drop,
                 experiencia_drop,
                 local: str) -> None:
        self.__nome: str = nome
        self.__vida: int = vida
        self.__ataque: int = ataque
        self.__defesa: int = defesa
        self.__pocoes_drop: list = pocoes_drop
        self.__itens_drop: int = itens_drop
        self.__experiencia_drop: int = experiencia_drop
        self.__local: str = local

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
    def local(self) -> str:
        return self.__local

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
                                     'Ruina Amaldiçoada',
                                     'Pântano',
                                     'Caverna profunda'],
                    'locais_dificil': ['Vulcão',
                                       'Topo da montanha',
                                       'Abismo',
                                       'Castelo',
                                       'Biblioteca Amaldiçoada']}

    dificuldade = randint(1, 100)
    # ---------------- DIFICULDADE: FÁCIL ---------------- #
    if dificuldade in range(1, 80):
        monstro_local = choice(monstro_info['locais_facil'])
        monstro_nome = choice(monstro_info['monstros_facil'])
        monstro_vida = randint(3, 5)
        monstro_ataque = randint(0, 1)
        monstro_defesa = randint(0, 1)
        monstro_p_drop_chance = randint(0, 12)
        monstro_i_drop_chance = randint(0, 20)
        monstro_experiencia_drop = randint(10, 40)

        if monstro_p_drop_chance in range(2):
            pot_drop = 1
        else:
            pot_drop = 0
        if monstro_i_drop_chance in range(2):
            item = 1
        else:
            item = 0

        monstro = Monstro(nome=monstro_nome,
                          vida=monstro_vida,
                          ataque=monstro_ataque,
                          defesa=monstro_defesa,
                          pocoes_drop=pot_drop,
                          itens_drop=item,
                          experiencia_drop=monstro_experiencia_drop,
                          local=monstro_local)
        return monstro

        # ---------------- DIFICULDADE: MÉDIA ---------------- #
    elif dificuldade in range(81, 95):
        monstro_local = choice(monstro_info['locais_medio'])
        monstro_nome = choice(monstro_info['monstros_medio'])
        monstro_vida = randint(5, 8)
        monstro_ataque = randint(0, 3)
        monstro_defesa = randint(0, 3)
        monstro_p_drop_chance = randint(0, 8)
        monstro_i_drop_chance = randint(0, 16)
        monstro_experiencia_drop = randint(40, 60)

        if monstro_p_drop_chance in range(2):
            pot_drop = 1
        else:
            pot_drop = 0
        if monstro_i_drop_chance in range(2):
            item_drop = 1
        else:
            item_drop = 0

        monstro = Monstro(nome=monstro_nome,
                          vida=monstro_vida,
                          ataque=monstro_ataque,
                          defesa=monstro_defesa,
                          pocoes_drop=pot_drop,
                          itens_drop=item_drop,
                          experiencia_drop=monstro_experiencia_drop,
                          local=monstro_local)
        return monstro

    # ---------------- DIFICULDADE: DIFÍCIL ---------------- #
    else:
        monstro_local = choice(monstro_info['locais_dificil'])
        monstro_nome = choice(monstro_info['monstros_dificil'])
        monstro_vida = randint(10, 16)
        monstro_ataque = randint(2, 6)
        monstro_defesa = randint(1, 5)
        monstro_p_drop_chance = randint(0, 4)
        monstro_i_drop_chance = randint(0, 4)
        monstro_experiencia_drop = randint(60, 90)

        if monstro_p_drop_chance in range(2):
            pot_drop = 1
        else:
            pot_drop = 0
        if monstro_i_drop_chance in range(2):
            item_drop = 1
        else:
            item_drop = 0

        monstro = Monstro(nome=monstro_nome,
                          vida=monstro_vida,
                          ataque=monstro_ataque,
                          defesa=monstro_defesa,
                          pocoes_drop=pot_drop,
                          itens_drop=item_drop,
                          experiencia_drop=monstro_experiencia_drop,
                          local=monstro_local)
        return monstro
