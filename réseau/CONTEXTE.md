# Réseaux Informatiques 1 (INF3050), 3A FISA

- **Enseignants** : Youssef FAKIH (responsable), Ali Awarkeh.
- **But du module** : passer de la compréhension des réseaux à leur conception, configuration et diagnostic (Ethernet, IP, transport, applications ; adressage, routage, services ; lecture des tables et captures).
- **Outils** : Cisco Packet Tracer, Wireshark, routeurs Cisco 4321 en salle I402/I403, PC Ubuntu (Telnet, SSH), Safe Exam Browser pour les évaluations.
- **Références** : Kurose & Ross, *Computer Networking: A Top-Down Approach* (7e éd.) ; Forouzan, *Data Communications and Networking* (5e éd.) ; Cisco ITN v7.

## Chapitres (cours magistraux)
| Dossier | Chapitre | Contenu |
|---|---|---|
| `cours 1/` (02/10) | Ch. 1, Introduction aux réseaux | Types de réseaux, composants, topologies, notions d'adressage, passerelle par défaut |
| `cours 2/` (07/10) | Ch. 2, Modèles des réseaux | OSI vs TCP/IP, encapsulation, couche physique, couche liaison (trame Ethernet, MAC), fonctionnement d'un switch |
| `cours 3/` (02/11) | Ch. 3, Couche réseau | Paquet IPv4, adresses publiques/privées, NAT, routage, sous-réseautage FLSM et VLSM |
| `cours 4/` (25/11) | Ch. 4, Communication locale et distante | Construction paquet + trame (MAC de destination = passerelle en distant), DNS, ARP, ICMP, DHCP |

Chaque dossier `cours N` contient : le PDF du chapitre, les enregistrements `.m4a` et leurs transcriptions `.txt`, et un **`Résumé à recopier.md`** (+ `.html`) rédigé à partir du cours. `cours 4/135.pdf` est une fiche perso sur le chapitre 4.

## `supports moodle/` (téléchargé depuis Moodle)
- `Généralités/` : Chapitre 0 (objectifs, programme, évaluation) et liste UID/groupes de la promo.
- `Information Utile/` : checklist PC, éléments à installer, configuration IP (Linux/Windows), plan des salles, réinitialisation d'un routeur Cisco 4321.
- `References/` : les deux livres de référence en entier (Kurose, Forouzan).
- `Activités/` : activité ARP (fichier `.pkt` Packet Tracer associé, resté sur Moodle).
- TP :
  - **TP1** : paramétrage IP et accès distant (hub, Telnet vs SSH, analyse Wireshark).
  - **TP2** : configuration LAN et routage inter-réseaux (dimensionnement IPv4, Linux/Windows).
  - **TP3** : routage Linux et NAT (FLSM).
  - **TP4** : ARP et compagnie (VLSM, ARP local/distant, captures).
  - **TP5** : architecture, adressage et routage statique sur Cisco 4321.
  - **TP6** : routage statique, DHCP/PAT, analyse ARP-ICMP.
  - Les fichiers « Répartition ... » donnent les sous-groupes par groupe FISA (34 à 39).

## Restés sur Moodle
Installeurs Cisco Packet Tracer, liens vidéo FLSM/VLSM, « Réseau d'une PME », inscription au tutoriel Packet Tracer.
