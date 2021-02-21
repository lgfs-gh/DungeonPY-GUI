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
