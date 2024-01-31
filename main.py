import json

def load_documents():
    with open('documents.json', 'r', encoding='utf-8') as file:
        return json.load(file)

def load_index():
    with open('title_pos_index.json', 'r', encoding='utf-8') as file:
        return json.load(file)

def tokenize_query(query):
    return [token.lower() for token in query.split()]

def search_documents(query, documents, index):
    tokens = tokenize_query(query)
    
    matching_documents = set(doc['id'] for doc in documents)
    
    for token in tokens:
        if token in index:
            matching_documents &= set(index[token]['docid'].keys())
    
    return matching_documents

def main():
    documents = load_documents()
    index = load_index()

    user_query = input("Entrez votre requête : ")
    
    matching_documents = search_documents(user_query, documents, index)

    if matching_documents:
        print("Documents correspondants :")
        for doc_id in matching_documents:
            print(f"ID: {doc_id}, Titre: {documents[doc_id]['title']}, URL: {documents[doc_id]['url']}")
    else:
        print("Aucun document ne correspond à la requête.")

if __name__ == "__main__":
    main()
