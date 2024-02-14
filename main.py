from load_documents import load_documents
from load_index import load_index
from rank_documents import rank_documents
from search_documents import search_documents

def main():
    # Charger les documents et l'index
    documents = load_documents()
    index = load_index()

    # Exemple de requête (commentez la ligne ci-dessus et décommentez la suivante pour une entrée utilisateur)
    user_query = input("Entrez votre requête : ")
    # user_query = "cannabis baron"
    
    # Rechercher les documents correspondants à la requête
    matching_documents = search_documents(user_query, documents, index)

    if matching_documents:
        print("Documents correspondants :")
        for doc_id_str in matching_documents:
            doc_id = int(doc_id_str)  # Convertir la chaîne en entier
            print(f"ID: {doc_id}, Titre: {documents[doc_id]['title']}, URL: {documents[doc_id]['url']}")
    else:
        print("Aucun document ne correspond à la requête.")

    ranked_documents = rank_documents(documents=matching_documents, query= user_query, index=index)
    
    
    
    print("------ METRIQUES ------")
    print(f"Requête = {user_query}")
    # On cherche le nombre de documents dans l'index (chaque token peut faire référence à plusieurs documents
    # donc on doit faire attention aux doublons, donc on utilise un set)
    id = set()
    for token, value in index.items():
        for key, value in index[token].items():
            id.add(key)
    print(f"Nombre de documents dans l'index: {len(id)}")        
    
    
    # Nombre de documents qui ont survécu au filtre
    print(f"Nombre de documents qui ont survécu au filtre : {len(matching_documents)}")
    
if __name__ == "__main__":
    main()
