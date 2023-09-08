import matplotlib.pyplot as plt
import random

def coloration_graphique(graph):
    def est_valide(sommet, couleur, coloration):
        for voisin in graph[sommet]:
            if coloration[voisin] == couleur:
                return False
        return True

    def coloration_util(sommet, coloration, nombre_de_couleurs):
        if sommet == len(graph):
            return True

        for couleur in range(1, nombre_de_couleurs + 1):
            if est_valide(sommet, couleur, coloration):
                coloration[sommet] = couleur
                if coloration_util(sommet + 1, coloration, nombre_de_couleurs):
                    return True
                coloration[sommet] = 0

    nombre_de_sommets = len(graph)
    coloration = [0] * nombre_de_sommets
    nombre_de_couleurs = 3  # Vous pouvez ajuster le nombre de couleurs ici

    if coloration_util(0, coloration, nombre_de_couleurs):
        print("Solution trouvée :")
        for sommet, couleur in enumerate(coloration):
            print(f"Sommet {sommet + 1} : Couleur {couleur}")

        # Création du graphique
        couleurs = [random.choice(['r', 'g', 'b', 'y', 'm', 'c']) for _ in range(nombre_de_couleurs)]
        positions = [(random.random(), random.random()) for _ in range(nombre_de_sommets)]

        plt.figure(figsize=(8, 6))
        for sommet, position, couleur in zip(range(nombre_de_sommets), positions, coloration):
            plt.scatter(position[0], position[1], s=100, c=couleurs[couleur - 1], label=f"Sommet {sommet + 1}")
        
        # Ajout des lignes de liaison entre les sommets reliés
        for sommet, voisins in enumerate(graph):
            for voisin in voisins:
                plt.plot([positions[sommet][0], positions[voisin][0]], [positions[sommet][1], positions[voisin][1]], color='k')

        plt.legend()
        plt.title("Coloration du graphe")
        plt.show()
    else:
        print("Aucune solution trouvée.")

# Exemple de graphe représenté par une liste d'adjacence
graph = [
    [1, 2, 4],  # Sommet 0 est relié à 1, 2 et 4
    [0, 2, 3],  # Sommet 1 est relié à 0, 2 et 3
    [0, 1, 4],  # Sommet 2 est relié à 0, 1 et 4
    [1],        # Sommet 3 est relié à 1
    [0, 2]      # Sommet 4 est relié à 0 et 2
]

coloration_graphique(graph)
