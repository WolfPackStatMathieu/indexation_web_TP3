from tokenize_query import tokenize_query


def search_documents(query, documents, index):
    """
    Recherche les documents correspondants à une requête en utilisant un index de position des tokens.

    Parameters:
        query (str): La requête de l'utilisateur.
        documents (list): La liste des documents représentés sous forme de dictionnaires avec des clés telles que 'id', 'title', et 'url'.
        index (dict): L'index des positions des tokens dans les documents.

    Returns:
        set: Un ensemble des identifiants des documents qui correspondent à tous les tokens de la requête.
    """
    # Tokeniser la requête de l'utilisateur
    tokens = tokenize_query(query)

    # Initialiser l'ensemble des documents correspondants avec tous les documents disponibles
    matching_documents = set(str(doc['id']) for doc in documents)

    # Parcourir chaque token de la requête
    for token in tokens:
        # Vérifier si le token est présent dans l'index
        if token in index:
            # Mettre à jour l'ensemble des documents correspondants en ne conservant que ceux ayant le token actuel
            matching_documents &= set(str(doc_id) for doc_id in index[token].keys())

    # Renvoyer l'ensemble final des documents correspondants à la requête
    return matching_documents

if __name__ == "__main__":
    # Exemple d'utilisation
    documents_example = [
        {"id": 0, "title": "Document 1", "url": "https://example.com/1"},
        {"id": 1, "title": "Document 2", "url": "https://example.com/2"},
        # Ajoutez d'autres documents au besoin
    ]

    index_example = {
        "token1": {"0": {"positions": [0], "count": 1}, "1": {"positions": [3], "count": 1}},
        "token2": {"0": {"positions": [5], "count": 1}, "1": {"positions": [8], "count": 1}},
        # Ajoutez d'autres tokens et positions au besoin
    }

    query_example = "token2"
    result = search_documents(query_example, documents_example, index_example)

    print("Documents correspondants :", result)
