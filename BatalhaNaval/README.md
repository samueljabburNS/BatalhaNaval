# Batalha Naval - GPTech Games

Trabalho 1 - Programacao em Python (Engenharia de Computacao, CEFET-MG
Divinopolis). Jogo de Batalha Naval em modo texto, Python 3.10+, Linux.

## Como executar

```bash
git clone <link-do-repositorio>
cd BatalhaNaval
python3 main.py
```

Nao ha dependencias externas (apenas biblioteca padrao).

## Como jogar

- Coordenadas no formato Letra + Numero (`C5`), colunas A-J, linhas 1-10.
- Durante a partida, digite `0` ou `menu` para abandonar e voltar ao menu.
- Legenda: `~` agua nao jogada | `N` navio | `X` acerto | `O` agua jogada.
- Frota de cada jogador: 2 navios grandes (4 posicoes) e 3 pequenos (2).
- Antes de comecar, cada jogador confere a frota: confirmar, sortear de
  novo ou posicionar manualmente (H/V).
- Modo Dois Jogadores: o programa pede para passar o teclado entre as
  vezes, para o adversario nao ver o tabuleiro.
- Estatisticas consideram o Jogador 1 (nos dois modos).

## Estrutura

| Arquivo | Responsabilidade |
|---|---|
| `main.py` | Loop da partida e ponto de entrada |
| `menu.py` | Menus e telas |
| `tabuleiro.py` | Tabuleiro 10x10, posicionamento, tiros |
| `navios.py` | Classe `Navio`, tipos e frota |
| `jogador.py` | Jogador humano, entrada de jogadas e frota |
| `computador.py` | IA do computador |
| `estatisticas.py` | Estatisticas persistidas em `data/` |
| `replay.py` | Historico de jogadas e replay |
| `utils.py` | Entrada segura, coordenadas, tempo, JSON |

## Rastreabilidade dos requisitos

| Requisito | Onde |
|---|---|
| RF01 menu | `menu.menu_principal` |
| RF02 tabuleiro 10x10 | `tabuleiro.Tabuleiro` |
| RF03 navios pequeno/grande | `navios.TIPOS_NAVIO` |
| RF04 posicionamento automatico sem sobreposicao | `Tabuleiro.posicionar_automaticamente` |
| RF05 validacao de jogadas | `utils.parse_coordenada`, `Jogador.escolher_jogada` |
| RF06 agua/acerto/afundado | `main.mensagem_resultado` |
| RF07 fim de jogo (vencedor, jogadas, tempo) | `menu.fim_de_jogo` |
| RF08 nova partida pelo menu | `main.nova_partida` |
| RF09 dois modos | `menu.selecionar_modo`, `main.preparar_jogadores` |
| RF10 posicionar/conferir antes | `Jogador.posicionar_frota` |
| RF11 historico | `replay.registrar_jogada` |
| RF12 estatisticas | `estatisticas.py` |
| RF13 replay | `replay.reproduzir` |
| RN01-RN05 | `utils`, `Jogador`, `Navio.afundado`, `Tabuleiro.todos_afundados`, `Computador` |

## Decisoes de projeto


- Persistencia em JSON (`data/estatisticas.json`, `data/ultima_partida.json`).
- Jogada repetida e rejeitada sem consumir a rodada (RN02).
- A vez sempre alterna, mesmo apos acerto.
- IA do computador (bonus): varre em padrao de xadrez e, apos um acerto,
  ataca as casas vizinhas ate afundar o navio.
- Entradas invalidas e Ctrl+C / Ctrl+D sao tratados sem quebrar o programa.


 ## Video de demonstracao [Assista no YouTube](https://youtu.be/zT7a1DCt584)
