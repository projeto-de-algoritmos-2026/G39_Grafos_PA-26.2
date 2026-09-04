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


def main():
    grafo = {
        "layout": LAYOUT,
        "nos": NOS,
        "arestas": criar_arestas(),
    }

    # joga no js
    with open("dados.js", "w", encoding="utf-8") as f:
        f.write("const dadosDoGrafo = ")
        f.write(json.dumps(grafo, ensure_ascii=False, indent=2))
        f.write(";\n")

    print("dados.js gerado com sucesso.")


if __name__ == "__main__":
    main()
