import networkx as nx

#Entre com o dataset que preferir
G = nx.read_edgelist("powergrid.edgelist.txt", nodetype=int)

print("Numero de vertices:", G.number_of_nodes())
print("Numero de arestas:", G.number_of_edges())
print("A rede e conexa?", nx.is_connected(G))

# CENTRALIDADE DE INTERMEDIACAO (Betweenness)
print("\nCalculando centralidade de intermediacao...")
centralidade_intermediacao = nx.betweenness_centrality(G, normalized=True)

top_inter = sorted(centralidade_intermediacao.items(), key=lambda x: x[1], reverse=True)[:10]

print("\nTOP 10 vertices por intermediacao:")
for vertice, valor in top_inter:
    print(f"Vertice {vertice} -> intermediacao = {valor:.5f}")


# CENTRALIDADE DE PROXIMIDADE (Closeness)
print("\nCalculando centralidade de proximidade...")
centralidade_proximidade = nx.closeness_centrality(G)

top_prox = sorted(centralidade_proximidade.items(), key=lambda x: x[1], reverse=True)[:10]

print("\nTOP 10 vertices por proximidade:")
for vertice, valor in top_prox:
    print(f"Vertice {vertice} -> proximidade = {valor:.5f}")

# CENTRALIDADE DE AUTOVETOR (Eigenvector)
print("\nCalculando centralidade por autovetor...")
centralidade_autovetor = nx.eigenvector_centrality(G, max_iter=500)

top_auto = sorted(centralidade_autovetor.items(), key=lambda x: x[1], reverse=True)[:10]

print("\nTOP 10 vertices por autovetor:")
for vertice, valor in top_auto:
    print(f"Vertice {vertice} -> autovetor = {valor:.5f}")

# PONTOS DE ARTICULACAO (Articulation Points)
print("\nDetectando vertices criticos (pontos de articulacao)...")
pontos_criticos = list(nx.articulation_points(G))

print("Primeiros 10 vertices criticos:", pontos_criticos[:10])

# ARESTAS CRITICAS (Bridges)
print("\nDetectando arestas criticas (bridges)...")
arestas_criticas = list(nx.bridges(G))

print("Primeiras 10 arestas criticas:")
print(arestas_criticas[:10])

# SIMULACAO DE FALHA DOS PRINCIPAIS NOS
def simular_falha(grafo, vertices_remover):
    H = grafo.copy()
    H.remove_nodes_from(vertices_remover)

    num_componentes = nx.number_connected_components(H)
    maior_componente = len(max(nx.connected_components(H), key=len))

    return num_componentes, maior_componente
