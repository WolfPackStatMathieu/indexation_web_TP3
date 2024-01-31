import json

def load_index():
    """
    Charge l'index à partir du fichier 'title_pos_index.json'.

    Returns:
        dict: L'index des positions des tokens dans les documents.
    """
    with open('title_pos_index.json', 'r', encoding='utf-8') as file:
        return json.load(file)

if __name__ == "__main__":
    # Exemple d'utilisation
    index_example = load_index()
    # print("Exemple d'index chargé :", index_example)
    
    # Accéder au premier élément du dictionnaire (par exemple, le dernier token de l'index)
    last_token = list(index_example.keys())[-1]
    print(index_example[last_token].items())
    # Parcourir chaque clé-valeur dans le dictionnaire correspondant au dernier token
    for key, value in index_example[last_token].items():
        print(f"Clé: {key}, Valeur: {value}, Type de la valeur: {type(value)}")
