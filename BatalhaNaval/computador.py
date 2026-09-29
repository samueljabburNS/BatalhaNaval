"""Adversario controlado pelo computador (RN05)."""
import random

from jogador import Jogador
from utils import TAMANHO


class Computador(Jogador):
    """IA simples: caca em xadrez e persegue vizinhos apos um acerto."""

    def __init__(self, nome="Computador"):
        super().__init__(nome)
        self.alvos = []

    def posicionar_frota(self):
        self.tabuleiro.posicionar_automaticamente()

    def escolher_jogada(self, tabuleiro_adversario):
        while self.alvos:
            posicao = self.alvos.pop(0)
            if not tabuleiro_adversario.ja_jogada(posicao):
                return posicao
        livres = [(i, j) for i in range(TAMANHO) for j in range(TAMANHO)
                  if not tabuleiro_adversario.ja_jogada((i, j))]
        # Navios tem >= 2 casas: basta varrer em padrao de xadrez.
        xadrez = [p for p in livres if (p[0] + p[1]) % 2 == 0]
        return random.choice(xadrez or livres)

    def registrar_resultado(self, posicao, resultado):
        super().registrar_resultado(posicao, resultado)
        if resultado == "afundado":
            self.alvos.clear()
        elif resultado == "acerto":
            linha, coluna = posicao
            vizinhos = [(linha - 1, coluna), (linha + 1, coluna),
                        (linha, coluna - 1), (linha, coluna + 1)]
            random.shuffle(vizinhos)
            for viz in vizinhos:
                if 0 <= viz[0] < TAMANHO and 0 <= viz[1] < TAMANHO:
                    self.alvos.append(viz)
