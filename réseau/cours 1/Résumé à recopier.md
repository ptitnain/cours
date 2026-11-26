**LE JEUNE Louis — UID : ____________**
Réseaux Informatiques 1 (INF3050) — Chapitre 1 : Introduction aux réseaux informatiques
Séance du 05/10/2026 — M. Y. FAKIH

---

## ===== RECTO =====

### Partie 1 — Histoire et composants des réseaux

**1) Introduction**
Un réseau informatique est un ensemble d'équipements communicants (les hôtes) qui échangent des données grâce à des protocoles et du matériel réseau. L'objectif final est d'assurer une communication efficace des données.

**2) Historique**
- 1800 : télégraphe (Morse), usage militaire.
- 1900 : réseau téléphonique commuté (RTC) → transmission de la voix.
- 1960 : ARPA, des universités américaines sont reliées pour partager leurs données de recherche.
- 1972 : ARPANET est relié au réseau de la Défense → naissance d'Internet, qui devient public.
- 1980 → aujourd'hui : communication sans fil (générations mobiles jusqu'à la 4G/5G).

**3) Composants d'un réseau**
On distingue le *software* (services et applications : mail, WhatsApp, Teams…) et le *hardware*, les éléments physiques qui permettent au software de fonctionner en réseau :
- **Dispositifs terminaux** : à l'extrémité du réseau, ils sont la source ou la destination finale des données (PC, smartphone, imprimante, serveur, objets IoT : caméra IP, capteur…). Un serveur web est d'abord destination (requête) puis source (réponse).
- **Dispositifs intermédiaires** : ils assurent la transmission, la commutation, le routage et la gestion des flux entre les terminaux.
- **Médias** : *guidés* (filaires) → coaxial (plus utilisé), paire torsadée/Ethernet (pas chère mais sensible aux champs électromagnétiques et limitée à 100 m), fibre optique (plus rapide et plus longue distance, mais plus chère et plus délicate à installer). *Non guidés* (sans fil) → Wi-Fi, Bluetooth, 4G/5G : flexibles et faciles à installer, mais les antennes doivent être en vue directe.
  L'info est codée en impulsions électriques (cuivre), lumineuses (fibre) ou par modulation de l'onde radio (amplitude, fréquence, phase, polarisation).

**4) Évolution des dispositifs intermédiaires**
Relier 2 ou 3 PC directement suffit, mais ça ne passe pas à l'échelle (une carte réseau par liaison). D'où :
- **Répéteur** : régénère le signal qui s'atténue avec la distance.
- **Hub** : répéteur multiport (une « multiprise »), il renvoie tout sur tous les ports → congestion.
- **Bridge** : coupe le réseau en 2 segments et filtre le trafic entre eux.
- **Switch** : hybride hub + bridge, il envoie les données uniquement au destinataire grâce aux **adresses MAC** (dans un même LAN).
- **Routeur** : relie des réseaux différents en raisonnant sur les **adresses IP** (ex : box Internet). Le **pare-feu** est un routeur avec plus de sécurité qui filtre le trafic.

**5) Adresse IP**
Chaque hôte doit avoir une @IP, son identifiant unique. Chaque paquet contient une @IP source et une @IP destination, inversées lors de la réponse. Pour joindre un autre réseau, le paquet passe de routeur en routeur à travers Internet.

**6) Catégories de réseaux**
PAN (quelques mètres, Bluetooth) < **LAN** (maison, école, campus — géré par un particulier ou le service informatique) < MAN (une ville) < **WAN** (pays, monde — géré par les FAI : Orange, SFR…). Les WAN interconnectent les LAN.

---

## ===== VERSO =====

**7) Topologies** *(faire un petit dessin à côté de chacune)*
- **Bus** (un câble principal) : + simple, peu cher / – une coupure arrête tout.
- **Étoile** (point central : switch) : + gestion et ajout faciles, une panne de câble ne touche qu'un poste / – si le point central tombe, tout tombe.
- **Anneau** (chaque poste relié à 2 voisins) : + temps d'accès constant / – une coupure arrête le réseau, ajout difficile.
- **Maillée** (chaque poste relié à plusieurs ou tous les autres) : + très fiable, chemins redondants / – coût élevé, installation complexe (banques, militaire).

**8) Internet et accès**
**Internet** (I majuscule) = ensemble mondial de LAN et WAN interconnectés ; **internet** (i minuscule) = plusieurs réseaux interconnectés, pas forcément publics. On y accède toujours via un FAI (ISP).
- Particuliers : Dial-up → DSL → câble → 3G/4G/5G → fibre.
- Entreprises (débit plus élevé et garanti) : ligne louée, Metro Ethernet, DSL pro, satellite.

### Partie 2 — Adressage IPv4

**9) L'adresse IPv4**
32 bits = 4 octets de 8 bits, écrits en décimal et séparés par des points (ex : 192.168.10.10). Elle est composée :
- d'une **partie réseau**, identique pour tous les hôtes d'un même réseau ;
- d'une **partie hôte**, unique pour chaque hôte (sinon conflit d'adresses).
Calculatrice interdite → conversion binaire à la main (128 64 32 16 8 4 2 1).

**10) Masque de sous-réseau**
C'est une @IPv4 spéciale : une suite de **1** (partie réseau) suivie de **0** (partie hôte). On l'écrit aussi avec la longueur du préfixe, le nombre de bits à 1 : 255.255.255.0 = **/24**. Une @IP se donne toujours avec son masque.

**11) Méthode de calcul (à retenir)**
- **@ réseau** = @IP **ET** masque, bit à bit (1 ET 1 = 1, sinon 0)
- **1er hôte** : partie hôte = 0…0**1**
- **Dernier hôte** : partie hôte = 1…1**0**
- **@ de diffusion** (broadcast) : partie hôte = 1…11 → joint tous les hôtes du réseau
- **Nombre total d'@** = 2^(32 − préfixe)
- **Nombre d'hôtes** = 2^(32 − préfixe) − 2 (on retire l'@ réseau et le broadcast)

*Exemple* : 192.168.10.10/23 (masque 255.255.254.0, 9 bits hôte)
→ réseau 192.168.10.0 / 1er 192.168.10.1 / dernier 192.168.11.254 / broadcast 192.168.11.255
→ 2⁹ = 512 adresses, 512 − 2 = 510 hôtes.

*Mon exercice* (né le 03/12/2005 → x = 12, y = 3, z = 200) : **120.12.3.200/27**
Les 3 premiers octets du masque valent 255, ils ne changent pas → on travaille seulement sur le dernier octet :
- 200 = 110|01000 et masque /27 = 255.255.255.224 → 224 = 111|00000
- @ réseau : 110|00000 = **120.12.3.192**
- 1er hôte : 110|00001 = **.193** / dernier : 110|11110 = **.222** / broadcast : 110|11111 = **.223**
- Plage attribuable : 120.12.3.193 → 120.12.3.222 ; 2⁵ = 32 adresses, 32 − 2 = **30 hôtes**
- En **/28** (masque 240 = 1111|0000) : réseau .192, plage .193 → .206, broadcast .207 ; 2⁴ = 16 adresses, **14 hôtes**

**12) Passerelle par défaut**
C'est l'adresse du routeur dans notre réseau (elle prend une des adresses d'hôte). Inutile pour une communication locale, mais indispensable pour sortir vers un autre réseau ou Internet : c'est la « porte de sortie » du réseau.
