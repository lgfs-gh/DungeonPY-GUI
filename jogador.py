class Jogador:

    def __init__(self: object, nome: str) -> None:
        self.__nome: str = nome
        self.__vida: int = 10
        self.__ataque: int = 1
        self.__defesa: int = 1
        self.__pocoes: int = 0
        self.__monstros_derrotados: int = 0
        self.__itens_coletados: int = 0
        self.__fugas_sucesso: int = 0
        self.__fugas_falha: int = 0
        self.__experiencia: int = 0
        self.__nivel: int = 0
        self.__mochila: list = ['algo', 'algo2']

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def vida(self) -> int:
        return self.__vida

    @vida.setter
    def vida(self, valor):
        self.__vida = valor

    @property
    def ataque(self) -> int:
        return self.__ataque

    @ataque.setter
    def ataque(self, valor):
        self.__ataque = valor

    @property
    def defesa(self) -> int:
        return self.__defesa

    @defesa.setter
    def defesa(self, valor):
        self.__defesa = valor

    @property
    def pocoes(self) -> int:
        return self.__pocoes

    @pocoes.setter
    def pocoes(self, valor):
        self.__pocoes = valor

    @property
    def monstros_derrotados(self) -> int:
        return self.__monstros_derrotados

    @monstros_derrotados.setter
    def monstros_derrotados(self, valor):
        self.__monstros_derrotados = valor

    @property
    def itens_coletados(self) -> int:
        return self.__itens_coletados

    @itens_coletados.setter
    def itens_coletados(self, valor):
        self.__itens_coletados = valor

    @property
    def fugas_sucesso(self):
        return self.__fugas_sucesso

    @fugas_sucesso.setter
    def fugas_sucesso(self, valor):
        self.__fugas_sucesso = valor

    @property
    def fugas_falha(self):
        return self.__fugas_falha

    @fugas_falha.setter
    def fugas_falha(self, valor):
        self.__fugas_falha = valor

    @property
    def experiencia(self) -> int:
        return self.__experiencia

    @experiencia.setter
    def experiencia(self, valor):
        self.__experiencia = valor

    @property
    def nivel(self) -> int:
        return self.__nivel

    @nivel.setter
    def nivel(self, valor):
        self.__nivel = valor

    def mostrar_itens(self):
        itens = ''
        for item in self.__mochila:
            itens = itens + '\n' + item
        return itens
