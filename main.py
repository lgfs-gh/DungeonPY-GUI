import PySimpleGUI as sg
from jogador import Jogador
from monstro import Monstro

# ----- Varieveis Teste ------ #
jogador = Jogador('Teste')
monstro = Monstro(nome='Aranha',
                  vida=10,
                  ataque=7,
                  defesa=3,
                  pocoes_drop=1,
                  itens_drop=['Adaga, Escudo'],
                  experiencia_drop=10)


def main():
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
        [sg.Text(f'Nome: {jogador.nome}\n'
                 f'Experiencia: {jogador.experiencia}\n'
                 f'Nivel: {jogador.nivel}\n'
                 f'Vida: {jogador.vida}\n'
                 f'Ataque: {jogador.ataque}\n'
                 f'Defesa: {jogador.defesa}\n')],
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
        [sg.Frame(title='Status',
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
        [sg.Frame(title='LAYOUT INFO!',
                  layout=layout_player_info)]
    ]
    # ------------ INFORMACOES DE BATALHA ------------- #
    layout_local_batalha = [
        [sg.Text('INSIRA O LOCAL DE BATALHA AQUI!')]
    ]
    layout_informacoes_batalha = [
        [sg.Text('INSIRA O LOCAL DE BATALHA AQUI!\n'
                 'EX: ROLOU 6 NO DADO\n'
                 'EX: RECEBEU 2 DE DANO')]
    ]
    layout_escolhas = [
        [sg.Button(button_text='Atacar'),
         sg.Button(button_text='OK!'),
         sg.Button(button_text='Fugir')]
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
        [sg.Text(f'Nome: {monstro.nome}\n'
                 f'Vida: {monstro.vida}\n'
                 f'Ataque: {monstro.ataque}\n'
                 f'Defesa: {monstro.defesa}\n')]
    ]
    layout_monstro_info = [
        [sg.Frame(title='Status',
         layout=layout_monstro_status)]
    ]
    layout_monstro_completo = [
        [sg.Frame(title='MONSTRO IMAGEM!',
                  layout=layout_monstro_imagem)],
        [sg.Frame(title='MONSTRO INFO!',
                  layout=layout_monstro_info)]
    ]

    # ============================== LAYOUT GLOBAL DA TELA ============================== #
    layout = [
        [sg.Frame(title='PLAYER',
                  layout=layout_player_completo
                  ),
         sg.Frame(title='BATALHA',
                  layout=layout_batalha_completo),
         sg.Frame(title='MONSTRO',
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


if __name__ == '__main__':
    main()
