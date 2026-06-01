# Backtracking — Algoritmos Avançados

Exercícios práticos de backtracking implementados em Python, cobrindo quatro problemas clássicos da técnica.

## Exercícios

### 1. Permutações de uma String
Gera todas as permutações possíveis de uma string usando backtracking com controle de índices usados.

**Entrada:** `"ABC"`  
**Saída:** `['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA']`

---

### 2. Subconjuntos com Soma Alvo
Encontra todos os subconjuntos de uma lista de inteiros cuja soma é igual a um valor alvo. Inclui comparativo de estados visitados com e sem poda.

**Entrada:** `nums = [1, 2, 3, 4, 5]`, `alvo = 5`  
**Saída:** `[[1, 4], [2, 3], [5]]`

---

### 3. N-Rainhas (4×4)
Resolve o problema das N-Rainhas para um tabuleiro 4×4, retornando todas as soluções válidas com impressão visual do tabuleiro.

**Saída (2 soluções):**

. Q . .       . . Q .
. . . Q       Q . . .
Q . . .       . . . Q
. . Q .       . Q . .

---

### 4. Sudoku 4×4
Resolve um Sudoku 4×4 via backtracking com verificação de linha, coluna e bloco 2×2. Exibe o número de chamadas recursivas realizadas.

**Tabuleiro inicial:**

[1, 0, 0, 4]
[0, 4, 1, 0]
[2, 0, 0, 3]
[4, 0, 0, 1]

---

## Como executar

Requer Python 3.10 ou superior.

    python backtracking.py

## Estrutura

    .
    └── backtracking.py   # todos os exercícios em um único arquivo

## Autores

- José Lucas Andrade Fonseca
- Sidney Cardoso de Oliveira Junior

## Disciplina

Algoritmos Avançados — Engenharia de Software
