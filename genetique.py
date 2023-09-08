import matplotlib.pyplot as plt
import random
import networkx as nx
import numpy as np


def generer_graphe_aleatoire(nombre_de_sommets, probabilite_arrete):
    G = nx.erdos_renyi_graph(nombre_de_sommets, probabilite_arrete)
    return G


def evaluer_coloration(graph, coloration):
    conflits = 0
    for sommet in graph.nodes():
        for voisin in graph.neighbors(sommet):
            if coloration[sommet] == coloration[voisin]:
                conflits += 1
    return conflits


def algorithme_genetique(
    nombre_de_sommets, nombre_de_couleurs, taille_population, generations
):
    graph = generer_graphe_aleatoire(nombre_de_sommets, 0.3)
    population = np.random.randint(
        1, nombre_de_couleurs + 1, size=(taille_population, nombre_de_sommets)
    )

    for generation in range(generations):
        scores = [evaluer_coloration(graph, individu) for individu in population]
        meilleurs_indices = np.argsort(scores)[: int(0.2 * taille_population)]
        meilleurs_individus = [population[i] for i in meilleurs_indices]

        enfants = []
        while len(enfants) < taille_population:
            parent1, parent2 = random.choices(meilleurs_individus, k=2)
            point_de_crossover = random.randint(1, nombre_de_sommets - 1)
            enfant = np.concatenate(
                (parent1[:point_de_crossover], parent2[point_de_crossover:])
            )
            mutations = random.sample(range(nombre_de_sommets), k=random.randint(1, 3))
            for mutation in mutations:
                enfant[mutation] = random.randint(1, nombre_de_couleurs)
            enfants.append(enfant)

        population = np.array(enfants)

    meilleur_individu = population[np.argmin(scores)]
    return meilleur_individu


def coloration_graphique(nombre_de_sommets, nombre_de_couleurs):
    meilleur_individu = algorithme_genetique(
        nombre_de_sommets, nombre_de_couleurs, taille_population=50, generations=100
    )
    graph = generer_graphe_aleatoire(nombre_de_sommets, 0.3)

    print("Solution trouvée :")
    for sommet, couleur in enumerate(meilleur_individu):
        print(f"Sommet {sommet + 1} : Couleur {couleur}")

    couleurs = [
        random.choice(["r", "g", "b", "y", "m", "c"]) for _ in range(nombre_de_couleurs)
    ]
    positions = nx.spring_layout(graph)

    plt.figure(figsize=(8, 6))
    for sommet, couleur in enumerate(meilleur_individu):
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


nombre_de_sommets = int(input("Entrez le nombre de sommets : "))
nombre_de_couleurs = int(input("Entrez le nombre de couleurs : "))

coloration_graphique(nombre_de_sommets, nombre_de_couleurs)
