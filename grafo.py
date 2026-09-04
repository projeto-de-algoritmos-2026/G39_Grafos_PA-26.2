import json
import random

# a cidade eh fixa, cada esquina é um no (com cordenadas x,y pra organizar no front)
NOS = [
    {"id": "A", "x": 100, "y": 100},
    {"id": "B", "x": 250, "y": 100},
    {"id": "C", "x": 400, "y": 100},
    {"id": "D", "x": 550, "y": 100},
    {"id": "E", "x": 100, "y": 250},
    {"id": "F", "x": 250, "y": 250},
    {"id": "G", "x": 400, "y": 250},
    {"id": "H", "x": 550, "y": 250},
    {"id": "I", "x": 100, "y": 400},
    {"id": "J", "x": 250, "y": 400},
    {"id": "K", "x": 400, "y": 400},
    {"id": "L", "x": 550, "y": 400},
]

# tamanho da tela
LAYOUT = {"width": 650, "height": 500}

# ja que a cidade numa muda as ruas tambem nao
# tem ruas entre todos os nos
RUAS = [
    # ruas horizontais
    ("A", "B"), ("B", "C"), ("C", "D"),
    ("E", "F"), ("F", "G"), ("G", "H"),
    ("I", "J"), ("J", "K"), ("K", "L"),
    # ruas verticais
    ("A", "E"), ("E", "I"),
    ("B", "F"), ("F", "J"),
    ("C", "G"), ("G", "K"),
    ("D", "H"), ("H", "L"),
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
    # a outra metade um obstaculo sorteado (tornado ou óleo).

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
