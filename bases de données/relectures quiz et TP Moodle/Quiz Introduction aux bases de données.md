# Quiz Introduction aux bases de données

*BD, section « Cours ». Relecture de ma tentative sur Moodle ([lien](https://learning.esiea.fr/mod/quiz/review.php?attempt=13776&cmid=9078)).*

## Résumé

- **Statut** : Terminée
- **Commencé** : vendredi 2 octobre 2026, 21:26
- **Terminé** : vendredi 2 octobre 2026, 21:32
- **Durée** : 6 min 32 s

## Question 1  (Terminé; Noté sur 2,00)

Dans un système de gestion de bibliothèque, vous devez modéliser les entités suivantes : Livre, Auteur, Membre, et Emprunt. Chaque livre est écrit par un ou plusieurs auteurs, chaque membre peut emprunter plusieurs livres, et chaque emprunt concerne un livre spécifique et un membre spécifique.Quel est le schéma correct pour représenter les relations entre ces entités ?

**Propositions :**

```
a. Livre -- ÉcritPar --> AuteurMembre -- Emprunte --> LivreLivre -- EmpruntéPar --> Membre 
b. 
Livre -- ÉcritPar --> AuteurMembre -- Effectue --> Emprunt -- Inclut --> LivreLivre -- EstÉcritPar --> Auteur

 
c. Livre -- EstRéservéPar --> Emprunt -- RéaliséPar --> MembreLivre -- ÉcritPar --> Auteur 
d. Livre -- AppartientÀ --> EmpruntEmprunt -- RéaliséPar --> MembreAuteur -- Écrit --> Livre
```

**Ma réponse :** a. Livre -- ÉcritPar --> AuteurMembre -- Emprunte --> LivreLivre -- EmpruntéPar --> Membre  b.  Livre -- ÉcritPar --> AuteurMembre -- Effectue --> Emprunt -- Inclut --> LivreLivre -- EstÉcritPar --> Auteur    c. Livre -- EstRéservéPar --> Emprunt -- RéaliséPar --> MembreLivre -- ÉcritPar --> Auteur  d. Livre -- AppartientÀ --> EmpruntEmprunt -- RéaliséPar --> MembreAuteur -- Écrit --> Livre

## Question 2  (Terminé; Noté sur 2,00)

Soit un système de gestion de commandes contient les entités suivantes :

Client (Attributs : NumClient, Nom, Prénom, Adresse)
Commande (Attributs : NumCommande, Date, Montant)
Produit (Attributs : CodeProduit, NomProduit, Prix)

Relations :

Un client peut passer plusieurs commandes.
Chaque commande peut contenir plusieurs produits.
Un produit peut apparaître dans plusieurs commandes.

Question: Quelle est la nature de la relation entre Client et Commande ?

**Propositions :**

```
a. Un-à-un 
b. 
Un-à-plusieurs

 
c. Plusieurs-à-un 
d. Plusieurs-à-plusieurs
```

**Ma réponse :** a. Un-à-un  b.  Un-à-plusieurs    c. Plusieurs-à-un  d. Plusieurs-à-plusieurs

## Question 3  (Terminé; Noté sur 2,00)

Soit un système de gestion de commandes contient les entités suivantes :

Client (Attributs : NumClient, Nom, Prénom, Adresse)
Commande (Attributs : NumCommande, Date, Montant)
Produit (Attributs : CodeProduit, NomProduit, Prix)

Relations :

Un client peut passer plusieurs commandes.
Chaque commande peut contenir plusieurs produits.
Un produit peut apparaître dans plusieurs commandes. 

Question: Quelle est la cardinalité de la relation entre Commande et Produit ?

**Propositions :**

```
a. Un-à-un 
b. 
Un-à-plusieurs

 
c. Plusieurs-à-un 
d. Plusieurs-à-plusieurs
```

**Ma réponse :** a. Un-à-un  b.  Un-à-plusieurs    c. Plusieurs-à-un  d. Plusieurs-à-plusieurs

## Question 4  (Terminé; Noté sur 2,00)

Soit un système de bibliothèque inclut les entités suivantes :

Livre (Attributs : ISBN, Titre, Auteur, Date de publication)
Membre (Attributs : Numéro de membre, Nom, Adresse, Date d’adhésion)
Emprunt (Attributs : Date d’emprunt, Date de retour prévue)

Relations :

Un membre peut emprunter plusieurs livres.
Chaque livre peut être emprunté par plusieurs membres.

Question: Quel est le type de relation entre les entités Livre et Membre ?

**Propositions :**

```
a. Un-à-un 
b. 
Un-à-plusieurs

 
c. Plusieurs-à-un 
d. Plusieurs-à-plusieurs
```

**Ma réponse :** a. Un-à-un  b.  Un-à-plusieurs    c. Plusieurs-à-un  d. Plusieurs-à-plusieurs

## Question 5  (Terminé; Noté sur 1,00)

Laquelle de ces catégories se doit d'avoir le même domaine pour son utilisation ?

**Propositions :**

```
a. une table 
b. une colonne

 
c. une ligne
```

**Ma réponse :** a. une table  b. une colonne    c. une ligne

## Question 6  (Terminé; Noté sur 1,00)

Quel est l'un des problèmes majeurs associés aux systèmes de fichiers pour la gestion des données ?

**Propositions :**

```
a. Trop facile à mettre en œuvre. 
b. Un accès illimité aux données par tous les utilisateurs. 
c. Difficulté à garantir la cohérence et la sécurité des données.
```

**Ma réponse :** a. Trop facile à mettre en œuvre.  b. Un accès illimité aux données par tous les utilisateurs.  c. Difficulté à garantir la cohérence et la sécurité des données.

## Question 7  (Terminé; Noté sur 1,00)

Parmi les différentes appellations suivantes, laquelle n’est pas liée au modèle conceptuel de
données?

**Propositions :**

```
a. Entité 
b. Association

 
c. Objet
```

**Ma réponse :** a. Entité  b. Association    c. Objet

## Question 8  (Terminé; Noté sur 1,00)

Quel est l'avantage majeur de l'utilisation d'une base de données par rapport aux fichiers classiques ?

**Propositions :**

```
a. Les données sont mieux sécurisées et plus faciles d'accès 
b. Plus de redondance 
c. Moins de flexibilité
```

**Ma réponse :** a. Les données sont mieux sécurisées et plus faciles d'accès  b. Plus de redondance  c. Moins de flexibilité

## Question 9  (Terminé; Noté sur 1,00)

Quel est le modèle conceptuel utilisé pour modéliser les données dans un SGBD?

**Propositions :**

```
a. Diagramme de classes  UML. 
b. Modèle Entité-Association (E-A).

 
c. Modèle de données relationnel. 
d. Schéma Relationnel.
```

**Ma réponse :** a. Diagramme de classes  UML.  b. Modèle Entité-Association (E-A).    c. Modèle de données relationnel.  d. Schéma Relationnel.

## Question 10  (Terminé; Noté sur 1,00)

Qu'est-ce qu'une contrainte d'intégrité fonctionnelle ?

**Propositions :**

```
a. Une règle qui garantit l'absence de redondance des données. 
b. Une règle qui garantit l'intégrité des relations entre les tables. 
c. Une règle qui impose qu'une colonne ou un ensemble de colonnes dépendent fonctionnellement d'une autre colonne. 
d. Une règle qui interdit les modifications sur les données.
```

**Ma réponse :** a. Une règle qui garantit l'absence de redondance des données.  b. Une règle qui garantit l'intégrité des relations entre les tables.  c. Une règle qui impose qu'une colonne ou un ensemble de colonnes dépendent fonctionnellement d'une autre colonne.  d. Une règle qui interdit les modifications sur les données.

## Question 11  (Terminé; Noté sur 1,00)

Qu'est-ce qu'une base de données informatique ?

**Propositions :**

```
a. Un réseau de stockage de données distribué sur plusieurs serveurs. 
b. Une collection d'informations organisées pour être consultables, gérables et mises à jour. 
c. Un programme qui exécute des commandes.
```

**Ma réponse :** a. Un réseau de stockage de données distribué sur plusieurs serveurs.  b. Une collection d'informations organisées pour être consultables, gérables et mises à jour.  c. Un programme qui exécute des commandes.

## Question 12  (Terminé; Noté sur 1,00)

Qu’est-ce qu’une clé primaire dans un modèle relationnel ?

**Propositions :**

```
a. Une colonne qui contient des valeurs dupliquées 
b. Une colonne qui permet de lier deux tables.
 
c. Une colonne ou un ensemble de colonnes qui identifie de manière unique chaque ligne d'une table. 
d. Une colonne qui permet d'ajouter des contraintes à la table.
```

**Ma réponse :** a. Une colonne qui contient des valeurs dupliquées  b. Une colonne qui permet de lier deux tables.   c. Une colonne ou un ensemble de colonnes qui identifie de manière unique chaque ligne d'une table.  d. Une colonne qui permet d'ajouter des contraintes à la table.

## Question 13  (Terminé; Noté sur 1,00)

Dans un modèle relationnel, une clé étrangère permet de :

**Propositions :**

```
a. Structurer les données en objets. 
b. Créer une relation entre deux tables. 
c. Identifier de manière unique une ligne dans une table. 
d. Éviter la redondance des données.
```

**Ma réponse :** a. Structurer les données en objets.  b. Créer une relation entre deux tables.  c. Identifier de manière unique une ligne dans une table.  d. Éviter la redondance des données.

## Question 14  (Terminé; Noté sur 1,00)

A propos de la modélisation :

**Propositions :**

```
a. C’est une étape de réflexion avant la conception. 
b. Le modèle entité-association est un schéma théorique qui vise à rendre compte des relations existant entre divers éléments d’un système.

 
c. On modélise pour éviter les anomalies d’insertion et de modifications. 
d. La cardinalité précise le nombre de fois minimum et maximum qu’une instance de relation participe à une association. 
e. Une entité possède toujours au moins un attribut.
```

**Ma réponse :** a. C’est une étape de réflexion avant la conception.  b. Le modèle entité-association est un schéma théorique qui vise à rendre compte des relations existant entre divers éléments d’un système.    c. On modélise pour éviter les anomalies d’insertion et de modifications.  d. La cardinalité précise le nombre de fois minimum et maximum qu’une instance de relation participe à une association.  e. Une entité possède toujours au moins un attribut. / a. C’est une étape de réflexion avant la conception.  b. Le modèle entité-association est un schéma théorique qui vise à rendre compte des relations existant entre divers éléments d’un système.    c. On modélise pour éviter les anomalies d’insertion et de modifications.  d. La cardinalité précise le nombre de fois minimum et maximum qu’une instance de relation participe à une association.  e. Une entité possède toujours au moins un attribut. / a. C’est une étape de réflexion avant la conception.  b. Le modèle entité-association est un schéma théorique qui vise à rendre compte des relations existant entre divers éléments d’un système.    c. On modélise pour éviter les anomalies d’insertion et de modifications.  d. La cardinalité précise le nombre de fois minimum et maximum qu’une instance de relation participe à une association.  e. Une entité possède toujours au moins un attribut.

## Question 15  (Terminé; Noté sur 1,00)

Dans une table, laquelle de ces informations est vraie ?

**Propositions :**

```
a. Une ligne ne peut être représentée qu'une seule fois. 
b. L'ordre des lignes n'est pas important. 
c. Les deux réponses.
```

**Ma réponse :** a. Une ligne ne peut être représentée qu'une seule fois.  b. L'ordre des lignes n'est pas important.  c. Les deux réponses.

## Question 16  (Terminé; Noté sur 1,00)

Quel est le modèle de base de données le plus utilisé ?

**Propositions :**

```
a. Modèle hiérarchique. 
b. Modèle réseau.

 
c. Modèle relationnel. 
d. Modèle orienté objet.
```

**Ma réponse :** a. Modèle hiérarchique.  b. Modèle réseau.    c. Modèle relationnel.  d. Modèle orienté objet.
