#!/usr/bin/env python3
#
# script name: tranformacao_linear.py
# author: Stefanyvitoria
# description: This script represent an example of linear
# transformation using a matrix from escal.
# Context: This script is necessary for users view different
# sizes of cube in virtual mode.


import numpy as np
import matplotlib.pyplot as plt
import math
import sys

def main(scale_factor_x, scale_factor_y, scale_factor_z):

    # Matriz de escala 3D
    matriz = np.array([
        [scale_factor_x, 0, 0, 0],
        [0, scale_factor_y, 0, 0],
        [0, 0, scale_factor_z, 0],
        [0, 0, 0, 1]
    ])

    # Definição dos pontos do cubo de volume 1
    pontos = np.array([
    [0, 0, 0, 1],   # Vértice 1
    [1, 0, 0, 1],   # Vértice 2
    [1, 1, 0, 1],   # Vértice 3
    [0, 1, 0, 1],   # Vértice 4
    [0, 0, 1, 1],   # Vértice 5
    [1, 0, 1, 1],   # Vértice 6
    [1, 1, 1, 1],   # Vértice 7
    [0, 1, 1, 1]    # Vértice 8
    ])

    # Aplicando a matriz de transformação aos pontos do cubo
    pontos_transformados = np.dot(pontos, matriz.T)

    # Plotando o cubo
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Definir proporção igual nos três eixos
    ax.set_box_aspect([1, 1, 1])

    # Desenho das arestas do cubo
    edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),  # Arestas da base
    (4, 5), (5, 6), (6, 7), (7, 4),  # Arestas da face superior
    (0, 4), (1, 5), (2, 6), (3, 7)   # Arestas conectando as bases
    ]

    colors = ['red', 'green', 'black', 'blue']

    for i, edge in enumerate(edges):
        ax.plot3D(
            [pontos_transformados[edge[0], 0], pontos_transformados[edge[1], 0]],
            [pontos_transformados[edge[0], 1], pontos_transformados[edge[1], 1]],
            [pontos_transformados[edge[0], 2], pontos_transformados[edge[1], 2]],
            colors[i%4]
        )

    # Configurações adicionais do gráfico
    ax.set_xlabel('Eixo X')
    ax.set_ylabel('Eixo Y')
    ax.set_zlabel('Eixo Z')


    # Definir proporção igual nos três eixos
    ax.set_box_aspect([np.ptp(pontos_transformados[:, 0]), np.ptp(pontos_transformados[:, 1]), np.ptp(pontos_transformados[:, 2])])


    plt.show()

if __name__ == '__main__':
    # Escalas
    scale_factor_x = 1
    scale_factor_y = 1
    scale_factor_z = 1

    print("\nStart script.")

    if (len(sys.argv) == 1):
        print("Control no passed, using control value default...")

    else:
        if (('-x' in sys.argv) and len(sys.argv) > 2):
            i = sys.argv.index("-x") +1
            scale_factor_x = sys.argv[i]
            print("Control -x passed.")

        if (('-y' in sys.argv) and len(sys.argv) > 2):
            i = sys.argv.index("-y") +1
            scale_factor_y = sys.argv[i]
            print("Control -y passed.")

        if (('-z' in sys.argv) and len(sys.argv) > 2):
            i = sys.argv.index("-z") +1
            scale_factor_z = sys.argv[i]
            print("Control -x passed.")

    print(f"control -x = {scale_factor_x}")
    print(f"control -y = {scale_factor_y}")
    print(f"control -z = {scale_factor_z}")

    main(
        scale_factor_x=float(scale_factor_x),
        scale_factor_y=float(scale_factor_y),
        scale_factor_z=float(scale_factor_z)
    )

    print("Script Done.")