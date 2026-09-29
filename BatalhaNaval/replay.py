"""Historico de jogadas (RF11) e modo replay (RF13)."""
from utils import (carregar_json, formatar_coordenada, ler_entrada,
                   salvar_json)

ARQUIVO = "ultima_partida.json"
ROTULOS = {"agua": "Agua", "acerto": "Acerto", "afundado": "Afundado"}


def registrar_jogada(historico, jogador, posicao, resultado):
    """Adiciona uma jogada ao historico da partida em andamento."""
    historico.append({"jogador": jogador,
                      "coordenada": formatar_coordenada(posicao),
                      "resultado": resultado})


def salvar(historico, vencedor, tempo):
    salvar_json(ARQUIVO, {"vencedor": vencedor, "tempo": tempo,
                          "jogadas": historico})


def reproduzir():
    dados = carregar_json(ARQUIVO, None)
    if not dados or not dados.get("jogadas"):
        print("Nenhuma partida gravada para replay ainda.")
        return
    jogadas = dados["jogadas"]
    total = len(jogadas)
    print("Reproduzindo replay da ultima partida...")
    for numero, jogada in enumerate(jogadas, start=1):
        rotulo = ROTULOS.get(jogada["resultado"], jogada["resultado"])
        print(f"Jogada {numero:02d}/{total} - {jogada['jogador']} - "
              f"{jogada['coordenada']} - {rotulo}")
        if numero < total:
            resposta = ler_entrada("[ENTER] Proxima jogada "
                                   "[Q] Sair do replay ")
            if resposta.upper() == "Q":
                return
    print(f"Fim do replay. Vencedor: {dados['vencedor']}")
