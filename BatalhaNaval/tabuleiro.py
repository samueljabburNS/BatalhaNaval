"""Tabuleiro 10x10 (RF02), posicionamento (RF04) e tiros (RF05/RF06)."""
import random

from navios import FROTA_PADRAO, Navio, gerar_posicoes
from utils import COLUNAS, TAMANHO

AGUA, NAVIO, ACERTO, AGUA_JOGADA = "~", "N", "X", "O"


class Tabuleiro:
    """Guarda os navios de um jogador e os tiros recebidos."""

    def __init__(self):
        self.navios = []
        self.tiros = {}  # posicao -> "agua" | "acerto" | "afundado"

    def limpar(self):
        self.navios = []
        self.tiros = {}

    def _ocupadas(self):
        return {p for navio in self.navios for p in navio.posicoes}

    @staticmethod
    def dentro(posicao):
        linha, coluna = posicao
        return 0 <= linha < TAMANHO and 0 <= coluna < TAMANHO

    def posicionar_navio(self, tipo, linha, coluna, horizontal):
        """Posiciona um navio; ValueError se sair do tabuleiro ou colidir."""
        posicoes = gerar_posicoes(tipo, linha, coluna, horizontal)
        if not all(self.dentro(p) for p in posicoes):
            raise ValueError("O navio ultrapassa os limites do tabuleiro.")
        if any(p in self._ocupadas() for p in posicoes):
            raise ValueError("O navio se sobrepoe a outro navio.")
        self.navios.append(Navio(tipo, posicoes))

    def posicionar_automaticamente(self, frota=None):
        """Sorteia posicoes sem sobreposicao (RF04)."""
        frota = frota or FROTA_PADRAO
        self.limpar()
        for tipo in frota:
            while True:
                linha = random.randrange(TAMANHO)
                coluna = random.randrange(TAMANHO)
                horizontal = random.choice([True, False])
                try:
                    self.posicionar_navio(tipo, linha, coluna, horizontal)
                    break
                except ValueError:
                    continue

    def navio_em(self, posicao):
        for navio in self.navios:
            if posicao in navio.posicoes:
                return navio
        return None

    def ja_jogada(self, posicao):
        return posicao in self.tiros

    def receber_tiro(self, posicao):
        """Processa um tiro. Devolve (resultado, navio_atingido_ou_None)."""
        if not self.dentro(posicao):
            raise ValueError("Coordenada fora do tabuleiro.")
        if self.ja_jogada(posicao):
            raise ValueError("Essa posicao ja foi jogada.")
        navio = self.navio_em(posicao)
        if navio is None:
            self.tiros[posicao] = "agua"
            return "agua", None
        navio.registrar_tiro(posicao)
        resultado = "afundado" if navio.afundado else "acerto"
        self.tiros[posicao] = "acerto"
        return resultado, navio

    def todos_afundados(self):
        """RN04: todos os navios destruidos."""
        return bool(self.navios) and all(n.afundado for n in self.navios)

    def frota_completa(self):
        return len(self.navios) == len(FROTA_PADRAO)

    def renderizar(self, mostrar_navios):
        """Devolve o tabuleiro como texto (legenda do mockup 6.3)."""
        ocupadas = self._ocupadas()
        linhas = ["   " + " ".join(COLUNAS)]
        for i in range(TAMANHO):
            celulas = []
            for j in range(TAMANHO):
                pos = (i, j)
                if pos in self.tiros:
                    marca = ACERTO if self.tiros[pos] == "acerto" \
                        else AGUA_JOGADA
                elif mostrar_navios and pos in ocupadas:
                    marca = NAVIO
                else:
                    marca = AGUA
                celulas.append(marca)
            linhas.append(f"{i + 1:>2} " + " ".join(celulas))
        return "\n".join(linhas)

    def exibir(self, mostrar_navios):
        print(self.renderizar(mostrar_navios))
        print("Legenda: ~ agua nao jogada | N navio | X acerto | "
              "O agua jogada")
