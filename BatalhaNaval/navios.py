"""Definicao dos navios (RF03)."""

TIPOS_NAVIO = {"pequeno": 2, "grande": 4}
FROTA_PADRAO = ["grande", "grande", "pequeno", "pequeno", "pequeno"]


class Navio:
    """Um navio com suas posicoes e as posicoes ja atingidas."""

    def __init__(self, tipo, posicoes):
        self.tipo = tipo
        self.posicoes = list(posicoes)
        self.atingidas = set()

    @property
    def tamanho(self):
        return len(self.posicoes)

    @property
    def afundado(self):
        """RN03: afundado quando todas as posicoes foram atingidas."""
        return len(self.atingidas) == self.tamanho

    def registrar_tiro(self, posicao):
        """Marca o tiro; devolve True se acertou o navio."""
        if posicao in self.posicoes:
            self.atingidas.add(posicao)
            return True
        return False


def gerar_posicoes(tipo, linha, coluna, horizontal):
    """Lista as posicoes que um navio ocuparia a partir de (linha, coluna)."""
    tamanho = TIPOS_NAVIO[tipo]
    if horizontal:
        return [(linha, coluna + i) for i in range(tamanho)]
    return [(linha + i, coluna) for i in range(tamanho)]
