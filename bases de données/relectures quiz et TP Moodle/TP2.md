# TP2

*BD, section « Travaux pratiques ». Relecture de ma tentative sur Moodle ([lien](https://learning.esiea.fr/mod/quiz/review.php?attempt=27362&cmid=9087)).*

## Résumé

- **Statut** : Terminée
- **Commencé** : mardi 3 novembre 2026, 13:20
- **Terminé** : mardi 24 novembre 2026, 09:21
- **Durée** : 20 jours 20 heures
- **Points** : 22,80/24,00
- **Note** : 19,00 sur 20,00 (95%)

## Question 1  (Correct; Note de 1,00 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
SELECT Titre FROM Film ORDER BY Titre;
```

**Retour Moodle :**

```
Feedback

Test
Résultat attendu
Résultat obtenu

-- Testing with original db
Titre
-----------------------
48 minutes pour vivre
Annie Hall
Brazil
Broken Arrow
Casablanca
Edward scissorhands
Greystocke
Impitoyable
Jurassic Park
Le dernier metro
Manhattan
Metropolis
Mission Impossible
Mission Impossible 2
Piege de cristal
Psychose
Pulp Fiction
Rencontres du 3eme type
Reservoir Dogs
Shining
Sleepy Hollow
Titanic
Twin Peaks
Underground
Une journee en enfer
Vertigo
Volte-Face
Titre
-----------------------
48 minutes pour vivre
Annie Hall
Brazil
Broken Arrow
Casablanca
Edward scissorhands
Greystocke
Impitoyable
Jurassic Park
Le dernier metro
Manhattan
Metropolis
Mission Impossible
Mission Impossible 2
Piege de cristal
Psychose
Pulp Fiction
Rencontres du 3eme type
Reservoir Dogs
Shining
Sleepy Hollow
Titanic
Twin Peaks
Underground
Une journee en enfer
Vertigo
Volte-Face

Tous les tests ont été réussis ! CorrectNote pour cet envoi : 1,00/1,00.
```

## Question 2  (Correct; Note de 1,00 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
SELECT Nom, Annee_naissance FROM Artiste WHERE Annee_naissance < 1950;
```

**Retour Moodle :**

```
Feedback

Test
Résultat attendu
Résultat obtenu

-- Testing with original db
Nom        Annee_naissance
---------  ---------------
Allen      1938
Lynch      1946
Lang       1899
Eastwood   1932
Hitchcock  1898
Kubrick    1935
Curtis     1902
Stewart    1911
Tarantino  1948
Spielberg  1943
Gillian    1944
Truffaut   1938
Keitel     1940
Cameron    1943
Nom        Annee_naissance
---------  ---------------
Allen      1938
Lynch      1946
Lang       1899
Eastwood   1932
Hitchcock  1898
Kubrick    1935
Curtis     1902
Stewart    1911
Tarantino  1948
Spielberg  1943
Gillian    1944
Truffaut   1938
Keitel     1940
Cameron    1943

Tous les tests ont été réussis ! CorrectNote pour cet envoi : 1,00/1,00.
```

## Question 3  (Correct; Note de 0,90 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
SELECT Nom_cinema FROM Cinema WHERE Arrondissement = 12;
```

**Retour Moodle :**

```
Feedback

Test
Résultat attendu
Résultat obtenu

-- Testing with original db
Nom_cinema
----------
Nations
Nom_cinema
----------
Nations

Tous les tests ont été réussis ! CorrectPoints pour cet envoi : 1,00/1,00. En tenant compte des tentatives précédentes, cela donne 0,90/1,00.
```

## Question 4  (Correct; Note de 1,00 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
SELECT Nom, Prenom FROM Artiste WHERE Nom LIKE 'H%';
```

**Retour Moodle :**

```
Feedback

Test
Résultat attendu
Résultat obtenu

-- Testing with original db
Nom        Prenom
---------  ------
Hitchcock  Alfred
Hunt       Greg
Hudson     Hugh
Nom        Prenom
---------  ------
Hitchcock  Alfred
Hunt       Greg
Hudson     Hugh

Tous les tests ont été réussis ! CorrectNote pour cet envoi : 1,00/1,00.
```

## Question 5  (Correct; Note de 1,00 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
SELECT Nom, Prenom FROM Artiste WHERE Annee_naissance IS NULL;
```

**Retour Moodle :**

```
Feedback

Test
Résultat attendu
Résultat obtenu

-- Testing with original db
Nom     Prenom
------  ------
Novak   Kim
Hudson  Hugh
Nom     Prenom
------  ------
Novak   Kim
Hudson  Hugh

Tous les tests ont été réussis ! CorrectNote pour cet envoi : 1,00/1,00.
```

## Question 6  (Correct; Note de 0,90 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
SELECT count(*) 
FROM Role 
WHERE Nom_acteur='Willis' 
AND Nom_Role = 'McLane';
```

**Retour Moodle :**

```
Feedback

Test
Résultat attendu
Résultat obtenu

-- Testing with original db
count(*)
--------
3
count(*)
--------
3

Tous les tests ont été réussis ! CorrectPoints pour cet envoi : 1,00/1,00. En tenant compte des tentatives précédentes, cela donne 0,90/1,00.
```

## Question 7  (Correct; Note de 1,00 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
SELECT A.Nom, A.Prenom 
FROM Artiste A
JOIN Role R ON A.Nom = R.Nom_acteur
WHERE R.Nom_Role = 'Tarzan';
```

**Retour Moodle :**

```
Feedback

Test
Résultat attendu
Résultat obtenu

-- Testing with original db
Nom      Prenom
-------  ----------
Lambert  Christophe
Nom      Prenom
-------  ----------
Lambert  Christophe

Tous les tests ont été réussis ! CorrectNote pour cet envoi : 1,00/1,00.
```

## Question 8  (Correct; Note de 1,00 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
SELECT R.Nom_acteur 
FROM Role R
JOIN Film F ON R.ID_film = F.ID_film
WHERE F.Titre = 'Vertigo';
```

**Retour Moodle :**

```
Feedback

Test
Résultat attendu
Résultat obtenu

-- Testing with original db
Nom_acteur
----------
Novak
Stewart
Nom_acteur
----------
Novak
Stewart

Tous les tests ont été réussis ! CorrectNote pour cet envoi : 1,00/1,00.
```

## Question 9  (Correct; Note de 1,00 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
SELECT F.Titre, S.Heure_debut, S.Heure_fin 
FROM Film F
JOIN Seance S ON F.ID_film = S.ID_film
WHERE S.Nom_cinema = 'Rex';
```

**Retour Moodle :**

```
Feedback

Test
Résultat attendu
Résultat obtenu

-- Testing with original db
Titre                 Heure_debut  Heure_fin
--------------------  -----------  ---------
Reservoir Dogs        8            9
Psychose              9            10
Une journee en enfer  7            8
Une journee en enfer  5            6
Shining               4            5
Vertigo               3            4
Jurassic Park         9            10
Jurassic Park         11           12
Jurassic Park         13           14
Metropolis            15           16
Metropolis            16           17
Metropolis            9            10
Titre                 Heure_debut  Heure_fin
--------------------  -----------  ---------
Reservoir Dogs        8            9
Psychose              9            10
Une journee en enfer  7            8
Une journee en enfer  5            6
Shining               4            5
Vertigo               3            4
Jurassic Park         9            10
Jurassic Park         11           12
Jurassic Park         13           14
Metropolis            15           16
Metropolis            16           17
Metropolis            9            10

Tous les tests ont été réussis ! CorrectNote pour cet envoi : 1,00/1,00.
```

## Question 10  (Correct; Note de 1,00 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
SELECT F.Titre, R.Nom_Role 
FROM Film F
JOIN Role R ON F.ID_film = R.ID_film
WHERE R.Nom_acteur = 'Allen';
```

**Retour Moodle :**

```
Feedback

Test
Résultat attendu
Résultat obtenu

-- Testing with original db
Titre       Nom_Role
----------  --------
Manhattan   Davis
Annie Hall  Jonas
Titre       Nom_Role
----------  --------
Manhattan   Davis
Annie Hall  Jonas

Tous les tests ont été réussis ! CorrectNote pour cet envoi : 1,00/1,00.
```

## Question 11  (Correct; Note de 0,90 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
SELECT F.Nom_Realisateur AS Nom_acteur, F.Titre, R.Nom_Role
FROM Film F
JOIN Role R ON F.ID_film = R.ID_film
WHERE F.Nom_Realisateur = R.Nom_acteur;
```

**Retour Moodle :**

```
Feedback

Test
Résultat attendu
Résultat obtenu

-- Testing with original db
Nom_acteur  Titre           Nom_Role
----------  --------------  --------
Allen       Manhattan       Davis
Allen       Annie Hall      Jonas
Tarantino   Reservoir Dogs  Mr Brown
Eastwood    Impitoyable     Munny
Nom_acteur  Titre           Nom_Role
----------  --------------  --------
Allen       Manhattan       Davis
Allen       Annie Hall      Jonas
Tarantino   Reservoir Dogs  Mr Brown
Eastwood    Impitoyable     Munny

Tous les tests ont été réussis ! CorrectPoints pour cet envoi : 1,00/1,00. En tenant compte des tentatives précédentes, cela donne 0,90/1,00.
```

## Question 12  (Correct; Note de 1,00 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
SELECT C.Nom_cinema, C.Adresse, S.Heure_debut, S.Heure_fin 
FROM Cinema C
JOIN Seance S ON C.Nom_cinema = S.Nom_cinema
JOIN Film F ON S.ID_film = F.ID_film
WHERE F.Titre = 'Shining';
```

**Retour Moodle :**

```
Feedback

Test
Résultat attendu
Résultat obtenu

-- Testing with original db
Nom_cinema  Adresse            Heure_debut  Heure_fin
----------  -----------------  -----------  ---------
Rex         22 Bd Poissoniere  4            5
Kino        3 Bd Raspail       18           19
Nations     3 Rue de Reuilly   1            2
Nations     3 Rue de Reuilly   3            4
Nations     3 Rue de Reuilly   4            5
Nom_cinema  Adresse            Heure_debut  Heure_fin
----------  -----------------  -----------  ---------
Rex         22 Bd Poissoniere  4            5
Kino        3 Bd Raspail       18           19
Nations     3 Rue de Reuilly   1            2
Nations     3 Rue de Reuilly   3            4
Nations     3 Rue de Reuilly   4            5

Tous les tests ont été réussis ! CorrectNote pour cet envoi : 1,00/1,00.
```

## Question 13  (Correct; Note de 1,00 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
SELECT C.Nom_cinema, C.Adresse, S.Heure_debut, S.Heure_fin 
FROM Cinema C
JOIN Seance S ON C.Nom_cinema = S.Nom_cinema
JOIN Role R ON S.ID_film = R.ID_film
WHERE R.Nom_acteur = 'Eastwood';
```

**Retour Moodle :**

```
Feedback

Test
Résultat attendu
Résultat obtenu

-- Testing with original db
Nom_cinema  Adresse           Heure_debut  Heure_fin
----------  ----------------  -----------  ---------
Halles      Forum des Halles  15           16
Nom_cinema  Adresse           Heure_debut  Heure_fin
----------  ----------------  -----------  ---------
Halles      Forum des Halles  15           16

Tous les tests ont été réussis ! CorrectNote pour cet envoi : 1,00/1,00.
```

## Question 14  (Correct; Note de 1,00 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
SELECT C.Nom_cinema, Sa.No_salle, Se.Heure_debut, Se.Heure_fin, F.Titre 
FROM Cinema C
JOIN Salle Sa ON C.Nom_cinema = Sa.Nom_cinema
JOIN Seance Se ON Sa.Nom_cinema = Se.Nom_cinema AND Sa.No_salle = Se.No_salle
JOIN Film F ON Se.ID_film = F.ID_film
WHERE C.Arrondissement = 2 
AND Sa.Climatise = 'O';
```

**Retour Moodle :**

```
Feedback

Test
Résultat attendu
Résultat obtenu

-- Testing with original db
Nom_cinema  No_salle  Heure_debut  Heure_fin  Titre
----------  --------  -----------  ---------  --------------------
Rex         1         8            9          Reservoir Dogs
Rex         1         9            10         Psychose
Rex         2         7            8          Une journee en enfer
Rex         2         5            6          Une journee en enfer
Rex         2         4            5          Shining
Rex         2         3            4          Vertigo
Nom_cinema  No_salle  Heure_debut  Heure_fin  Titre
----------  --------  -----------  ---------  --------------------
Rex         1         8            9          Reservoir Dogs
Rex         1         9            10         Psychose
Rex         2         7            8          Une journee en enfer
Rex         2         5            6          Une journee en enfer
Rex         2         4            5          Shining
Rex         2         3            4          Vertigo

Tous les tests ont été réussis ! CorrectNote pour cet envoi : 1,00/1,00.
```

## Question 15  (Correct; Note de 1,00 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
SELECT DISTINCT C.Nom_cinema, C.Adresse, C.Arrondissement, Sa.Capacite
FROM Cinema C
JOIN Salle Sa ON C.Nom_cinema = Sa.Nom_cinema
JOIN Seance Se ON C.Nom_cinema = Se.Nom_cinema
JOIN Role R ON Se.ID_film = R.ID_film
WHERE Sa.Capacite > 150 
AND R.Nom_acteur = 'Willis';
```

**Retour Moodle :**

```
Feedback

Test
Résultat attendu
Résultat obtenu

-- Testing with original db
Nom_cinema  Adresse       Arrondissement  Capacite
----------  ------------  --------------  --------
Kino        3 Bd Raspail  15              280
Nom_cinema  Adresse       Arrondissement  Capacite
----------  ------------  --------------  --------
Kino        3 Bd Raspail  15              280

Tous les tests ont été réussis ! CorrectNote pour cet envoi : 1,00/1,00.
```

## Question 16  (Correct; Note de 1,00 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
SELECT Nom_cinema, Adresse 
FROM Cinema 
WHERE Nom_cinema NOT IN (
    SELECT Nom_cinema 
    FROM Salle 
    WHERE Capacite <= 100
);
```

**Retour Moodle :**

```
Feedback

Test
Résultat attendu
Résultat obtenu

-- Testing with original db
Nom_cinema  Adresse
----------  ------------
Kino        3 Bd Raspail
Nom_cinema  Adresse
----------  ------------
Kino        3 Bd Raspail

Tous les tests ont été réussis ! CorrectNote pour cet envoi : 1,00/1,00.
```

## Question 17  (Correct; Note de 0,90 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
SELECT R.Nom_acteur AS Nom_acteur
FROM Role R
WHERE R.Nom_acteur NOT IN (SELECT Nom_Realisateur FROM Film)
GROUP BY R.Nom_acteur
ORDER BY MIN(R.ID_film), R.Nom_acteur;
```

**Retour Moodle :**

```
Feedback

Test
Résultat attendu
Résultat obtenu

-- Testing with original db
Nom_acteur
----------
Keitel
Willis
Novak
Stewart
Travolta
Lambert
Cage
DiCaprio
Cruise
Depp
Ricci
Nom_acteur
----------
Keitel
Willis
Novak
Stewart
Travolta
Lambert
Cage
DiCaprio
Cruise
Depp
Ricci

Tous les tests ont été réussis ! CorrectPoints pour cet envoi : 1,00/1,00. En tenant compte des tentatives précédentes, cela donne 0,90/1,00.
```

## Question 18  (Correct; Note de 1,00 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
SELECT C.Nom_cinema, C.Adresse
FROM Cinema C
WHERE C.Nom_cinema NOT IN (
    SELECT S.Nom_cinema
    FROM Seance S
    JOIN Film F ON S.ID_film = F.ID_film
    WHERE F.Nom_Realisateur = 'Tarantino'
);
```

**Retour Moodle :**

```
Feedback

Test
Résultat attendu
Résultat obtenu

-- Testing with original db
Nom_cinema  Adresse
----------  ----------------
Nations     3 Rue de Reuilly
Halles      Forum des Halles
Nom_cinema  Adresse
----------  ----------------
Nations     3 Rue de Reuilly
Halles      Forum des Halles

Tous les tests ont été réussis ! CorrectNote pour cet envoi : 1,00/1,00.
```

## Question 19  (Correct; Note de 0,90 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
SELECT sum(Capacite)
FROM Salle
WHERE Nom_cinema = 'Rex';
```

**Retour Moodle :**

```
Feedback

Test
Résultat attendu
Résultat obtenu

-- Testing with original db
sum(Capacite)
-------------
410
sum(Capacite)
-------------
410

Tous les tests ont été réussis ! CorrectPoints pour cet envoi : 1,00/1,00. En tenant compte des tentatives précédentes, cela donne 0,90/1,00.
```

## Question 20  (Correct; Note de 1,00 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
SELECT MIN(Annee), MAX(Annee) FROM Film WHERE Annee
```

**Retour Moodle :**

```
Feedback

Test
Résultat attendu
Résultat obtenu

-- Testing with original db
MIN(Annee)  MAX(Annee)
----------  ----------
1926        2000
MIN(Annee)  MAX(Annee)
----------  ----------
1926        2000

Tous les tests ont été réussis ! CorrectNote pour cet envoi : 1,00/1,00.
```

## Question 21  (Correct; Note de 0,60 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
SELECT Nom_cinema, sum(Capacite)
FROM Salle
GROUP BY Nom_cinema
ORDER BY Nom_cinema;
```

**Retour Moodle :**

```
Feedback

Test
Résultat attendu
Résultat obtenu

-- Testing with original db
Nom_cinema  sum(Capacite)
----------  -------------
Halles      195
Kino        530
Nations     280
Rex         410
Nom_cinema  sum(Capacite)
----------  -------------
Halles      195
Kino        530
Nations     280
Rex         410

Tous les tests ont été réussis ! CorrectPoints pour cet envoi : 1,00/1,00. En tenant compte des tentatives précédentes, cela donne 0,60/1,00.
```

## Question 22  (Correct; Note de 0,90 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
SELECT Nom_cinema, count(*)
FROM Salle
WHERE Climatise = 'O'
GROUP BY Nom_cinema
HAVING COUNT(*) > 1;
```

**Retour Moodle :**

```
Feedback

Test
Résultat attendu
Résultat obtenu

-- Testing with original db
Nom_cinema  count(*)
----------  --------
Kino        2
Rex         2
Nom_cinema  count(*)
----------  --------
Kino        2
Rex         2

Tous les tests ont été réussis ! CorrectPoints pour cet envoi : 1,00/1,00. En tenant compte des tentatives précédentes, cela donne 0,90/1,00.
```

## Question 23  (Correct; Note de 0,90 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
SELECT A.Nom, A.Prenom, count(*)
FROM Artiste A
JOIN Role R ON A.Nom = R.Nom_acteur
JOIN Film F ON R.ID_film = F.ID_film
WHERE F.Annee >= 1985
GROUP BY A.Nom, A.Prenom
HAVING COUNT(*) >= 3;
```

**Retour Moodle :**

```
Feedback

Test
Résultat attendu
Résultat obtenu

-- Testing with original db
Nom       Prenom  count(*)
--------  ------  --------
Travolta  John    3
Willis    Bruce   4
Nom       Prenom  count(*)
--------  ------  --------
Travolta  John    3
Willis    Bruce   4

Tous les tests ont été réussis ! CorrectPoints pour cet envoi : 1,00/1,00. En tenant compte des tentatives précédentes, cela donne 0,90/1,00.
```

## Question 24  (Correct; Note de 0,90 sur 1,00)

(énoncé vide)

**Mon code / ma réponse :**

```
SELECT C.Nom_cinema
FROM Cinema C
WHERE NOT EXISTS (
    SELECT F.ID_film
    FROM Film F
    WHERE F.Nom_Realisateur = 'Kubrick'
      AND NOT EXISTS (
          SELECT 1
          FROM Seance S
          WHERE S.Nom_cinema = C.Nom_cinema
            AND S.ID_film = F.ID_film
      )
)
ORDER BY C.ROWID;
```

**Retour Moodle :**

```
Feedback

Test
Résultat attendu
Résultat obtenu

-- Testing with original db
Nom_cinema
----------
Rex
Kino
Nations
Nom_cinema
----------
Rex
Kino
Nations

Tous les tests ont été réussis ! CorrectPoints pour cet envoi : 1,00/1,00. En tenant compte des tentatives précédentes, cela donne 0,90/1,00.
```
