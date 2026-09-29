"""Ponto de entrada do jogo Batalha Naval."""
import time

import estatisticas
import menu
import replay
from computador import Computador
from jogador import Jogador
from utils import (SairPartida, formatar_coordenada, formatar_tempo,
                   limpar_tela)

MENSAGENS = {
    "agua": "Agua! Nenhum navio atingido nessa posicao.",
    "acerto": "Acerto! Voce atingiu um navio inimigo.",
}


def mensagem_resultado(resultado, navio):
    if resultado == "afundado":
        return (f"Navio afundado! Voce destruiu um navio {navio.tipo} "
                "do adversario.")
    return MENSAGENS[resultado]


def exibir_estado(atual, outro):
    print(f"\n--- Vez de {atual.nome} ---")
    print("Tabuleiro do adversario:")
    outro.tabuleiro.exibir(mostrar_navios=False)
    print("\nSeu tabuleiro:")
    atual.tabuleiro.exibir(mostrar_navios=True)


def preparar_jogadores(modo):
    jogador1 = Jogador("Jogador 1")
    jogador1.posicionar_frota()
    if modo == 1:
        jogador2 = Computador()
        jogador2.posicionar_frota()
    else:
        limpar_tela()
        menu.pausar("Passe o teclado ao Jogador 2 e pressione ENTER...")
        jogador2 = Jogador("Jogador 2")
        jogador2.posicionar_frota()
        limpar_tela()
        menu.pausar("Esconda a tela. ENTER para comecar...")
    return jogador1, jogador2


def jogar_partida(modo):
    """Executa uma partida completa. Devolve a opcao do fim de jogo."""
    jogador1, jogador2 = preparar_jogadores(modo)
    historico = []
    inicio = time.time()
    atual, outro = jogador1, jogador2
    while True:
        limpar_tela()
        if isinstance(atual, Jogador) and not isinstance(atual, Computador):
            exibir_estado(atual, outro)
        posicao = atual.escolher_jogada(outro.tabuleiro)
        resultado, navio = outro.tabuleiro.receber_tiro(posicao)
        atual.registrar_resultado(posicao, resultado)
        replay.registrar_jogada(historico, atual.nome, posicao, resultado)
        if isinstance(atual, Computador):
            print(f"\nComputador jogou em {formatar_coordenada(posicao)}: "
                  f"{resultado}.")
        else:
            print("\n" + mensagem_resultado(resultado, navio))
        if outro.tabuleiro.todos_afundados():
            break
        if modo == 2 or isinstance(atual, Computador):
            menu.pausar()
        atual, outro = outro, atual
    tempo = formatar_tempo(time.time() - inicio)
    replay.salvar(historico, atual.nome, tempo)
    estatisticas.registrar_partida(
        atual is jogador1, jogador1.tiros, jogador1.acertos)
    limpar_tela()
    return menu.fim_de_jogo(atual.nome, len(historico), tempo)


def nova_partida():
    """Fluxo de nova partida; permite encadear partidas (RF08)."""
    while True:
        modo = menu.selecionar_modo()
        if modo == 0:
            return
        try:
            opcao = jogar_partida(modo)
        except SairPartida:
            print("Partida abandonada. Voltando ao menu.")
            return
        if opcao == "1":
            replay.reproduzir()
            menu.pausar()
        elif opcao == "3":
            return


def main():
    try:
        while True:
            opcao = menu.menu_principal()
            if opcao == "1":
                nova_partida()
            elif opcao == "2":
                estatisticas.exibir()
            elif opcao == "3":
                replay.reproduzir()
            elif opcao == "4":
                menu.creditos()
            else:
                print("Ate a proxima!")
                break
    except KeyboardInterrupt:
        print("\nJogo encerrado.")


if __name__ == "__main__":
    main()
