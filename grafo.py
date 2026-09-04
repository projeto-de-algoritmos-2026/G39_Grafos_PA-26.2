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

# custofixo de cada tipo de rua.
# pra declarar se nessa rua tem obstaculo ou nao
PESO_RUA_NORMAL = 1
PESO_RUA_OBSTACULO = 5


def sortear_labels(qtd, semente):
    # sorteia pra quantidade de ruas labels metade NORMAL metade OBSTRUIDA
    random.seed(semente)
    metade = qtd // 2
    labels = ["normal"] * metade + ["obstruida"] * (qtd - metade)
    random.shuffle(labels)  # embaralha para nao seguir sempre a mesma ordem
    return labels


def criar_arestas(semente=42):

    # chama a funcao pra gerar as labels
    labels = sortear_labels(len(RUAS), semente)

    arestas = []
    #zip junta o 1 da primeira lista com 1 da segunda lista, 2 com 2, etc
    for (a, b), label in zip(RUAS, labels):
        peso = PESO_RUA_NORMAL if label == "normal" else PESO_RUA_OBSTACULO
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
