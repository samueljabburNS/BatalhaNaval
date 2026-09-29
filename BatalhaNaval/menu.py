"""Menus e telas de texto (RF01, RF09, RF07)."""
from utils import ler_entrada, ler_opcao

LINHA = "=" * 50
TRACO = "-" * 50


def menu_principal():
    print(LINHA)
    print("BATALHA NAVAL - GPTECH GAMES")
    print(LINHA)
    print("1. Nova partida")
    print("2. Ver estatisticas")
    print("3. Assistir replay da ultima partida")
    print("4. Creditos")
    print("5. Sair")
    print(TRACO)
    return ler_opcao("Escolha uma opcao: ", ("1", "2", "3", "4", "5"))


def selecionar_modo():
    """Devolve 1 (vs computador), 2 (dois jogadores) ou 0 (voltar)."""
    print("\nSelecione o modo de jogo:")
    print("[1] Jogador vs Computador")
    print("[2] Dois Jogadores")
    print("[0] Voltar ao menu")
    return int(ler_opcao(">> ", ("0", "1", "2")))


def creditos():
    print(LINHA)
    print("CREDITOS")
    print(LINHA)
    print("Batalha Naval - GPTech Games")
    print("Trabalho 1 - Programacao em Python - CEFET-MG Divinopolis")
    print("Desenvolvimento: Samuel")


def pausar(mensagem="Pressione ENTER para continuar..."):
    ler_entrada(mensagem)


def fim_de_jogo(vencedor, jogadas, tempo):
    """Tela final (mockup 6.5). Devolve '1' replay, '2' nova, '3' menu."""
    print(LINHA)
    print("FIM DE JOGO")
    print(LINHA)
    print(f"Vencedor: {vencedor}")
    print(f"Total de jogadas: {jogadas}")
    print(f"Tempo de partida: {tempo}")
    print(TRACO)
    print("[1] Ver replay [2] Nova partida [3] Menu principal")
    return ler_opcao("Escolha uma opcao: ", ("1", "2", "3"))
