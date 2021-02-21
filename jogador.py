class Jogador:

    def __init__(self: object, nome: str) -> None:
        self.__nome: str = nome
        self.__vida: int = 10
        self.__ataque: int = 1
        self.__defesa: int = 1
        self.__pocoes: int = 0
        self.__monstros_derrotados: int = 0
        self.__itens_coletados: int = 0
        self.__experiencia: int = 0
        self.__nivel: int = 0
        self.__mochila: list = ['algo', 'algo2']

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def vida(self) -> int:
        return self.__vida

    @property
    def ataque(self) -> int:
        return self.__ataque

    @property
    def defesa(self) -> int:
        return self.__defesa

    @property
    def pocoes(self) -> int:
        return self.__pocoes

    @property
    def monstros_derrotados(self) -> int:
        return self.__monstros_derrotados

    @property
    def itens_coletados(self) -> int:
        return self.__itens_coletados

    @property
    def experiencia(self) -> int:
        return self.__experiencia

    @property
    def nivel(self) -> int:
        return self.__nivel

    def mostrar_itens(self):
        itens = ''
        for item in self.__mochila:
            itens = itens + '\n' + item
        return itens
