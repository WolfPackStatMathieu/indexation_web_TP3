import json

from load_documents import load_documents
from load_index import load_index
from rank_documents import rank_documents

def save_ranked_documents_to_json(ranked_doc_ids, documents, file_name="results.json"):
    """
    Enregistre une liste de documents classés au format JSON.

    Parameters:
        ranked_doc_ids (list): Liste des identifiants de documents classés par pertinence.
        documents (list): Liste originale de tous les documents disponibles.
        file_name (str): Nom du fichier JSON de sortie.
    """
    # Préparer la liste des documents avec les informations requises
    results = []
    for doc_id in ranked_doc_ids:
        # Trouver le document correspondant dans la liste de documents
        doc = next((doc for doc in documents if doc['id'] == doc_id), None)
        if doc is not None:
            # Ajouter le titre et l'URL du document à la liste des résultats
            results.append({"Titre": doc['title'], "Url": doc['url']})

    # Écrire les résultats dans un fichier JSON
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=4)

    print(f"Les documents classés ont été enregistrés dans {file_name}")

# Exemple d'utilisation
if __name__ == "__main__":
    # Supposons que ranked_documents soit la liste des ID de documents classés obtenue précédemment
    documents = load_documents()  # Chargez vos documents ici
    index = load_index()  # Chargez votre index ici
    query = "danse classique"
    ranked_doc_ids = rank_documents(documents, query, index)

    # Enregistrez les documents classés dans un fichier JSON
    save_ranked_documents_to_json(ranked_doc_ids, documents)
