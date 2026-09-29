# Arquitetura

`main` orquestra `menu`, `jogador`/`computador`, `tabuleiro`, `estatisticas`
e `replay`. `Computador` herda de `Jogador` e sobrescreve o posicionamento
e a escolha de jogadas. `utils` concentra E/S segura e JSON.
