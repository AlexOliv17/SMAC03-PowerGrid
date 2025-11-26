import igraph as ig
import random

def carregar_grafo():
    print("Carregando grafo original...")
    arestas = []
    with open("powergrid.edgelist.txt", "r") as f: #Entre com o dataset que preferir
        for line in f:
            u, v = map(int, line.split())
            arestas.append((u, v))

    vertices = set()
    for u, v in arestas:
        vertices.add(u)
        vertices.add(v)

    G = ig.Graph()
    G.add_vertices(max(vertices) + 1)
    G.add_edges(arestas)

    print(f"Grafo carregado: {G.vcount()} vertices, {G.ecount()} arestas")
    return G


def augmentacao_resiliente(G, num_add=300):
    print("\nCalculando metricas estruturais...")

    grau = G.degree()
    avg_grau = sum(grau) / len(grau)

    inter = G.betweenness()
    med_inter = sorted(inter)[len(inter)//2]

    cluster = G.transitivity_local_undirected(mode="zero")

    print("Selecionando vertices perifericos de interesse...")

    perifericos = [
        v for v in range(G.vcount())
        if grau[v] <= avg_grau and inter[v] <= med_inter and cluster[v] < 0.05
    ]

    print(f"Total de vertices perifericos elegiveis: {len(perifericos)}")

    candidatos = []

    print("\nGerando candidatos de pares perifericos...")
    for _ in range(num_add * 20):
        u, v = random.sample(perifericos, 2)

        if G.are_adjacent(u, v):
            continue

        d = G.distances(u, v)[0][0]

        count = 0

        # arestas longas
        count += min(d, 10)

        # Penaliza vértices próximos de hubs
        count -= inter[u] * 0.1
        count -= inter[v] * 0.1

        # regiões vulneráveis
        count += (0.1 - cluster[u])
        count += (0.1 - cluster[v])

        candidatos.append((count, u, v))

    print(f"Candidatos gerados: {len(candidatos)}")
    candidatos.sort(reverse=True)

    print("\nSelecionando arestas para augmentacao...")
    adicionadas = 0
    nova_lista = []

    for count, u, v in candidatos:
        if adicionadas >= num_add:
            break
        if not G.are_adjacent(u, v):
            G.add_edge(u, v)
            nova_lista.append((u, v))
            adicionadas += 1

    print(f"Arestas realmente adicionadas: {adicionadas}")
    return G, nova_lista


def salvar_grafo(G):
    with open("powergrid_augmentacao.edgelist.txt", "w") as f:
        for u, v in G.get_edgelist():
            f.write(f"{u} {v}\n")
    print("\nGrafo salvo como powergrid_augmentacao.edgelist.txt")

G = carregar_grafo()
G2, add = augmentacao_resiliente(G, num_add=300)
salvar_grafo(G2)