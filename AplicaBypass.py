import networkx as nx

TOP_K = 50            # quantidade de vértices mais críticos a tratar
LIMIT_PER_NODE = 1     # quantas novas arestas será adicionada por vértice crítico

INPUT_FILE = "powergrid.edgelist.txt" #Entre com o dataset que preferir
OUTPUT_FILE = "powergrid_bypass.edgelist.txt"


def aplica_bypass():
    print("Carregando grafo...")
    G = nx.read_edgelist(INPUT_FILE, nodetype=int)
    print(f"Grafo carregado: {G.number_of_nodes()} vertices, {G.number_of_edges()} arestas\n")

    print("Calculando intermediacao...")
    bet = nx.betweenness_centrality(G)

    # seleciona os TOP_K vértices mais críticos
    top = sorted(bet.items(), key=lambda x: x[1], reverse=True)[:TOP_K]
    top_vertices = [n for n, _ in top]
    print(f"Selecionados {len(top_vertices)} vertices mais criticos para bypass.\n")

    # aplica o bypass
    for v in top_vertices:
        vizinhos = list(G.neighbors(v))
        # prioriza vizinhos com maior grau
        vizinhos = sorted(vizinhos, key=lambda x: G.degree(x), reverse=True)

        adicionadas = 0
        for i in range(len(vizinhos)):
            if adicionadas >= LIMIT_PER_NODE:
                break
            for j in range(i+1, len(vizinhos)):
                u = vizinhos[i]
                w = vizinhos[j]

                if not G.has_edge(u, w):
                    G.add_edge(u, w)
                    adicionadas += 1

                    if adicionadas >= LIMIT_PER_NODE:
                        break

        print(f"Vertice {v}: {adicionadas} novas arestas adicionadas.")

    # gera o dataset com as alterações
    nx.write_edgelist(G, OUTPUT_FILE, data=False)
    print(f"\nBypass concluido! Arquivo salvo como '{OUTPUT_FILE}'")

aplica_bypass()