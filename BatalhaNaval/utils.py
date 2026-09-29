"""Funcoes utilitarias: entrada segura, coordenadas, tempo e JSON."""
import json
import re
from pathlib import Path

TAMANHO = 10
COLUNAS = "ABCDEFGHIJ"
DATA_DIR = Path(__file__).resolve().parent / "data"


class SairPartida(Exception):
    """Sinaliza que o jogador quer abandonar a partida atual."""


def ler_entrada(prompt):
    """Le uma linha do teclado; encerra com elegancia em Ctrl+D."""
    try:
        return input(prompt).strip()
    except EOFError:
        print("\nEntrada encerrada. Ate logo!")
        raise SystemExit(0)


def ler_opcao(prompt, validas):
    """Repete a leitura ate o usuario digitar uma das opcoes validas."""
    while True:
        texto = ler_entrada(prompt).upper()
        if texto in validas:
            return texto
        print("Opcao invalida. Opcoes: " + ", ".join(validas) + ".")


def parse_coordenada(texto):
    """Converte 'C5' em (linha, coluna) com indices a partir de 0.

    Levanta ValueError com mensagem explicativa se for invalida (RN01).
    """
    limpo = texto.strip().upper().replace(" ", "")
    achado = re.fullmatch(r"([A-Z])(\d{1,2})", limpo)
    if not achado:
        raise ValueError("Formato invalido. Use Letra + Numero, ex.: C5.")
    coluna = COLUNAS.find(achado.group(1))
    linha = int(achado.group(2)) - 1
    if coluna < 0 or not 0 <= linha < TAMANHO:
        raise ValueError("Fora do tabuleiro. Use colunas A-J e linhas 1-10.")
    return linha, coluna


def formatar_coordenada(posicao):
    """Converte (linha, coluna) em texto como 'C5'."""
    linha, coluna = posicao
    return f"{COLUNAS[coluna]}{linha + 1}"


def formatar_tempo(segundos):
    """Formata segundos como HH:MM:SS."""
    segundos = int(segundos)
    horas, resto = divmod(segundos, 3600)
    minutos, segs = divmod(resto, 60)
    return f"{horas:02d}:{minutos:02d}:{segs:02d}"


def limpar_tela():
    """Limpa o terminal (ANSI, funciona em Linux)."""
    print("\033[H\033[J", end="")


def carregar_json(nome_arquivo, padrao):
    """Carrega JSON da pasta data/; devolve o padrao se falhar."""
    caminho = DATA_DIR / nome_arquivo
    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError, OSError):
        return padrao


def salvar_json(nome_arquivo, dados):
    """Salva dados em JSON na pasta data/."""
    try:
        DATA_DIR.mkdir(exist_ok=True)
        caminho = DATA_DIR / nome_arquivo
        with open(caminho, "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=2)
    except OSError as erro:
        print(f"Aviso: nao foi possivel salvar {nome_arquivo} ({erro}).")
