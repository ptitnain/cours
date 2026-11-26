# Contexte général : cours 2026-2027

## Qui / quoi
- École : **ESIEA Paris**, cycle ingénieur, **3e année (3A) en FISA**, c'est-à-dire en alternance (apprentissage). Semestre **S05** (sept. 2026 à janv. 2027).
- Groupes de TP FISA numérotés 34 à 39.
- Moodle de l'école : https://learning.esiea.fr/my/ (le Moodle est la source des PDF de ce dossier).
- Les PDF ont été récupérés depuis Moodle le 26/11/2026. Ils sont rangés par matière, puis par section Moodle (même nom que la section sur Moodle).

## Organisation du dossier
| Dossier | Module Moodle | Code |
|---|---|---|
| `réseau/` | Réseaux informatiques (Réseaux Informatiques 1) | INF3050 |
| `systèmes d'exploitation/` | Systèmes d'exploitation (Linux) | INF3039 |
| `architecture microprocesseur/` | Architecture d'un système à microprocesseur | SYS3041 |
| `bases de données/` | Bases de données | INF3031 |
| `probabilités et statistiques/` | Probabilités et Statistiques | MAT3055 |
| `java POO/` | Programmation orientée objet en Java | INF3132 |
| `traitement du signal/` | Traitement numérique du signal et applications | SYS3045 |
| `anglais/` (+ `anglais/TOEIC/`) | Anglais 3A FISA S05 + préparation TOEIC | LAN3081 |
| `PAIRSE projet RSE/` | PAIRSE, Projet à impact RSE (gestion de projet agile) | HUM3091 |
| `PASS remise à niveau/` | Remises à niveau 3A : électronique, informatique (Java), maths | SYS3043, INF3036, PLU3198 |

Chaque dossier contient un `CONTEXTE.md` qui résume le contenu du cours et liste les supports.

## Façon de travailler de l'étudiant (vu dans `réseau/`)
- Un sous-dossier par séance (`cours 1`, `cours 2`, ...).
- Enregistrements audio du cours (`.m4a`) puis transcriptions (`.txt`, Whisper « Large-v3-turbo » / Google).
- Un **« Résumé à recopier.md »** par chapitre : résumé rédigé, en français, en paragraphes avec mots-clés en gras, à recopier à la main (en-tête : nom, UID, module, chapitre, date). Converti en HTML avec `réseau/md2html.py`.
- Schémas SVG dans `schemas/` quand c'est utile.
Ce même format peut être réutilisé pour les autres matières.

## Non récupéré (volontairement)
- Espaces non pédagogiques : International, APIC, Promotion 3A, ESIEA Talents, Formation en entreprise.
- Fichiers non-PDF (docx, pptx, mp3, zip, installeurs...) : ils restent sur Moodle, et chaque `CONTEXTE.md` les signale.
- Anglais renforcé (groupe C) : pas de PDF sur Moodle (seulement docx/odt/pptx).

## Relectures des quiz/TP Moodle
Les TP et quiz faits en ligne sur Moodle (questions, mes réponses, note, correction et retour de Moodle) sont exportés en Markdown dans `<matière>/relectures quiz et TP Moodle/` : bases de données (quiz intro, QCM SQL, TP2, exercices supplémentaires), systèmes d'exploitation (TP1 à TP3), java POO (Q2.x à Q4.x, TD1 à TD3, TP1). Récupérés le 26/11/2026. Les quiz pas encore tentés (examens blancs, SE TP4, Java Q1.x...) n'ont pas de relecture.

## PDF scannés (sans texte)
Certains PDF sont des images sans texte (électronique « cours 2026 » sauf Arduino, TD Bode, TP Arduino, supports d'anglais In Company U10, TOEIC Target Score, guides Remote TOEIC). Pour les étudier, il faut les ouvrir et les lire visuellement.

## Graphe de connaissances
Le graphe graphify du dossier est dans `graphify-out/` (voir `graphify-out/GRAPH_REPORT.md`).
