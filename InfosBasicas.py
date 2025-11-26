import networkx as nx
import matplotlib.pyplot as plt

#Entre com o dataset que preferir
G = nx.read_edgelist("powergrid.edgelist.txt", nodetype=int)

print("Numero de vertices:", G.number_of_nodes())
print("Numero de arestas:", G.number_of_edges())
print("Conexo?", nx.is_connected(G))
print("Numero de componentes conectados:", nx.number_connected_components(G))

# calcula o grau dos vertices
graus = [d for n, d in G.degree()]
print("Grau medio:", sum(graus) / len(graus))

# imprime os vertices com maior grau(potencial distribuidores da rede)
top5 = sorted(G.degree, key=lambda x: x[1], reverse=True)[:5]
print("Top 5 vertices com maior grau:")
for n, d in top5:
    print(f"Vertice {n} -> grau {d}")