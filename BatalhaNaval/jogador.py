"""Jogador humano: posicionamento (RF10) e jogadas (RF05, RN02)."""
from navios import FROTA_PADRAO
from tabuleiro import Tabuleiro
from utils import (SairPartida, ler_entrada, ler_opcao, parse_coordenada)


class Jogador:
    """Jogador humano com seu tabuleiro e contadores."""

    def __init__(self, nome):
        self.nome = nome
        self.tabuleiro = Tabuleiro()
        self.tiros = 0
        self.acertos = 0

    def registrar_resultado(self, posicao, resultado):
        """Atualiza contadores apos uma jogada."""
        self.tiros += 1
        if resultado != "agua":
            self.acertos += 1

    def escolher_jogada(self, tabuleiro_adversario):
        """Pede uma jogada valida; repeticao nao consome a rodada (RN02)."""
        while True:
            texto = ler_entrada(
                f"{self.nome}, sua jogada (ex.: C5, 0 = menu): ")
            if texto.upper() in ("0", "MENU"):
                raise SairPartida
            try:
                posicao = parse_coordenada(texto)
            except ValueError as erro:
                print(erro)
                continue
            if tabuleiro_adversario.ja_jogada(posicao):
                print("Voce ja jogou nessa posicao! Escolha outra, essa "
                      "jogada nao conta como rodada.")
                continue
            return posicao

    def posicionar_frota(self):
        """Posiciona e confere os navios antes da partida (RF10)."""
        self.tabuleiro.posicionar_automaticamente()
        while True:
            print(f"\nFrota de {self.nome}:")
            self.tabuleiro.exibir(mostrar_navios=True)
            print("\n[1] Confirmar  [2] Sortear novamente  "
                  "[3] Posicionar manualmente")
            opcao = ler_opcao(">> ", ("1", "2", "3"))
            if opcao == "1":
                return
            if opcao == "2":
                self.tabuleiro.posicionar_automaticamente()
            else:
                self._posicionar_manualmente()

    def _posicionar_manualmente(self):
        self.tabuleiro.limpar()
        for tipo in FROTA_PADRAO:
            while True:
                self.tabuleiro.exibir(mostrar_navios=True)
                texto = ler_entrada(
                    f"Posicao inicial do navio {tipo} (ex.: C5): ")
                try:
                    linha, coluna = parse_coordenada(texto)
                except ValueError as erro:
                    print(erro)
                    continue
                sentido = ler_opcao(
                    "[H] Horizontal ou [V] Vertical? ", ("H", "V"))
                try:
                    self.tabuleiro.posicionar_navio(
                        tipo, linha, coluna, sentido == "H")
                    break
                except ValueError as erro:
                    print(erro)
