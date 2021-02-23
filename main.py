from random import choice, randint
from itens import gen_item

import PySimpleGUI as sg
from jogador import Jogador
from monstro import gerar_monstro

# ----- Varieveis Teste ------ #
jogador = None
monstro = gerar_monstro()


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
    global monstro

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
        [sg.Text(f'Nome: {jogador.nome}',
                 size=(30, 1),)],
        [sg.Text(f'Vida: {jogador.vida}',
                 size=(30, 1),
                 key='_p_vida_')],
        [sg.Text(f'Ataque: {jogador.ataque}',
                 size=(30, 1),
                 key='_p_atk_')],
        [sg.Text(f'Defesa: {jogador.defesa}',
                 size=(30, 1),
                 key='_p_def_')],
        [sg.Text(f'Experiencia: {jogador.experiencia}',
                 size=(30, 1),
                 key='_p_xp_')],
        [sg.Text(f'Nivel: {jogador.nivel}',
                 size=(30, 1),
                 key='_p_nivel_')],
        [sg.Button(button_text='Mochila',
                   enable_events=True,
                   key='_mostrar_mochila_')]
    ]
    layout_player_mochila = [
        [sg.Text(f'Quantidade de poções: {jogador.pocoes}\n',
                 key='_qnt_pocoes_')],
        [sg.Text(f'ITENS: {jogador.mostrar_itens()}',
                 size=(30, 10),
                 key='_p_itens_')],
        [sg.Button(button_text='Usar poção',
                   enable_events=True,
                   key='_usar_pocao_'),
         sg.Button(button_text='Status',
                   enable_events=True,
                   key='_mostrar_status_')]
    ]
    layout_player_info = [
        [sg.Frame(title='Status',
                  border_width=1,
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
        [sg.Text(f'Você está num(a) {monstro.local}',
                 size=(40, 2),
                 justification='c',
                 key='_local_')]
    ]
    layout_informacoes_batalha = [
        [sg.Text(f'Você se depara com um(a) {monstro.nome}', key='_info_batalha_',
                 justification='c',
                 size=(40, 5))]
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
                  element_justification='c',
                  layout=layout_batalha_info)]
    ]
    # ------------ MONSTRO STATUS ------------- #
    layout_monstro_status = [
        [sg.Text(f'Nome: {monstro.nome}',
                 size=(30, 1),
                 justification='c',
                 key='_m_nome_')],
        [sg.Text(f'Vida: {monstro.vida}',
                 key='_m_vida_')],
        [sg.Text(f'Ataque: {monstro.ataque}',
                 key='_m_atk_')],
        [sg.Text(f'Defesa: {monstro.defesa}',
                 key='_m_def_')]
    ]
    layout_monstro_info = [
        [sg.Frame(title='STATUS',
                  title_location='n',
                  element_justification='c',
                  border_width=0,
                  layout=layout_monstro_status)]
    ]
    layout_monstro_completo = [
        [sg.Frame(title='MONSTRO IMAGEM!',
                  layout=layout_monstro_imagem)],
        [sg.Frame(title='MONSTRO INFO!',
                  element_justification='c',
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
        # =========================== EVENTOS BATALHA =========================== #
        # ------------- ESCOLHENDO LUTAR ------------- #
        if event == '_lutar_':
            window.FindElement('_lutar_').Update(disabled=True)
            window.FindElement('_fugir_').Update(disabled=True)
            window.FindElement('_ok_').Update(disabled=False)
            window.FindElement('_info_batalha_'). \
                Update(value=f'Você entrou em batalha com {monstro.nome}!')
        # ------------- ESCOLHENDO FUGIR ------------- #
        if event == '_fugir_':
            window.FindElement('_lutar_').Update(disabled=True)
            window.FindElement('_fugir_').Update(disabled=True)
            window.FindElement('_ok_').Update(disabled=True)
            sucesso = randint(1, 6)
            if sucesso in range(1, 4):
                # FUGIU COM SUCESSO
                jogador.fugas_sucesso += 1
                window.FindElement('_lutar_').Update(disabled=False)
                window.FindElement('_fugir_').Update(disabled=False)
                window.FindElement('_ok_').Update(disabled=True)
                sg.popup_quick('Você fugiu com sucesso!')
                monstro = gerar_monstro()
                window.FindElement('_m_nome_').Update(value=f'Nome: {monstro.nome}')
                window.FindElement('_m_vida_').Update(value=f'Vida: {monstro.vida}')
                window.FindElement('_m_atk_').Update(value=f'Ataque: {monstro.ataque}')
                window.FindElement('_m_def_').Update(value=f'Defesa: {monstro.defesa}')
                window.FindElement('_local_').Update(value=f'Você está num(a) {monstro.local}')
                window.FindElement('_info_batalha_').Update(value=f'Você se depara com um(a) {monstro.nome}')
            else:
                # FALHOU EM FUGIR
                jogador.fugas_falha += 1
                window.FindElement('_lutar_').Update(disabled=True)
                window.FindElement('_fugir_').Update(disabled=True)
                window.FindElement('_ok_').Update(disabled=False)
                sg.popup_quick('Você falhou em fugir!')
                window.FindElement('_info_batalha_'). \
                    Update(value=f'Você foi apanhado por {monstro.nome}!')

        # ------------- LUTANDO ------------- #
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
                        window.FindElement('_info_batalha_'). \
                            Update(value=f'Você deu {dano} de dano em {monstro.nome}!\n\n'
                                         f'{monstro.nome} deu um dano de {dano} em você!')
                        window.FindElement('_m_vida_'). \
                            Update(value=f'Vida: {monstro.vida}')
                        window.FindElement('_p_vida_'). \
                            Update(value=f'Vida: {jogador.vida}')
                    elif player_ataque > monstro_defesa and monstro_ataque <= player_defesa:
                        dano = player_ataque - monstro_defesa
                        monstro.vida -= dano
                        window.FindElement('_info_batalha_'). \
                            Update(value=f'Você deu {dano} de dano em {monstro.nome}!\n\n'
                                         f'Você defendeu o ataque de {monstro.nome}!')
                        window.FindElement('_m_vida_'). \
                            Update(value=f'Vida: {monstro.vida}')
                    elif player_ataque <= monstro_defesa and monstro_ataque > player_defesa:
                        dano = monstro_ataque - player_defesa
                        jogador.vida -= dano
                        window.FindElement('_info_batalha_'). \
                            Update(value=f'{monstro.nome} defendeu seu ataque!\n\n'
                                         f'{monstro.nome} deu um dano de {dano} em você!')
                        window.FindElement('_p_vida_'). \
                            Update(value=f'Vida: {jogador.vida}')
                    elif player_ataque <= monstro_defesa and monstro_ataque <= player_defesa:
                        window.FindElement('_info_batalha_'). \
                            Update(value=f'Você defendeu o ataque de {monstro.nome}!\n\n'
                                         f'{monstro.nome} defendeu seu ataque!')
                else:
                    # ------------ ADICIONANDO XP/ITEM/DROP E MOSTRANDO ------------ #
                    # - XP!
                    jogador.monstros_derrotados += 1
                    jogador.experiencia += monstro.experiencia_drop
                    window.FindElement('_p_xp_'). \
                        Update(value=f'Experiencia: {jogador.experiencia}')

                    # - POT!
                    if monstro.pocoes_drop == 1:
                        jogador.pocoes += 1
                        window.FindElement('_qnt_pocoes_'). \
                            Update(value=f'Quantidade de poções: {jogador.pocoes}\n')

                    # - ITEM!
                    if monstro.itens_drop == 1:
                        jogador.itens_coletados += 1
                        item = gen_item()
                        if item.tipo == 'ataque':
                            jogador.ataque += 1
                            window.FindElement('_p_atk_'). \
                                Update(value=f'Ataque: {jogador.ataque}')
                        else:
                            jogador.defesa += 1
                            window.FindElement('_p_def_'). \
                                Update(value=f'Defesa: {jogador.ataque}')

                        jogador.adicionar_na_mochila(item)
                        window.FindElement('_p_itens_'). \
                            Update(value=f'ITENS: {jogador.mostrar_itens()}')
                        # --- POP UP --- #
                        sg.popup(f'Você derrotou {monstro.nome}!\n\n'
                                 f'Você recebeu {monstro.experiencia_drop} XP!\n\n'
                                 f'Você recebeu {monstro.pocoes_drop} POÇÕES\n\n'
                                 f'Você recebeu o item:\n{item.nome}\n')
                    else:
                        # --- POP UP --- #
                        sg.popup(f'Você derrotou {monstro.nome}!\n\n'
                                 f'Você recebeu {monstro.experiencia_drop} XP!\n\n'
                                 f'Você recebeu {monstro.pocoes_drop} POÇÕES\n')

                    # ---------- GERANDO A PROXIMA BATALHA ----------- #
                    monstro = gerar_monstro()
                    window.FindElement('_m_nome_').Update(value=f'Nome: {monstro.nome}')
                    window.FindElement('_m_vida_').Update(value=f'Vida: {monstro.vida}')
                    window.FindElement('_m_atk_').Update(value=f'Ataque: {monstro.ataque}')
                    window.FindElement('_m_def_').Update(value=f'Defesa: {monstro.defesa}')
                    window.FindElement('_local_').Update(value=f'Você está num(a) {monstro.local}')
                    window.FindElement('_info_batalha_').Update(value=f'Você se depara com um(a) {monstro.nome}')
                    window.FindElement('_lutar_').Update(disabled=False)
                    window.FindElement('_fugir_').Update(disabled=False)
                    window.FindElement('_ok_').Update(disabled=True)
            else:
                # ---------------- MORTE DO JOGADOR ---------------------- #
                sg.popup(f'Você morreu {jogador.nome}!\n\n'
                         f'Você atingiu nível {jogador.nivel}\n\n'
                         f'Realizou {jogador.fugas_sucesso} fuga(s) com sucesso\n\n'
                         f'Foi apanhado {jogador.fugas_falha} vez(es) tentando fugir\n\n'
                         f'Acumulou {jogador.ataque} ponto(s) de ataque\n\n'
                         f'Acumulou {jogador.defesa} ponto(s) de defesa\n\n'
                         f'Derrotou {jogador.monstros_derrotados} monstro(s).\n\n'
                         f'Coletou {jogador.itens_coletados} itens.')
                window.close()
                main()

    window.Close()


if __name__ == '__main__':
    main()
