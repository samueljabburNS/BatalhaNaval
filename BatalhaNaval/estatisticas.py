"""Estatisticas de desempenho do Jogador 1 (RF12)."""
from utils import carregar_json, salvar_json

ARQUIVO = "estatisticas.json"


def _padrao():
    return {"partidas": 0, "vitorias": 0, "derrotas": 0,
            "tiros": 0, "acertos": 0}


def carregar():
    dados = _padrao()
    dados.update(carregar_json(ARQUIVO, {}))
    return dados


def aproveitamento(dados):
    """Percentual de tiros que acertaram navios."""
    if dados["tiros"] == 0:
        return 0.0
    return dados["acertos"] * 100 / dados["tiros"]


def registrar_partida(venceu, tiros, acertos):
    dados = carregar()
    dados["partidas"] += 1
    dados["vitorias" if venceu else "derrotas"] += 1
    dados["tiros"] += tiros
    dados["acertos"] += acertos
    salvar_json(ARQUIVO, dados)


def exibir():
    dados = carregar()
    print("=" * 50)
    print("ESTATISTICAS DO JOGADOR 1")
    print("=" * 50)
    print(f"Partidas jogadas: {dados['partidas']}")
    print(f"Vitorias: {dados['vitorias']}  Derrotas: {dados['derrotas']}")
    print(f"Tiros: {dados['tiros']}  Acertos: {dados['acertos']}")
    print(f"Aproveitamento: {aproveitamento(dados):.1f}%")
