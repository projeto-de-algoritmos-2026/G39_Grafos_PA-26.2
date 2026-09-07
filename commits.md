# Commits

### rascunho: 1
**autor:** Isabelle
Montagem do grafo com nós simples fixos, arestas fixas, e duas opcoes de peso (1 e 5) que são geradas de maneira aleatória sempre que o programa roda
A ideia é que cada no seja uma esquina da cidade, cada rua com peso 1 seja uma rua livre e cada rua com o peso 5 seja uma rua com um obstaculo

### tipos obstaculos
**autor:** Isabelle
Adicionei diferentes tipos de obstáculos igual ao jogo da polly (tornado, lama, pregos, óleo)
Como rodar - readme

### +nos e responsivo
**autor:** Isabelle
Mais nós no jogo e tela responsiva

### layout: rascunho
**autor:** Isabelle
Inicio de testes do layout e front tentando fazer parecer com o jogo da polly
apenas ruas e nos foram montados

### layout: faixa de pedestres
**autor:** Isabelle
ajuste da faixa de pedestres, commit para nao perder configuracoes

### layout: rua
**autor:** Isabelle
ajustes finais da rua

### layout: terreno
**autor:** Isabelle
adicionei terrenos padroes entre ruas
adicionei primeiras imagens na pasta imagens/canteiros para terrenos

### layout: +nos
**autor:** Isabelle
adicionei mais nos no layout

### layout: v1
**autor:** Isabelle
ajustei ruas, mudei o terreno para se adpatr melhor no computador


### grafo: geração programática
**autor:** Cibelly
1. Grafo agora é gerado por parâmetros (colunas, linhas) em vez de listas fixas. Grade 
mantida em 32 nós.

### layout: unificação com o grafo
**autor:** Cibelly
1. Layout deixou de ter grade própria e passou a ler direto do dados.js, mesmo arquivo 
gerado pelo grafo. Antes tinha 24 nós no layout e 32 no grafo, agora bate certinho.

### logica: dijkstra e sorteio em javascript
**autor:** Cibelly
2. Sorteio de partida/chegada e Dijkstra movidos de Python para JavaScript, rodando toda 
vez que a página abre. grafo.py agora só gera a cidade fixa (nos, arestas, pesos).

### layout: destaque do caminho minimo
**autor:** Cibelly
2. Adicionado destaque visual em layout-rascunho.html: caminho minimo em amarelo, partida 
em verde, chegada em vermelho. Cada F5 sorteia um desafio novo. 
comando para ver : xdg-open ~/G39_Grafos_PA-26.2/layout-rascunho.html

### lógica: dijkstra com pontos intermediários e desafios dinâmicos
**autor:** Cibelly
3. Implementado o fluxo de desafios com três pontos: Lila (partida) → Lea (ponto intermediário) → festa (chegada).
O sorteio agora garante uma distância mínima entre os pontos e o Dijkstra é executado duas vezes: no trecho Lila→Lea e no trecho Lea→festa, com o custo total calculado pela soma dos dois caminhos.

### jogo: movimento do carrinho e logica de vitoria
**autor:** Cibelly
Carrinho agora se move ao clicar nos nos vizinhos. Jogo tem 2 fases (Lila->Lea, 
Lea->festa) e ao chegar mostra o caminho percorrido comparado com o dijkstra (quanto 
ficou acima do otimo). //preciso arrumar pq ate agr elas só vao pra festa, e aparentemente tem mais lugares q não lembrava

### jogo: destino aleatorio e carro da lea seguindo
**autor:** Cibelly
Destino final agora e sorteado entre banco, parque, predio e quadra de esportes (exclusivo, 
nao repete em outro quarteirao). Carro da lea aparece ao encontrar a lila (roxo, via filtro 
css) e segue um no atras dela ate o destino. Removidas todas as referencias a "festa".

### docs: readme e identidade visual
**autor:** Cibelly
Criado README.md completo (sobre o jogo, grafo, dijkstra, instalacao, como jogar) e 
assets/banner.svg com ilustracao das casas da Lila e da Lea.