# Exercicio 1 - Permutacoes de uma string

def permutacoes(s: str) -> list[str]:
    resultado = []
    usados = set()
    atual = []

    def backtrack():
        # se o tamanho atual bateu com o da string, achei uma permutacao
        if len(atual) == len(s):
            resultado.append("".join(atual))
            return

        for i in range(len(s)):
            if i in usados:
                continue
            # escolhe o caractere
            usados.add(i)
            atual.append(s[i])

            backtrack()

            # desfaz a escolha (backtrack)
            atual.pop()
            usados.remove(i)

    backtrack()
    return resultado


# teste exercicio 1
print("=== Exercicio 1 - Permutacoes ===")
print(permutacoes("ABC"))
print()


# Exercicio 2 - Subconjuntos com soma alvo

def subconjuntos_soma(nums: list[int], alvo: int) -> list[list[int]]:
    resultado = []
    estados_sem_poda = [0]
    estados_com_poda = [0]

    def backtrack(inicio, atual, soma):
        estados_com_poda[0] += 1

        if soma == alvo:
            resultado.append(atual[:])
            return

        for i in range(inicio, len(nums)):
            # poda: se a soma ja passou do alvo, nao continua
            if soma + nums[i] > alvo:
                continue

            atual.append(nums[i])
            backtrack(i + 1, atual, soma + nums[i])
            atual.pop()

    # conta sem poda pra comparar
    def backtrack_sem_poda(inicio, atual, soma):
        estados_sem_poda[0] += 1

        if soma == alvo:
            return

        for i in range(inicio, len(nums)):
            atual.append(nums[i])
            backtrack_sem_poda(i + 1, atual, soma + nums[i])
            atual.pop()

    backtrack(0, [], 0)
    backtrack_sem_poda(0, [], 0)

    print(f"  Estados visitados COM poda: {estados_com_poda[0]}")
    print(f"  Estados visitados SEM poda: {estados_sem_poda[0]}")

    return resultado


# teste exercicio 2
print("=== Exercicio 2 - Subconjuntos com soma ===")
nums = [1, 2, 3, 4, 5]
alvo = 5
print(f"  nums = {nums}, alvo = {alvo}")
print(f"  Resultado: {subconjuntos_soma(nums, alvo)}")
print()


# Exercicio 3 - N-Rainhas (4x4)

def n_rainhas(n: int) -> list[list[int]]:
    resultado = []
    colunas = set()
    diag_positiva = set()  # linha + coluna
    diag_negativa = set()  # linha - coluna

    solucao = []

    def backtrack(linha):
        if linha == n:
            resultado.append(solucao[:])
            return

        for col in range(n):
            # verifica se a posicao ta segura
            if col in colunas or (linha + col) in diag_positiva or (linha - col) in diag_negativa:
                continue

            # coloca a rainha
            colunas.add(col)
            diag_positiva.add(linha + col)
            diag_negativa.add(linha - col)
            solucao.append(col)

            backtrack(linha + 1)

            # tira a rainha (backtrack)
            solucao.pop()
            colunas.remove(col)
            diag_positiva.remove(linha + col)
            diag_negativa.remove(linha - col)

    backtrack(0)
    return resultado


def imprimir_tabuleiro(solucao, n):
    for linha in range(n):
        row = ""
        for col in range(n):
            if solucao[linha] == col:
                row += "Q "
            else:
                row += ". "
        print("  " + row)
    print()


# teste exercicio 3
print("=== Exercicio 3 - N-Rainhas ===")
solucoes = n_rainhas(4)
for i, sol in enumerate(solucoes, start=1):
    print(f"  Solucao {i}: {sol}")
    imprimir_tabuleiro(sol, 4)
print()


# Exercicio 4 - Sudoku 4x4

def encontrar_vazia(tabuleiro):
    for i in range(4):
        for j in range(4):
            if tabuleiro[i][j] == 0:
                return (i, j)
    return None


def valido(tabuleiro, linha, col, num):
    # checa a linha
    if num in tabuleiro[linha]:
        return False

    # checa a coluna
    for i in range(4):
        if tabuleiro[i][col] == num:
            return False

    # checa o bloco 2x2
    bloco_linha = (linha // 2) * 2
    bloco_col = (col // 2) * 2
    for i in range(bloco_linha, bloco_linha + 2):
        for j in range(bloco_col, bloco_col + 2):
            if tabuleiro[i][j] == num:
                return False

    return True


chamadas_recursivas = [0]

def resolver_sudoku(tabuleiro: list[list[int]]) -> bool:
    chamadas_recursivas[0] += 1

    vazia = encontrar_vazia(tabuleiro)
    if vazia is None:
        return True  # resolveu, nao tem mais celula vazia

    linha, col = vazia

    for num in range(1, 5):
        if valido(tabuleiro, linha, col, num):
            tabuleiro[linha][col] = num

            if resolver_sudoku(tabuleiro):
                return True

            # nao deu certo, desfaz (backtrack)
            tabuleiro[linha][col] = 0

    return False


# teste exercicio 4
print("=== Exercicio 4 - Sudoku 4x4 ===")
tabuleiro = [
    [1, 0, 0, 4],
    [0, 4, 1, 0],
    [2, 0, 0, 3],
    [4, 0, 0, 1],
]

print("  Tabuleiro inicial:")
for linha in tabuleiro:
    print(f"  {linha}")
print()

if resolver_sudoku(tabuleiro):
    print("  Tabuleiro resolvido:")
    for linha in tabuleiro:
        print(f"  {linha}")
    print(f"\n  Chamadas recursivas: {chamadas_recursivas[0]}")
else:
    print("  Sem solucao")
