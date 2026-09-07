import heapq
import json
import random

# a cidade eh fixa, cada esquina é um no (com cordenadas x,y pra organizar no front)
NOS = [
    # linha 0
    {"id": 1, "x": 100, "y": 100},
    {"id": 2, "x": 250, "y": 100},
    {"id": 3, "x": 400, "y": 100},
    {"id": 4, "x": 550, "y": 100},
    {"id": 5, "x": 700, "y": 100},
    {"id": 6, "x": 850, "y": 100},
    {"id": 7, "x": 1000, "y": 100},
    {"id": 8, "x": 1150, "y": 100},
    # linha 1
    {"id": 9, "x": 100, "y": 250},
    {"id": 10, "x": 250, "y": 250},
    {"id": 11, "x": 400, "y": 250},
    {"id": 12, "x": 550, "y": 250},
    {"id": 13, "x": 700, "y": 250},
    {"id": 14, "x": 850, "y": 250},
    {"id": 15, "x": 1000, "y": 250},
    {"id": 16, "x": 1150, "y": 250},
    # linha 2
    {"id": 17, "x": 100, "y": 400},
    {"id": 18, "x": 250, "y": 400},
    {"id": 19, "x": 400, "y": 400},
    {"id": 20, "x": 550, "y": 400},
    {"id": 21, "x": 700, "y": 400},
    {"id": 22, "x": 850, "y": 400},
    {"id": 23, "x": 1000, "y": 400},
    {"id": 24, "x": 1150, "y": 400},
    # linha 3
    {"id": 25, "x": 100, "y": 550},
    {"id": 26, "x": 250, "y": 550},
    {"id": 27, "x": 400, "y": 550},
    {"id": 28, "x": 550, "y": 550},
    {"id": 29, "x": 700, "y": 550},
    {"id": 30, "x": 850, "y": 550},
    {"id": 31, "x": 1000, "y": 550},
    {"id": 32, "x": 1150, "y": 550},
]

# tamanho da tela
LAYOUT = {"width": 1250, "height": 650}

# ja que a cidade numa muda as ruas tambem nao
# tem ruas entre todos os nos
RUAS = [
    # ruas horizontais
    (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8),
    (9, 10), (10, 11), (11, 12), (12, 13), (13, 14), (14, 15), (15, 16),
    (17, 18), (18, 19), (19, 20), (20, 21), (21, 22), (22, 23), (23, 24),
    (25, 26), (26, 27), (27, 28), (28, 29), (29, 30), (30, 31), (31, 32),
    # ruas verticais
    (1, 9), (9, 17), (17, 25),
    (2, 10), (10, 18), (18, 26),
    (3, 11), (11, 19), (19, 27),
    (4, 12), (12, 20), (20, 28),
    (5, 13), (13, 21), (21, 29),
    (6, 14), (14, 22), (22, 30),
    (7, 15), (15, 23), (23, 31),
    (8, 16), (16, 24), (24, 32),
]

# custo fixo da rua normal.
PESO_RUA_NORMAL = 1

# dicionario com os tipos de obstaculo e o peso de cada um.
# pra pegar o peso de um obstaculo, e so fazer OBSTACULOS["tornado"] -> 7
OBSTACULOS = {
    "tornado": 7,
    "óleo": 5,
    "pregos": 3,
    "lama": 8,
}


def sortear_labels(qtd, semente):
    # essa funcao devolve uma lista com "qtd" labels: metade "normal" e
    # a outra metade um obstaculo sorteado.

    # random.seed(numero) faz os sorteios ficarem sempre iguais toda vez
    # que o programa roda (sem isso, o resultado mudaria a cada execucao).
    random.seed(semente)

    qnt_normal = qtd // 2
    qnt_obstruida = qtd - qnt_normal

    # comeca a lista so com as ruas normais.
    labels = ["normal"] * qnt_normal

    # pega so os NOMES do dicionario, sem os pesos.
    # ["tornado", "óleo", "pregos", "lama"]
    nomes_dos_obstaculos = list(OBSTACULOS.keys())

    # pra cada rua obstruida que falta, sorteia um nome da lista acima.
    for _ in range(qnt_obstruida):
        # random.choice(lista) devolve UM item aleatorio dessa lista.
        
        obstaculo_sorteado = random.choice(nomes_dos_obstaculos)
        labels.append(obstaculo_sorteado)

    # random.shuffle(lista) embaralha a lista, trocando a ordem dos itens
    random.shuffle(labels)

    return labels


def criar_arestas(semente=42):

    # chama a funcao pra gerar as labels
    labels = sortear_labels(len(RUAS), semente)

    arestas = []
    #zip junta o 1 da primeira lista com 1 da segunda lista, 2 com 2, etc
    for (a, b), label in zip(RUAS, labels):
        if label == "normal":
            peso = PESO_RUA_NORMAL
        else:
            # label aqui e "tornado" ou "óleo", entao busca o peso dele
            # dentro do dicionario OBSTACULOS.
            peso = OBSTACULOS[label]

        arestas.append({
            "source": a,
            "target": b,
            "label": label,
            "peso": peso,
        })
    return arestas


# quanto mais longe (em numero de arestas) partida e chegada tem que estar
# uma da outra pro sorteio aceitar o par
DISTANCIA_MINIMA_ARESTAS = 6


def construir_lista_adjacencia(arestas):
    # pra cada no, guarda uma lista de (vizinho, peso) -- o grafo nao e
    # direcionado, entao toda aresta entra dos dois lados.
    adjacencia = {no["id"]: [] for no in NOS}
    for aresta in arestas:
        a, b, peso = aresta["source"], aresta["target"], aresta["peso"]
        adjacencia[a].append((b, peso))
        adjacencia[b].append((a, peso))
    return adjacencia


def distancia_em_arestas(adjacencia, origem):
    # bfs sem peso: numero minimo de ruas pra sair de "origem" ate cada no.
    # serve so pra saber o quao "longe" dois pontos estao um do outro,
    # sem levar os obstaculos em conta (isso quem faz e o dijkstra).
    distancias = {origem: 0}
    fila = [origem]
    while fila:
        atual = fila.pop(0)
        for vizinho, _peso in adjacencia[atual]:
            if vizinho not in distancias:
                distancias[vizinho] = distancias[atual] + 1
                fila.append(vizinho)
    return distancias


def sortear_partida_chegada(adjacencia, semente=None):
    # sorteia dois nos garantindo que fiquem a pelo menos
    # DISTANCIA_MINIMA_ARESTAS ruas de distancia um do outro.
    rng = random.Random(semente)
    ids = [no["id"] for no in NOS]

    while True:
        partida = rng.choice(ids)
        chegada = rng.choice(ids)
        if partida == chegada:
            continue

        distancias = distancia_em_arestas(adjacencia, partida)
        if distancias[chegada] >= DISTANCIA_MINIMA_ARESTAS:
            return partida, chegada


def dijkstra(adjacencia, origem, destino):
    # caminho minimo (considerando o peso/custo de cada rua, obstaculos
    # inclusos) de "origem" ate "destino" usando uma fila de prioridade.
    distancias = {no: float("inf") for no in adjacencia}
    distancias[origem] = 0
    anterior = {}
    visitados = set()

    fila = [(0, origem)]
    while fila:
        custo_atual, atual = heapq.heappop(fila)

        if atual in visitados:
            continue
        visitados.add(atual)

        if atual == destino:
            break

        for vizinho, peso in adjacencia[atual]:
            novo_custo = custo_atual + peso
            if novo_custo < distancias[vizinho]:
                distancias[vizinho] = novo_custo
                anterior[vizinho] = atual
                heapq.heappush(fila, (novo_custo, vizinho))

    # reconstroi o caminho voltando de destino ate origem pelos "anterior"
    caminho = [destino]
    while caminho[-1] != origem:
        caminho.append(anterior[caminho[-1]])
    caminho.reverse()

    return caminho, distancias[destino]


def main():
    # o sorteio de partida/chegada e o dijkstra rodam no navegador (ver
    # layout-rascunho.html), pra cada jogador que abrir a pagina receber um
    # desafio novo sem precisar rodar esse script de novo. aqui em python
    # essas mesmas funcoes servem so pra testar/validar a logica antes de
    # portar pra js -- por isso o resultado abaixo e so impresso, nao vai
    # pro dados.js.
    arestas = criar_arestas()
    adjacencia = construir_lista_adjacencia(arestas)
    partida, chegada = sortear_partida_chegada(adjacencia)
    caminho, custo_total = dijkstra(adjacencia, partida, chegada)

    grafo = {
        "layout": LAYOUT,
        "nos": NOS,
        "arestas": arestas,
    }

    # joga no js
    with open("dados.js", "w", encoding="utf-8") as f:
        f.write("const dadosDoGrafo = ")
        f.write(json.dumps(grafo, ensure_ascii=False, indent=2))
        f.write(";\n")

    print("dados.js gerado com sucesso.")
    print(f"[teste python] partida: {partida} | chegada: {chegada}")
    print(f"[teste python] caminho minimo (dijkstra): {caminho}")
    print(f"[teste python] custo total: {custo_total}")


if __name__ == "__main__":
    main()
