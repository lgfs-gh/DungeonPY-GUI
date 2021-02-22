from random import choice, randint

import PySimpleGUI as sg
from jogador import Jogador
from monstro import gerar_monstro


# ----- Varieveis Teste ------ #
jogador = None
monstro, local = gerar_monstro()


# --------- SISTEMA DE BATALHA ---------- #
def batalha(escolha):
    if escolha == 1:
        pass
    else:
        pass


def main():
    global jogador
    nome_random = choice(['Arther', 'Frery', 'Remonnet', 'Richessa', 'Adelie', 'Mirielda'])
    # ============================== LAYOUT GLOBAL MENU ============================== #
    layout_menu = [
        [sg.Text('# ----- NOME ----- #', font='Any 12')],
        [sg.InputText(default_text=nome_random, size=(30, 1), key='_nome_p_')],
        [sg.Text('# ----- SEXO ----- #', font='Any 12')],
        [sg.Checkbox(' Masculino'), sg.Checkbox(' Feminino')],
        [sg.Button('Iniciar', size=(30, 1), key='_iniciar_')],
        [sg.Button('Sair', size=(30, 1), key='Cancel')]
    ]

    window = sg.Window(
        title='DUNGEON',
        layout=layout_menu,
        element_justification='c'
    )

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
            break
        if event == '_iniciar_':
            jogador = Jogador(values['_nome_p_'])
            sg.popup('Jogo iniciado!')
            window.Close()
            game()
    window.Close()


def game():
    # -------- VARIAVEIS ----------- #
    global jogador

    # ------------ IMAGENS ------------- #
    layout_player_imagem = [
        [sg.Text('INSIRA A IMAGEM DO PLAYER AQUI!')]
    ]
    layout_fundo_imagem = [
        [sg.Text('INSIRA A IMAGEM DO FUNDO AQUI!')]
    ]
    layout_monstro_imagem = [
        [sg.Text('INSIRA A IMAGEM DO MONSTRO AQUI!')]
    ]

    # ------------ PLAYER STATUS/MOCHILA ------------- #
    layout_player_status = [
        [sg.Text(f'Nome: {jogador.nome}')],
        [sg.Text(f'Vida: {jogador.vida}',
                 key='_p_vida_')],
        [sg.Text(f'Ataque: {jogador.ataque}',
                 key='_p_atk_')],
        [sg.Text(f'Defesa: {jogador.defesa}',
                 key='_p_def_')],
        [sg.Text(f'Experiencia: {jogador.experiencia}',
                 key='_p_xp_')],
        [sg.Text(f'Nivel: {jogador.nivel}',
                 key='_p_nivel_')],
        [sg.Button(button_text='Mochila',
                   enable_events=True,
                   key='_mostrar_mochila_')]
    ]
    layout_player_mochila = [
        [sg.Text(f'Quantidade de poções: {jogador.pocoes}\n'
                 f'ITENS: {jogador.mostrar_itens()}')],
        [sg.Button(button_text='Usar poção',
                   enable_events=True,
                   key='_usar_pocao_'),
         sg.Button(button_text='Status',
                   enable_events=True,
                   key='_mostrar_status_')]
    ]
    layout_player_info = [
        [sg.Frame(title='# ---- STATUS ---- #',
                  element_justification='c',
                  border_width=0,
                  layout=layout_player_status,
                  visible=True,
                  key='_player_status_'),
         sg.Frame(title='Mochila',
                  layout=layout_player_mochila,
                  visible=False,
                  key='_player_mochila_')
         ],
    ]
    layout_player_completo = [
        [sg.Frame(title='PLAYER IMAGEM!',
                  layout=layout_player_imagem)],
        [sg.Frame(title='PLAYER INFO',
                  layout=layout_player_info)]
    ]
    # ------------ INFORMACOES DE BATALHA ------------- #
    layout_local_batalha = [
        [sg.Text('INSIRA O LOCAL DE BATALHA AQUI!')]
    ]
    layout_informacoes_batalha = [
        [sg.Text('INSIRA INFORMAÇÕES DE DANO!\n\n\n\n\n', key='_info_batalha_')]
    ]
    layout_escolhas = [
        [sg.Button(button_text='Lutar', key='_lutar_', disabled=False),
         sg.Button(button_text='OK!', key='_ok_', disabled=True),
         sg.Button(button_text='Fugir', key='_fugir_', disabled=False)]
    ]
    layout_batalha_info = [
        [sg.Frame(title='LOCAL',
                  layout=layout_local_batalha),
         ],
        [sg.Frame(title='BATALHA INFO',
                  layout=layout_informacoes_batalha)],
        [sg.Frame(title='ESCOLHAS!',
                  layout=layout_escolhas)]
    ]
    layout_batalha_completo = [
        [sg.Frame(title='FUNDO IMAGEM!',
                  layout=layout_fundo_imagem)],
        [sg.Frame(title='BATALHA INFO',
                  layout=layout_batalha_info)]
    ]
    # ------------ MONSTRO STATUS ------------- #
    layout_monstro_status = [
        [sg.Text(f'Nome: {monstro.nome}')],
        [sg.Text(f'Vida: {monstro.vida}',
                 key='_m_vida_')],
        [sg.Text(f'Ataque: {monstro.ataque}',
                 key='_m_atk_')],
        [sg.Text(f'Defesa: {monstro.defesa}',
                 key='_m_def_')]
    ]
    layout_monstro_info = [
        [sg.Frame(title='# ---- STATUS ---- #',
                  element_justification='c',
                  border_width=0,
                  layout=layout_monstro_status)]
    ]
    layout_monstro_completo = [
        [sg.Frame(title='MONSTRO IMAGEM!',
                  layout=layout_monstro_imagem)],
        [sg.Frame(title='MONSTRO INFO!',
                  layout=layout_monstro_info)]
    ]

    # ============================== LAYOUT GLOBAL JOGO ============================== #
    layout = [
        [sg.Frame(title='PLAYER',
                  element_justification='c',
                  layout=layout_player_completo
                  ),
         sg.Frame(title='BATALHA',
                  element_justification='c',
                  layout=layout_batalha_completo),
         sg.Frame(title='MONSTRO',
                  element_justification='c',
                  layout=layout_monstro_completo)
         ]
    ]

    window = sg.Window(
        title='DUNGEON',
        layout=layout,
        element_justification='c'
    )

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
            break
        if event == '_mostrar_mochila_':
            window.FindElement('_player_status_').Update(visible=False)
            window.FindElement('_player_mochila_').Update(visible=True)
        if event == '_mostrar_status_':
            window.FindElement('_player_mochila_').Update(visible=False)
            window.FindElement('_player_status_').Update(visible=True)
        # ----------- EVENTOS BATALHA -------------- #
        if event == '_lutar_':
            window.FindElement('_lutar_').Update(disabled=True)
            window.FindElement('_fugir_').Update(disabled=True)
            window.FindElement('_ok_').Update(disabled=False)
            window.FindElement('_info_batalha_').\
                Update(value=f'Você entrou em batalha com {monstro.nome}!')
        if event == '_fugir_':
            window.FindElement('_lutar_').Update(disabled=True)
            window.FindElement('_fugir_').Update(disabled=True)
            window.FindElement('_ok_').Update(disabled=True)
            sucesso = randint(1, 6)
            if sucesso in range(1, 4):
                # FUGIU COM SUCESSO
                window.FindElement('_lutar_').Update(disabled=False)
                window.FindElement('_fugir_').Update(disabled=False)
                window.FindElement('_ok_').Update(disabled=True)
                window.FindElement('_info_batalha_').Update(value='Fugiu com sucesso!')
            else:
                window.FindElement('_lutar_').Update(disabled=True)
                window.FindElement('_fugir_').Update(disabled=True)
                window.FindElement('_ok_').Update(disabled=False)
                window.FindElement('_info_batalha_').Update(value=f'Você foi apanhado por {monstro.nome}!')

        if event == '_ok_':
            if jogador.vida > 0:
                if monstro.vida > 0:
                    dado_player = randint(1, 6)
                    player_ataque = dado_player + jogador.ataque
                    player_defesa = dado_player + jogador.defesa
                    dado_monstro = randint(1, 6)
                    monstro_ataque = dado_monstro + monstro.ataque
                    monstro_defesa = dado_monstro + monstro.defesa
                    if player_ataque > monstro_defesa and monstro_ataque > player_defesa:
                        dano = player_ataque - monstro_defesa
                        dano2 = monstro_ataque - player_defesa
                        monstro.vida -= dano
                        jogador.vida -= dano2
                        window.FindElement('_info_batalha_').\
                            Update(value=f'Você deu {dano} de dano em {monstro.nome}!\n'
                                         f'{monstro.nome} deu um dano de {dano} em você!')
                        window.FindElement('_m_vida_').\
                            Update(value=f'Vida: {monstro.vida}')
                        window.FindElement('_p_vida_').\
                            Update(value=f'Vida: {jogador.vida}')
                    elif player_ataque > monstro_defesa and monstro_ataque <= player_defesa:
                        dano = player_ataque - monstro_defesa
                        monstro.vida -= dano
                        window.FindElement('_info_batalha_').\
                            Update(value=f'Você deu {dano} de dano em {monstro.nome}!\n'
                                         f'Você defendeu o ataque de {monstro.nome}!')
                        window.FindElement('_m_vida_').\
                            Update(value=f'Vida: {monstro.vida}')
                    elif player_ataque <= monstro_defesa and monstro_ataque > player_defesa:
                        dano = monstro_ataque - player_defesa
                        jogador.vida -= dano
                        window.FindElement('_info_batalha_').\
                            Update(value=f'{monstro.nome} defendeu seu ataque!\n'
                                         f'{monstro.nome} deu um dano de {dano} em você!')
                        window.FindElement('_p_vida_').\
                            Update(value=f'Vida: {jogador.vida}')
                    elif player_ataque <= monstro_defesa and monstro_ataque <= player_defesa:
                        window.FindElement('_info_batalha_').\
                            Update(value=f'Você defendeu o ataque de {monstro.nome}!\n'
                                         f'{monstro.nome} defendeu seu ataque!')
                else:
                    jogador.monstros_derrotados += 1
                    jogador.experiencia += monstro.experiencia_drop
                    window.FindElement('_info_batalha_'). \
                        Update(value=f'Você derrotou {monstro.nome}!\n'
                                     f'Você recebeu {monstro.experiencia_drop} XP!\n'
                                     f'Você recebeu {monstro.pocoes_drop} POÇÕES\n'
                                     f'Você recebeu o item: {monstro.itens_drop}')
            else:
                sg.popup('Você morreu!')
                window.close()
                main()

    window.Close()


if __name__ == '__main__':
    main()
