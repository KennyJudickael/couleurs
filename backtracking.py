import matplotlib.pyplot as plt
import random
import networkx as nx


def generer_graphe_aleatoire(nombre_de_sommets, probabilite_arrete):
    G = nx.erdos_renyi_graph(nombre_de_sommets, probabilite_arrete)
    return G


def est_valide(sommet, couleur, coloration, graph):
    for voisin in graph.neighbors(sommet):
        if coloration[voisin] == couleur:
            return False
    return True


def coloration_backtracking(graph, nombre_de_couleurs):
    def backtrack(sommet):
        if sommet == nombre_de_sommets:
            return True

        for couleur in range(1, nombre_de_couleurs + 1):
            if est_valide(sommet, couleur, coloration, graph):
                coloration[sommet] = couleur
                if backtrack(sommet + 1):
                    return True
                coloration[sommet] = 0

        return False

    nombre_de_sommets = len(graph)
    coloration = [0] * nombre_de_sommets
    if backtrack(0):
        print("Solution trouvée :")
        for sommet, couleur in enumerate(coloration):
            print(f"Sommet {sommet + 1} : Couleur {couleur}")

        couleurs = [
            random.choice(["r", "g", "b", "y", "m", "c"])
            for _ in range(nombre_de_couleurs)
        ]
        positions = nx.spring_layout(graph)

        plt.figure(figsize=(8, 6))
        for sommet, couleur in enumerate(coloration):
            plt.scatter(
                positions[sommet][0],
                positions[sommet][1],
                s=100,
                c=couleurs[couleur - 1],
                label=f"Sommet {sommet + 1}",
            )

        for edge in graph.edges():
            plt.plot(
                [positions[edge[0]][0], positions[edge[1]][0]],
                [positions[edge[0]][1], positions[edge[1]][1]],
                color="k",
            )

        plt.legend()
        plt.title("Coloration du graphe")
        plt.show()
    else:
        print("Aucune solution trouvée.")


nombre_de_sommets = int(input("Entrez le nombre de sommets : "))
nombre_de_couleurs = int(input("Entrez le nombre de couleurs : "))

graph = generer_graphe_aleatoire(nombre_de_sommets, 0.3)
coloration_backtracking(graph, nombre_de_couleurs)
