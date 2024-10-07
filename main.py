#### Imports et définition des variables globales
"""Voici le début de code de Salem Jana"""

import csv

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """

    with open (filename,mode='r',encoding='utf8') as f :
        r = csv.reader(f, delimiter=';') #lire fichier ligne par ligne
        l = [[int(J) for J in ligne] for ligne in r] # Convertir ligne/l
        return l



def get_list_k(data, k):
    """get-list"""
    if 0 <= k < len(data): # Vérifiez valididité de k
        return data[k]

    return None




def get_first(l):
    """1ere element de la liste"""
    if l :             # vérification que l n'est pas vide
        return l[0]
    return None


def get_last(l):
    """get_last"""
    if l:
        return l[-1]
    return None


def get_max(l):
    """het max"""
    if l:
        return max(l)
    return None



def get_min(l):
    """get min"""
    if l:
        return min(l)
    return None



def get_sum(l):
    """get sum"""
    if l:
        return sum(l)
    return None



#### Fonction principale


def main():
    """main"""
    data = read_data(FILENAME)
    for i, l in enumerate(data):
        print(i, l)

    k = 37  # Change cet index pour tester d'autres valeurs
    if k < len(data):
        print(f"Liste à l'index {k}: {get_list_k(data, k)}")
    else:
        print(f"L'index {k} est hors limites, il n'y a que {len(data)} lignes dans le fichier.")


if __name__ == "__main__":
    main()
