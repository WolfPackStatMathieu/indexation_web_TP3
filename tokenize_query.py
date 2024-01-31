def tokenize_query(query):
    """
    Tokenise la requête en utilisant un split sur les espaces et convertit tous les tokens en minuscules.

    Parameters:
        query (str): La requête de l'utilisateur.

    Returns:
        list: Liste des tokens de la requête, en minuscules.
    """
    return [token.lower() for token in query.split()]

if __name__ == "__main__":
    # Exemple d'utilisation de tokenize_query
    example_query = "Exemple de Requête Utilisateur"
    tokenized_example = tokenize_query(example_query)

    print(f"Requête originale : '{example_query}'")
    print(f"Tokens obtenus    : {tokenized_example}")
