import json

def load_documents():
    """
    Charge les documents à partir du fichier 'documents.json'.

    Returns:
        list: La liste des documents représentés sous forme de dictionnaires avec des clés telles que 'id', 'title', et 'url'.
    """
    with open('documents.json', 'r', encoding='utf-8') as file:
        return json.load(file)

if __name__ == "__main__":
    # Exemple d'utilisation
    documents_example = load_documents()
    # print("Exemple de documents chargés :", documents_example)
    # print(documents_example[0])
    # Accéder au premier élément du dictionnaire (index 0)
    first_document = documents_example[0]
    # Parcourir chaque clé-valeur dans le dictionnaire
    for key, value in first_document.items():
        print(f"Clé: {key}, Valeur: {value}, Type de la valeur: {type(value)}")
