from random import randint, choice
from monstro import Monstro

batalha_info = {'locais_facil': ['Local F1', 'Local F2', 'Local F3'],
                'locais_medio': ['Local M1', 'Local M2', 'Local M3'],
                'locais_dificil': ['Local D1', 'Local D2', 'Local D3'],
                'monstros_facil': ['Monstro F1', 'Monstro F2', 'MonstroF3'],
                'monstros_medio': ['Monstro M1', 'Monstro M2', 'Monstro M3'],
                'monstros_dificil': ['Monstro D1', 'Monstro D2', 'Monstro D3']}


def gerar_monstro(dificuldade):

    if dificuldade in range(1, 70):
        local = choice(batalha_info['locais_facil'])
        monstro_nome = choice(batalha_info['monstros_facil'])
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
        return monstro, local
    elif dificuldade in range(71, 90):
        local = choice(batalha_info['locais_medio'])
        monstro_nome = choice(batalha_info['monstros_medio'])
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
        return monstro, local
    else:
        local = choice(batalha_info['locais_dificil'])
        monstro_nome = choice(batalha_info['monstros_dificil'])
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
        return monstro, local


def batalha(escolha):

    dificuldade = randint(1, 100)
    monstro, local = gerar_monstro(dificuldade)

    if escolha == 1:  # Lutar
        pass
    else:  # Fugir
        pass
