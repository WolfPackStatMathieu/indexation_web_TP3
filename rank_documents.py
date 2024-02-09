from tokenize_query import tokenize_query


def rank_documents(documents, query, index):
    """
    Classe les documents par pertinence en fonction d'une requête, en utilisant une fonction de ranking linéaire
    basée sur la fréquence des tokens et leur position moyenne dans les documents.

    Parameters:
        documents (list): La liste des documents chargés par load_documents.
        query (str): La requête de l'utilisateur.
        index (dict): L'index des positions des tokens dans les documents, chargé par load_index.

    Returns:
        list: Une liste d'identifiants de documents ordonnés par leur score de pertinence.
    """
    query_tokens = tokenize_query(query)
    scores = {} # initialisation des scores

    for doc in documents: # pour chaque document filtré
        doc_id = str(doc['id'])
        doc_score = 0
        
        # on cherche un par un dans les tokens issus de la requete
        # ex: query_tokens = ['loi']
        for token in query_tokens: 
            # Si le token est présent parmi les token indexes et que l'id du
            # document est présent dans le dictionnaire du token
            # ex: '137' in index['loi'] ==> True
            # 'loi' est dans l'index et '137' est un doc_id contenu dans le 
            # dictionnaire  "index['loi']"
            if token in index and doc_id in index[token]:
                # récupération des données pour ce token dans ce document
                token_data = index[token][doc_id]
                # >>> index['loi']['137']
                # {'positions': [4], 'count': 1} 
                # le token 'loi' est présent à la position 4, 1 fois dans le document
                freq_score = token_data['count']
                # Inverse de la position moyenne
                pos_score = 1 / (1 + sum(token_data['positions']) / len(token_data['positions']))  
                # Ajustez ces poids en fonction de votre analyse sur leur importance relative
                doc_score += 0.7 * freq_score + 0.3 * pos_score
        # Création d'une entrée dans le dictionnaire scores={doc_id:, doc_score:}
        scores[doc_id] = doc_score

    # Trier les documents par leur score de pertinence en ordre décroissant
    ranked_doc_ids = sorted(scores, key=scores.get, reverse=True)

    # Convertir les identifiants de documents en entiers, si nécessaire, et les retourner
    return [int(doc_id) for doc_id in ranked_doc_ids if scores[doc_id] > 0]

from tokenize_query import tokenize_query
from load_documents import load_documents
from load_index import load_index

if __name__ == "__main__":
    # Charger les documents et l'index à partir de fichiers JSON ou d'une autre source
    documents = load_documents()  # Supposons que cette fonction retourne une liste de dictionnaires de documents
    index = load_index()  # Supposons que cette fonction retourne un dictionnaire représentant l'index

    # Définir une requête de test
    query = "exemple de requête"

    # Appeler rank_documents pour obtenir les documents classés par pertinence
    ranked_documents = rank_documents(documents, query, index)

    # Afficher les résultats
    print("Documents classés par pertinence :")
    for doc_id in ranked_documents:
        print(f"ID du document: {doc_id}")
        # Vous pouvez également afficher d'autres détails du document, comme le titre, si vous le souhaitez
        print(f"Titre: {next(doc for doc in documents if doc['id'] == doc_id)['title']}")
