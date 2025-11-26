import networkx as nx

LIMIT_POR_ARESTAP = 1  # quantas novas conexões criar por arestas pontes
INPUT_FILE = "powergrid.edgelist.txt" #Entre com o dataset que preferir
OUTPUT_FILE = "powergrid_redundancia.edgelist.txt"

def aplica_redundancia():
    print("Carregando grafo...")
    G = nx.read_edgelist(INPUT_FILE, nodetype=int)
    print(f"Grafo carregado: {G.number_of_nodes()} vertices, {G.number_of_edges()} arestas\n")

    print("Detectando arestas-ponte...")
    arestas_pontes = list(nx.bridges(G))
    print(f"Arestas-pontes encontradas: {len(arestas_pontes)}\n")

    total_add = 0
    # Para cada aresta-ponte, tentamos criar até LIMIT_POR_ARESTAP arestas alternativas
    for (u, v) in arestas_pontes:
        nu = [x for x in G.neighbors(u) if x != v]
        nv = [x for x in G.neighbors(v) if x != u]

        # ordenar candidatos por grau de forma decrescente
        nu_sorted = sorted(nu, key=lambda x: G.degree(x), reverse=True)
        nv_sorted = sorted(nv, key=lambda x: G.degree(x), reverse=True)

        add = 0
        for a in nu_sorted:
            if add >= LIMIT_POR_ARESTAP:
                break
            for b in nv_sorted:
                if add >= LIMIT_POR_ARESTAP:
                    break
                if a == b:
                    continue
                if not G.has_edge(a, b):
                    G.add_edge(a, b)
                    add += 1
                    total_add += 1
        if add > 0:
            print(f"Bridge ({u},{v}): adicionadas {add} arestas entre vizinhos.")

    # salvar resultado
    nx.write_edgelist(G, OUTPUT_FILE, data=False)
    print(f"\nRedundancia concluida! Total de arestas adicionadas: {total_add}")
    print(f"Arquivo salvo como '{OUTPUT_FILE}'")

aplica_redundancia()