"""search_documents commence 
par créer un ensemble pour chaque token de la requête 
qui contient les ID des documents où le token apparaît.
Ensuite, elle utilise set.intersection pour trouver 
l'intersection de tous ces ensembles, ce qui garantit 
que seuls les documents contenant tous les tokens de la 
requête sont conservés. Si aucun token de la requête 
n'est trouvé dans l'index, la fonction retourne un ensemble 
vide, indiquant qu'aucun document ne correspond à la requête.
"""
from tokenize_query import tokenize_query

def search_documents(query, documents, index):
    """
    Recherche les documents correspondants à une requête en utilisant un index de position des tokens,
    en s'assurant que tous les tokens de la requête sont présents dans les documents.

    Parameters:
        query (str): La requête de l'utilisateur.
        documents (list): La liste des documents représentés sous forme de dictionnaires avec des clés telles que 'id', 'title', et 'url'.
        index (dict): L'index des positions des tokens dans les documents.

    Returns:
        set: Un ensemble des identifiants des documents qui correspondent à tous les tokens de la requête.
    """
    tokens = tokenize_query(query)
    
    # Utiliser un ensemble pour stocker les ID de documents correspondant à chaque token
    token_doc_ids = [set(index[token].keys()) for token in tokens if token in index]

    # Trouver l'intersection de tous ces ensembles pour s'assurer que tous les tokens sont présents
    if token_doc_ids:
        matching_documents = set.intersection(*token_doc_ids)
    else:
        # Si aucun token n'est trouvé dans l'index, aucun document ne correspond
        matching_documents = set()

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

    query_example = "token1 token2"
    result = search_documents(query_example, documents_example, index_example)

    print("Documents correspondants :", result)
