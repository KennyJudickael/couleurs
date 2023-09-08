import matplotlib.pyplot as plt
import random
import networkx as nx  # Pour la génération du graphe aléatoire


def generer_graphe_aleatoire(nombre_de_sommets, probabilite_arrete):
    G = nx.erdos_renyi_graph(nombre_de_sommets, probabilite_arrete)
    return G


def coloration_graphique(nombre_de_sommets, nombre_de_couleurs):
    graph = generer_graphe_aleatoire(
        nombre_de_sommets, 0.3
    )  # Modifier la probabilité d'arête selon vos besoins

    def est_valide(sommet, couleur, coloration):
        for voisin in graph.neighbors(sommet):
            if coloration[voisin] == couleur:
                return False
        return True

    def coloration_util(sommet, coloration, nombre_de_couleurs):
        if sommet == nombre_de_sommets:
            return True

        for couleur in range(1, nombre_de_couleurs + 1):
            if est_valide(sommet, couleur, coloration):
                coloration[sommet] = couleur
                if coloration_util(sommet + 1, coloration, nombre_de_couleurs):
                    return True
                coloration[sommet] = 0

    coloration = [0] * nombre_de_sommets

    if coloration_util(0, coloration, nombre_de_couleurs):
        print("Solution trouvée :")
        for sommet, couleur in enumerate(coloration):
            print(f"Sommet {sommet + 1} : Couleur {couleur}")

        # Création du graphique
        couleurs = [
            random.choice(["r", "g", "b", "y", "m", "c"])
            for _ in range(nombre_de_couleurs)
        ]
        positions = nx.spring_layout(
            graph
        )  # Utilisez un algorithme de placement pour positionner les nœuds

        plt.figure(figsize=(8, 6))
        for sommet, couleur in enumerate(coloration):
            plt.scatter(
                positions[sommet][0],
                positions[sommet][1],
                s=100,
                c=couleurs[couleur - 1],
                label=f"Sommet {sommet + 1}",
            )

        # Ajout des lignes de liaison entre les sommets reliés
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


# Demander à l'utilisateur de saisir le nombre de sommets et le nombre de couleurs
nombre_de_sommets = int(input("Entrez le nombre de sommets : "))
nombre_de_couleurs = int(input("Entrez le nombre de couleurs : "))

coloration_graphique(nombre_de_sommets, nombre_de_couleurs)
