#!/usr/bin/env python3
#
# script name: fluxo_intencao.py
# author: Stefanyvitoria
# description: This script represent a "flux and intention" problem.
# The flux are the possible paths for go from INI to FIM and the 
# intention is reduce the time for it.

import networkx as nx
import matplotlib.pyplot as plt
import sys

def main(graph_path):
    # Cria um grafo direcionado
    G = nx.DiGraph()

    #lê o arquivo de configuração do grafo
    file = open(graph_path, "r")
    lines = file.readlines()


    # Adiciona as arestas com os valores onde
    # Cada nó representa uma rua e cada aresta representa
    # uma conexão entre ruas e o peso da aresta é o tempo
    # necessário para percorrer de uma rua a outra
    try: 
        for line in lines:
            line =line.strip().split(" ")
            no_ori, no_dest, edge_value = line[0], line[2], int(line[4])
            G.add_edge(no_ori, no_dest, weight=edge_value)
    except:
        print(f"Graph file Error, check if your file is correct.")
        print("""The graph file has to be exactly like the template below,
        where each line will represent an edge in the graph:
        <no source> -> <no destination> = <threshold value>
        <no source> -> <no destination> = <threshold value>
        ...""")
        exit(2)

    # Calcula o menor caminho usando o algoritmo de Dijkstra
    shortest_path = nx.dijkstra_path(G, 'INI', 'FIM', weight='weight')

    # Obtém as posições dos nós para um layout de plotagem
    pos = nx.spring_layout(G)

    # Obtém os valores das arestas
    edge_labels = nx.get_edge_attributes(G, 'weight')

    # Plota o grafo e as labels das arestas
    nx.draw_networkx(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=12)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)

    time = 0

    # Percorre todas as arestas do grafo e define a cor
    for no_ori, no_dest, edge_value  in G.edges(data=True):
        # Verifica se a aresta pertence ao caminho mais curto
        if no_ori in shortest_path and no_dest in shortest_path:
            # Define a cor das arestas do caminho mais curto como vermelho e a espessura como 2
            edge_color = 'red'
            edge_width = 2
            time += edge_value["weight"]
        else:
            # Define a cor das outras arestas como preto e a espessura como 1
            edge_color = 'black'
            edge_width = 1
        # Desenha a aresta com os atributos definidos
        nx.draw_networkx_edges(G, pos, edgelist=[(no_ori, no_dest)], width=edge_width, edge_color=edge_color)

    # Exibe o menor caminho
    print(f"O Menor caminho é: {shortest_path}")
    print(f"O custo em tempo é: {time}")

    # Exibe o plot
    plt.axis('off')
    plt.show()

if __name__ == '__main__':
    graph_path = "./graph.txt"

    print("\nStart script.")

    if (len(sys.argv) == 1):
        print("Graph path no passed, using path default...")
        print(f"graph path = {graph_path}")

    elif (('-file' in sys.argv) and len(sys.argv) > 2):
        graph_path = sys.argv[2]
        print("Graph path passed.")
        print(f"graph path = {graph_path}")
    
    elif ('-help' in sys.argv):
        print("""The graph file has to be exactly like the template below,
        where each line will represent an edge in the graph:
        <no source> -> <no destination> = <threshold value>
        <no source> -> <no destination> = <threshold value>
        ...""")
        exit(0)

    else:
        print("Params incorrect.")
        print("Usage: python ./fluxo_intencao.py -file <graph file name>.txt")
        print("       python ./fluxo_intencao.py -help")
        exit(1)

    main(graph_path)

    print("Script Done!")
    exit(0)
