# indexation_web_TP3

## Calcul du Score de Pertinence

La formule pour calculer le score de pertinence d'un document, basé sur la position des tokens et leur fréquence, est décrite ci-dessous. Ce score est utilisé pour évaluer la pertinence des documents par rapport à une requête utilisateur.

### Fréquence du Token (`freq_score`)

La fréquence d'un token dans un document est représentée par `freq_score`.

### Position des Tokens (`positions`)

L'ensemble des positions de ce token dans le document est noté `positions`.

### Calcul du Score Basé sur la Position (`pos_score`)

Le score basé sur la position, `pos_score`, est calculé comme suit :

- **Formule :**
$$pos_{score} = 1 / (1 + (\sum positions / len(positions)))$$


où $\sum positions$ représente la somme des indices de position du token dans le document, et `len(positions)` est le nombre total d'occurrences du token dans le document. Cette formule calcule l'inverse de la position moyenne du token, ajusté pour valoriser les tokens apparaissant plus tôt dans le document.

### Calcul du Score Total du Document (`doc_score`)

Le score total du document, `doc_score`, combine `freq_score` et `pos_score` :

- **Formule :**

$$doc_{score} = 0.7 * freq_{score} + 0.3 * pos_{score}$$


Les coefficients 0.7 et 0.3 sont des poids attribués respectivement à `freq_score` et `pos_score`, reflétant leur importance relative dans le calcul du score total. Ces poids peuvent être ajustés selon l'analyse de leur impact sur la pertinence du document.

Cette approche équilibre entre la fréquence d'apparition d'un token dans un document et la précocité de son apparition, afin de déterminer la pertinence globale du document par rapport à une requête utilisateur.
