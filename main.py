
from load_documents import load_documents
from load_index import load_index
from search_documents import search_documents

def main():
    documents = load_documents()
    index = load_index()

    # user_query = input("Entrez votre requête : ")
    user_query = "µtorrent"
    
    matching_documents = search_documents(user_query, documents, index)

    if matching_documents:
        print("Documents correspondants :")
        for doc_id_str in matching_documents:
            doc_id = int(doc_id_str)  # Convertir la chaîne en entier
            print(f"ID: {doc_id}, Titre: {documents[doc_id]['title']}, URL: {documents[doc_id]['url']}")
    else:
        print("Aucun document ne correspond à la requête.")


if __name__ == "__main__":
    main()
