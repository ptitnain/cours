# QCM-SQL

*BD, section « Cours ». Relecture de ma tentative sur Moodle ([lien](https://learning.esiea.fr/mod/quiz/review.php?attempt=27220&cmid=9081)).*

## Résumé

- **Statut** : Terminée
- **Commencé** : mardi 3 novembre 2026, 13:07
- **Terminé** : mardi 3 novembre 2026, 13:30
- **Durée** : 23 min 17 s

## Question 1  (Terminé; Noté sur 1,00)

Un administrateur souhaite afficher les villes dont le résultat de count(*) est supérieur à 10.000, alors il doit écrire?

**Propositions :**

```
a. SELECT ville, count(*) FROM table_ville GROUP BY ville WHERE count(id_ville)>10000; 
b. SELECT ville, count(*) FROM table_ville GROUP BY ville WHERE count(*)>10000; 
c. SELECT ville, count(*) FROM table_ville GROUP BY ville HAVING count(*)>10000; 
d. SELECT ville, count(*) FROM table_ville GROUP BY ville count(*)>10000;
```

**Ma réponse :** a. SELECT ville, count(*) FROM table_ville GROUP BY ville WHERE count(id_ville)>10000;  b. SELECT ville, count(*) FROM table_ville GROUP BY ville WHERE count(*)>10000;  c. SELECT ville, count(*) FROM table_ville GROUP BY ville HAVING count(*)>10000;  d. SELECT ville, count(*) FROM table_ville GROUP BY ville count(*)>10000;

## Question 2  (Terminé; Noté sur 1,00)

Quelle requête insère un nouveau client dans la table clients avec les informations suivantes : nom "Martin", ville "Paris" ?

**Propositions :**

```
a. INSERT INTO clients (nom, ville) VALUES ('Martin', 'Paris'); 
b. INSERT client INTO clients ('Martin', 'Paris'); 
c. INSERT INTO clients SET nom = 'Martin', ville = 'Paris'; 
d. ADD INTO clients (nom, ville) VALUES ('Martin', 'Paris');
```

**Ma réponse :** a. INSERT INTO clients (nom, ville) VALUES ('Martin', 'Paris');  b. INSERT client INTO clients ('Martin', 'Paris');  c. INSERT INTO clients SET nom = 'Martin', ville = 'Paris';  d. ADD INTO clients (nom, ville) VALUES ('Martin', 'Paris');

## Question 3  (Terminé; Noté sur 1,00)

Quelle requête met à jour la ville de l'employé avec l'id_client égal à 5 à "Lyon" ?

**Propositions :**

```
a. SET clients UPDATE ville = 'Lyon' WHERE id_client = 5; 
b. MODIFY clients SET ville = 'Lyon' WHERE id_client = 5; 
c. UPDATE clients SET ville = 'Lyon' WHERE id_client = 5; 
d. UPDATE clients CHANGE ville = 'Lyon' WHERE id_client = 5;
```

**Ma réponse :** a. SET clients UPDATE ville = 'Lyon' WHERE id_client = 5;  b. MODIFY clients SET ville = 'Lyon' WHERE id_client = 5;  c. UPDATE clients SET ville = 'Lyon' WHERE id_client = 5;  d. UPDATE clients CHANGE ville = 'Lyon' WHERE id_client = 5;

## Question 4  (Terminé; Noté sur 1,00)

Quelle requête supprime le client dont l'id_client est égal à 7 ?

**Propositions :**

```
a. DELETE client FROM clients WHERE id_client = 7; 
b. REMOVE client FROM clients WHERE id_client = 7; 
c. DELETE FROM clients WHERE id_client = 7; 
d. REMOVE FROM clients WHERE id_client = 7;
```

**Ma réponse :** a. DELETE client FROM clients WHERE id_client = 7;  b. REMOVE client FROM clients WHERE id_client = 7;  c. DELETE FROM clients WHERE id_client = 7;  d. REMOVE FROM clients WHERE id_client = 7;

## Question 5  (Terminé; Noté sur 1,00)

Quelle requête supprime tous les enregistrements de la table commandes?

**Propositions :**

```
a. DELETE FROM commandes; 
b. TRUNCATE commandes; 
c. DELETE * FROM commandes; 
d. REMOVE * FROM commandes;
```

**Ma réponse :** a. DELETE FROM commandes;  b. TRUNCATE commandes;  c. DELETE * FROM commandes;  d. REMOVE * FROM commandes; / a. DELETE FROM commandes;  b. TRUNCATE commandes;  c. DELETE * FROM commandes;  d. REMOVE * FROM commandes;

## Question 6  (Terminé; Noté sur 1,00)

Quelle requête joint les tables clients, commandes, et produits pour obtenir les noms des clients, leurs commandes, et le nom des produits commandés ?

**Propositions :**

```
a. SELECT clients.nom, commandes.numero, produits.nom_produit
FROM clients
JOIN commandes ON clients.id_client = commandes.id_client
JOIN produits ON commandes.id_produit = produits.id_produit; 
b. SELECT clients.nom, commandes.numero, produits.nom_produit
FROM clients, commandes, produits
WHERE clients.id_client = commandes.id_client
AND commandes.id_produit = produits.id_produit; 
c. SELECT clients.nom, produits.nom_produit
FROM clients, commandes, produits JOIN commandes ON clients.id_client = commandes.id_client
JOIN produits ON produits.id_produit = commandes.id_produit;
```

**Ma réponse :** a. SELECT clients.nom, commandes.numero, produits.nom_produit FROM clients JOIN commandes ON clients.id_client = commandes.id_client JOIN produits ON commandes.id_produit = produits.id_produit;  b. SELECT clients.nom, commandes.numero, produits.nom_produit FROM clients, commandes, produits WHERE clients.id_client = commandes.id_client AND commandes.id_produit = produits.id_produit;  c. SELECT clients.nom, produits.nom_produit FROM clients, commandes, produits JOIN commandes ON clients.id_client = commandes.id_client JOIN produits ON produits.id_produit = commandes.id_produit; / a. SELECT clients.nom, commandes.numero, produits.nom_produit FROM clients JOIN commandes ON clients.id_client = commandes.id_client JOIN produits ON commandes.id_produit = produits.id_produit;  b. SELECT clients.nom, commandes.numero, produits.nom_produit FROM clients, commandes, produits WHERE clients.id_client = commandes.id_client AND commandes.id_produit = produits.id_produit;  c. SELECT clients.nom, produits.nom_produit FROM clients, commandes, produits JOIN commandes ON clients.id_client = commandes.id_client JOIN produits ON produits.id_produit = commandes.id_produit;

## Question 7  (Terminé; Noté sur 1,00)

Un administrateur souhaite afficher les noms des clients ainsi que les produits qu'ils ont commandés. Les informations des clients sont dans la table clients, et celles des produits dans la table commandes. Quelle requête est correcte ?

**Propositions :**

```
a. SELECT clients.nom, commandes.produit
FROM clients JOIN commandes
ON clients.id_client = commandes.id_client; 
b. SELECT clients.nom, commandes.produit
FROM clients, commandes
WHERE clients.id_client = commandes.id_client; 
c. SELECT nom, produit
FROM clients INNER JOIN commandes; 
d. SELECT clients.nom, commandes.produit
FROM clients  JOIN commandes;
```

**Ma réponse :** a. SELECT clients.nom, commandes.produit FROM clients JOIN commandes ON clients.id_client = commandes.id_client;  b. SELECT clients.nom, commandes.produit FROM clients, commandes WHERE clients.id_client = commandes.id_client;  c. SELECT nom, produit FROM clients INNER JOIN commandes;  d. SELECT clients.nom, commandes.produit FROM clients  JOIN commandes; / a. SELECT clients.nom, commandes.produit FROM clients JOIN commandes ON clients.id_client = commandes.id_client;  b. SELECT clients.nom, commandes.produit FROM clients, commandes WHERE clients.id_client = commandes.id_client;  c. SELECT nom, produit FROM clients INNER JOIN commandes;  d. SELECT clients.nom, commandes.produit FROM clients  JOIN commandes;

## Question 8  (Terminé; Noté sur 1,00)

Quelle requête SQL renvoie toutes les villes sans doublons à partir de la table employes ?

**Propositions :**

```
a. SELECT ville FROM employes; 
b. SELECT ville FROM employes GROUP BY ville; 
c. SELECT DISTINCT ville FROM employes; 
d. SELECT ville FROM employes ORDER BY ville;
```

**Ma réponse :** a. SELECT ville FROM employes;  b. SELECT ville FROM employes GROUP BY ville;  c. SELECT DISTINCT ville FROM employes;  d. SELECT ville FROM employes ORDER BY ville; / a. SELECT ville FROM employes;  b. SELECT ville FROM employes GROUP BY ville;  c. SELECT DISTINCT ville FROM employes;  d. SELECT ville FROM employes ORDER BY ville;

## Question 9  (Terminé; Noté sur 1,00)

Un administrateur souhaite trier les employés par nom dans l'ordre décroissant. Quelle requête doit-il écrire ?

**Propositions :**

```
a. SELECT * FROM employes ORDER BY nom ASC; 
b. SELECT * FROM employes ORDER BY nom; 
c. SELECT * FROM employes SORT BY nom DESC; 
d. SELECT * FROM employes ORDER BY nom DESC;
```

**Ma réponse :** a. SELECT * FROM employes ORDER BY nom ASC;  b. SELECT * FROM employes ORDER BY nom;  c. SELECT * FROM employes SORT BY nom DESC;  d. SELECT * FROM employes ORDER BY nom DESC;

## Question 10  (Terminé; Noté sur 1,00)

Un administrateur souhaite afficher les noms des employés qui ont un salaire supérieur à la moyenne des salaires. Quelle requête est correcte ?

**Propositions :**

```
a. SELECT nom FROM employes WHERE salaire > AVG(salaire); 
b. SELECT nom FROM employes WHERE salaire > (SELECT AVG(salaire) FROM employes); 
c. SELECT nom FROM employes WHERE salaire > (AVG(salaire)); 
d. SELECT nom FROM employes HAVING salaire > (SELECT AVG(salaire));
```

**Ma réponse :** a. SELECT nom FROM employes WHERE salaire > AVG(salaire);  b. SELECT nom FROM employes WHERE salaire > (SELECT AVG(salaire) FROM employes);  c. SELECT nom FROM employes WHERE salaire > (AVG(salaire));  d. SELECT nom FROM employes HAVING salaire > (SELECT AVG(salaire));

## Question 11  (Terminé; Noté sur 1,00)

Quelle requête renvoie les noms de tous les clients à partir des tables clients_France et clients_etranger sans doublons ?

**Propositions :**

```
a. SELECT nom FROM clients_france INTERSECT SELECT nom FROM clients_etranger; 
b. SELECT nom FROM clients_france UNION SELECT nom FROM clients_etranger; 
c. SELECT nom FROM clients_france AND SELECT nom FROM clients_etranger; 
d. SELECT nom FROM clients_france JOIN clients_etranger ON clients_france.nom = clients_etranger.nom;
```

**Ma réponse :** a. SELECT nom FROM clients_france INTERSECT SELECT nom FROM clients_etranger;  b. SELECT nom FROM clients_france UNION SELECT nom FROM clients_etranger;  c. SELECT nom FROM clients_france AND SELECT nom FROM clients_etranger;  d. SELECT nom FROM clients_france JOIN clients_etranger ON clients_france.nom = clients_etranger.nom;

## Question 12  (Terminé; Noté sur 1,00)

Quelle requête renvoie le nombre total de clients dans la table clients?

**Propositions :**

```
a. SELECT SUM(*) FROM clients; 
b. SELECT COUNT(id_client) FROM clients; 
c. SELECT TOTAL(id_client) FROM clients; 
d. SELECT MAX(id_client) FROM clients;
```

**Ma réponse :** a. SELECT SUM(*) FROM clients;  b. SELECT COUNT(id_client) FROM clients;  c. SELECT TOTAL(id_client) FROM clients;  d. SELECT MAX(id_client) FROM clients;

## Question 13  (Terminé; Noté sur 1,00)

Un administrateur souhaite afficher les produits dont le prix est supérieur à 100. Quelle requête est correcte ?

**Propositions :**

```
a. SELECT * FROM produits WHERE prix > 100; 
b. SELECT * FROM produits WHERE prix = 100; 
c. SELECT * FROM produits HAVING prix > 100; 
d. SELECT * FROM produits WHERE prix >= 100;
```

**Ma réponse :** a. SELECT * FROM produits WHERE prix > 100;  b. SELECT * FROM produits WHERE prix = 100;  c. SELECT * FROM produits HAVING prix > 100;  d. SELECT * FROM produits WHERE prix >= 100;

## Question 14  (Terminé; Noté sur 1,00)

Quelle requête affiche tous les enregistrements de la table clients ?

**Propositions :**

```
a. SELECT * FROM clients; 
b. SELECT clients FROM *; 
c. SELECT tout FROM clients; 
d. SELECT clients.* FROM clients;
```

**Ma réponse :** a. SELECT * FROM clients;  b. SELECT clients FROM *;  c. SELECT tout FROM clients;  d. SELECT clients.* FROM clients; / a. SELECT * FROM clients;  b. SELECT clients FROM *;  c. SELECT tout FROM clients;  d. SELECT clients.* FROM clients;
