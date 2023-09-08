import random
import numpy as np
import matplotlib.pyplot as plt


def generer_carre_magique(N):
    carre = np.zeros((N, N), dtype=int)
    valeurs = list(range(1, N**2 + 1))
    random.shuffle(valeurs)

    for i in range(N):
        for j in range(N):
            carre[i][j] = valeurs.pop()

    return carre


def evaluer_carre_magique(carre):
    N = len(carre)
    somme_magique = N * (N**2 + 1) // 2

    lignes = [sum(carre[i, :]) for i in range(N)]
    colonnes = [sum(carre[:, j]) for j in range(N)]
    diagonale_principale = sum(carre[i, i] for i in range(N))
    diagonale_secondaire = sum(carre[i, N - 1 - i] for i in range(N))

    distances = (
        [abs(somme_magique - ligne) for ligne in lignes]
        + [abs(somme_magique - colonne) for colonne in colonnes]
        + [
            abs(somme_magique - diagonale_principale),
            abs(somme_magique - diagonale_secondaire),
        ]
    )

    return sum(distances)


def croisement(carre1, carre2):
    N = len(carre1)
    point_de_crossover = random.randint(1, N**2 - 1)

    carre_enfant = np.zeros((N, N), dtype=int)
    valeurs_enfant = []

    for i in range(N):
        for j in range(N):
            if i * N + j < point_de_crossover:
                carre_enfant[i][j] = carre1[i][j]
                valeurs_enfant.append(carre1[i][j])
            else:
                carre_enfant[i][j] = carre2[i][j]
                valeurs_enfant.append(carre2[i][j])

    return carre_enfant


def mutation(carre, probabilite_mutation):
    N = len(carre)
    for i in range(N):
        for j in range(N):
            if random.random() < probabilite_mutation:
                valeurs_possibles = list(
                    set(range(1, N**2 + 1)) - set(carre[i, :]) - set(carre[:, j])
                )
                carre[i][j] = random.choice(valeurs_possibles)

    return carre


def algorithme_genetique(N, taille_population, generations, probabilite_mutation):
    population = [generer_carre_magique(N) for _ in range(taille_population)]

    for generation in range(generations):
        scores = [evaluer_carre_magique(carre) for carre in population]
        meilleurs_indices = np.argsort(scores)
        meilleurs_individus = [
            population[i] for i in meilleurs_indices[: int(0.2 * taille_population)]
        ]

        enfants = []
        while len(enfants) < taille_population:
            parent1, parent2 = random.choices(meilleurs_individus, k=2)
            enfant = croisement(parent1, parent2)
            enfant = mutation(enfant, probabilite_mutation)
            enfants.append(enfant)

        population = enfants

    meilleur_carre = population[meilleurs_indices[0]]
    return meilleur_carre


def afficher_carre_magique(carre):
    N = len(carre)

    plt.figure(figsize=(6, 6))
    plt.imshow(
        carre, cmap="YlGnBu", interpolation="nearest"
    )  # Utilisation d'une carte de couleurs pour représenter les valeurs
    plt.colorbar()

    for i in range(N):
        for j in range(N):
            plt.text(
                j,
                i,
                str(carre[i][j]),
                va="center",
                ha="center",
                color="black",
                fontsize=12,
            )

    plt.title("Carré Magique")
    plt.axis("off")  # Désactive les axes
    plt.show()


# Taille du carré magique (par exemple, 3x3)
N = int(
    input("Entrez la taille du carré magique (par exemple, 3 pour un carré 3x3) : ")
)
taille_population = 100
generations = 100
probabilite_mutation = 0.1

meilleur_carre_magique = algorithme_genetique(
    N, taille_population, generations, probabilite_mutation
)
print("Carré magique généré par l'algorithme génétique :")
afficher_carre_magique(meilleur_carre_magique)
