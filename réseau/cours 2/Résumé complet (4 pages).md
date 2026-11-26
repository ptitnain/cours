**LE JEUNE Louis — UID : ____________**
Réseaux Informatiques 1 (INF3050) — Chapitre 2 : Modèles des réseaux, couche physique, couche liaison de données
Séance du 07/10/2026 — M. Y. FAKIH

---

## ===== FEUILLE 1 — RECTO =====

### Partie 1 — Modèles OSI et TCP/IP

**1) Encapsulation** (analogie de la lettre)
Comme deux personnes doivent parler la même langue, deux machines doivent suivre les mêmes **protocoles** (règles, normes) : format et ordre des messages, actions à l'envoi et à la réception.
Encapsuler = placer un format de message dans un autre, comme une lettre dans une enveloppe. Il faut **4 adresses** pour envoyer un message :
- dans la lettre : « Bonjour Florian » = **@IP destination**, la signature « Youssef » = **@IP source** → adresses **logiques**, dans le **paquet** ;
- sur l'enveloppe : adresse du destinataire = **@MAC destination**, adresse de l'expéditeur = **@MAC source** → adresses **physiques**, dans la **trame**.
La trame est l'enveloppe qui transporte le paquet. Si l'adresse ou le format est faux, le message n'est pas livré.

**2) Modes de livraison**
- **Unicast** (monodiffusion) : 1 source → 1 destinataire
- **Multicast** (multidiffusion) : 1 source → un groupe (pas vu en détail)
- **Broadcast** (diffusion) : 1 source → tout le monde

**3) Pourquoi un modèle en couches ?**
Prendre l'avion est un système complexe : on le découpe en couches (billet, bagages, passager, vol), chacune avec une fonction au départ et la fonction inverse à l'arrivée. Avantages :
- une modification reste **locale** à sa couche → maintenance plus simple ;
- le système devient **universel** → **interopérabilité** : des PC Dell, HP ou Asus communiquent entre eux.
Une couche = un sous-problème ; plusieurs protocoles peuvent appartenir à la même couche s'ils le résolvent de façons différentes.

**4) Modèle OSI (théorique) et TCP/IP (pratique)** ★ *(dessiner le tableau)*

| N° | OSI | TCP/IP | PDU |
|---|---|---|---|
| 7 | Application | | Données |
| 6 | Présentation | Application | Données |
| 5 | Session | | Données |
| 4 | Transport | Transport | Segment |
| 3 | Réseau | Réseau | Paquet |
| 2 | Liaison de données | Liaison de données | Trame |
| 1 | Physique | Physique | Bits |

- L'ancien TCP/IP a 4 couches (application, transport, internet, accès réseau = physique + liaison regroupées). Celui à 5 couches est le même, il sépare juste ces deux couches. **On utilise celui à 5 couches.**
- Les **numéros de couche** n'existent que dans l'OSI : « couche 3 » = forcément OSI.
- **PDU** (unité de protocole de données) = nom du message à chaque couche ★ question d'exam.

**5) Encapsulation complète (communication web)**
Données HTTP → **segment TCP** (+ ports) → **paquet IP** (+ @IP) → **trame Ethernet** (+ @MAC en en-tête, CRC en queue) → **bits**.
- Envoi : de **haut en bas** (on ajoute un en-tête à chaque couche).
- Réception : de **bas en haut** (on retire les en-têtes = désencapsulation).

---

## ===== FEUILLE 1 — VERSO =====

**6) Rôle de chaque couche**
- **Physique (1)** : transporte des 0 et des 1 d'un point A à un point B, sans comprendre leur contenu (comme un chauffeur de bus qui ne sait pas où on descend).
- **Liaison de données (2)** : transmission des **trames d'un saut au saut suivant sur le lien local** (*hop-by-hop*) grâce aux **@MAC**. Pour nous, un saut = un routeur (un switch n'est pas un saut).
- **Réseau (3)** : transmission des **paquets de bout en bout** (*end-to-end* : de la source originale à la destination finale) grâce aux **@IP**, + le **routage**.
- **Transport (4)** : identifie les **flux / services** grâce aux **numéros de port**. Ex : YouTube et Netflix ouverts en même temps → même IP, même MAC, mais ports différents. **UDP** = rapidité (jeux, live) / **TCP** = fiabilité (mails, données à ne pas perdre).
- **Session (5)** : identifie l'**utilisateur** indépendamment des couches inférieures (IP, MAC, port). Ex : on reste connecté à Instagram en changeant de réseau.
- **Présentation (6)** : formatage (ASCII, UTF-8…), compression, chiffrement.
- **Application (7)** : interface entre l'utilisateur et le réseau (sans l'appli WhatsApp, pas de message WhatsApp).

→ En pratique, les applications gèrent elles-mêmes (ou pas) la session et la présentation : c'est pour ça que TCP/IP regroupe les couches 5, 6 et 7 en une seule couche application.
→ **L'IP dit où aller, la MAC dit comment y aller physiquement** : les deux sont complémentaires.

**7) Exemple : combien de trames ?** ★ exam *(recopier le schéma)*
PC-A (192.168.1.10, MAC AA) → R1 → R2 → R3 → PC-B (172.16.1.20, MAC 22).
3 routeurs → 4 réseaux → **4 trames**.

| Trame | MAC dest | MAC source | Paquet IP |
|---|---|---|---|
| 1 : PC-A → R1 | BB-BB | AA-AA | 192.168.1.10 → 172.16.1.20 |
| 2 : R1 → R2 | DD-DD | CC-CC | identique |
| 3 : R2 → R3 | FF-FF | EE-EE | identique |
| 4 : R3 → PC-B | 22-22 | 11-11 | identique |

- Les **@MAC changent à chaque routeur**, les **@IP ne changent jamais**.
- Chaque **interface** d'un routeur a sa propre @MAC.
- Le routeur vérifie que la MAC destination est la sienne, désencapsule, lit l'IP destination, consulte sa **table de routage** puis réencapsule dans une nouvelle trame (route inconnue → paquet abandonné).

**Équipements par couche** : hub = couche 1 / switch = couche 2 (lit seulement les MAC → **commutation intra-réseau**) / routeur = couche 3 (lit les MAC et les IP → **routage inter-réseau**).

---

## ===== FEUILLE 2 — RECTO =====

### Partie 2 — La couche physique

**8) Rôle** : il faut au minimum une **carte réseau (NIC)**. La couche physique transforme les bits en signaux (électriques, lumineux ou ondes radio), les envoie sur le support, puis reconvertit les signaux reçus en bits.

**9) Bande passante, débit, latence** ★ *(analogie de l'autoroute)*
- **Bande passante** : capacité **maximale théorique** (autoroute à 100 ou 1000 voies). Ce n'est pas une vitesse : les bits voyagent à la même vitesse (≈ 0,64 × c) en 100 Mbit/s comme en 1 Gbit/s.
- **Débit** (*throughput*) : ce qui passe réellement → toujours < bande passante.
- **Débit applicatif** (*goodput*) : débit − signalisation (en-têtes, accusés, retransmissions) = les voitures de police qui prennent de la place sans transporter de vraies données → toujours < débit.
- **Latence** : temps pour que les données aillent de A à B.
- Le débit est limité par le **lien le plus lent** du chemin (goulot d'étranglement).

**10) Câbles en cuivre**
- **Coaxial** : ancien (Internet + TV), sert encore pour les antennes et le satellite.
- **Paire torsadée** : 8 fils = 4 paires, connecteur **RJ-45**, pas chère mais limitée à 100 m. Deux perturbations :
  - **diaphonie** (*crosstalk*) : un fil « entend » son voisin à cause du champ magnétique induit → la **torsade** annule en partie ces champs ;
  - **interférences EMI/RFI** : ex. box posée sur un micro-ondes (tous deux à 2,4 GHz).
- **UTP** = non blindé (utilisé en TP) / **STP** = blindé, plus cher, mieux protégé.

**11) Câble droit, croisé ou rollover** ★ TP
- **Droit** : équipements différents → PC–switch, switch–routeur.
- **Croisé** : équipements identiques → switch–switch, PC–PC, routeur–routeur, **+ PC–routeur** (exception).
- **Rollover** (Cisco) : PC → port console d'un switch ou d'un routeur, pour le configurer.
Les routeurs Cisco 4321 du TP n'ont pas l'**auto-MDIX** (qui adapte le câble tout seul) → il faut choisir le bon câble.

**12) Fibre optique** : impulsions lumineuses, totalement insensible aux EMI/RFI.
- **Monomode (SMF)** : un seul faisceau, **laser**, plus cher et plus performant.
- **Multimode (MMF)** : plusieurs faisceaux, **LED**, dispersion → moins performant mais moins cher.
- UTP : jusqu'à 10 Gbit/s sur 100 m, peu cher / fibre : jusqu'à 100 Gbit/s sur des km, plus chère et délicate à installer.

**13) Sans fil** : support **partagé** → interférences, et n'importe qui peut capturer les paquets (il faut chiffrer).

### Partie 3 — La couche liaison de données

**14) Fonctions** (en plus du transport des trames saut par saut)
- **Contrôle d'erreur** : le récepteur recalcule le **CRC** et le compare à celui reçu en fin de trame → différent = trame rejetée et retransmise.
- **Contrôle de flux** : adapter son débit à la capacité de la destination (PC à 10 Gbit/s → serveur à 10 Mbit/s = saturation) et à la **congestion** du réseau.

---

## ===== FEUILLE 2 — VERSO =====

**15) Trame Ethernet 802.3** ★ exam (Wireshark)
| Préambule + SFD (8 o) | MAC dest (6 o) | MAC source (6 o) | Type (2 o) | Données (46 à 1500 o) | FCS / CRC (4 o) |
- Préambule + SFD = synchronisation, **invisibles dans Wireshark**.
- Dans Wireshark : **6 premiers octets = MAC destination** (toujours en premier), 6 suivants = MAC source, puis le type (**0x0800 = IPv4**).
- **MTU = 1500 octets** de données max (3010 o → 3 trames). Moins de 46 o → **padding** (on complète avec des 0).
- IEEE 802 : 802.3 = Ethernet, 802.11 = Wi-Fi, 802.15 = Bluetooth.

**16) Hub et @MAC**
Le hub renvoie chaque trame à tous les PC (vu sur Packet Tracer) → un PC non concerné reçoit les données = **atteinte à la confidentialité**. D'où les @MAC : on ne traite une trame que si elle nous est adressée.
- **@MAC = 48 bits = 6 octets = 12 chiffres hexa**, gravée dans la ROM de la carte.
- 3 premiers octets = **OUI** (donné par l'IEEE au fabricant) + 3 derniers uniques → unique au monde.
- Unique **par interface**, pas par appareil (Ethernet, Wi-Fi, Bluetooth ont chacun la leur). Voir les siennes : `ipconfig /all`.
- Notations : `00-60-70-09-B4-95` (Windows), `00:60:70:09:B4:95` (Linux), `0060.7009.B495` (Cisco).

**17) Envoi d'une trame** : MAC source = celle de la carte qui envoie. MAC destination :
- broadcast → `FF-FF-FF-FF-FF-FF` (et `00-00-00-00-00-00` = MAC inconnue, voir ARP) ;
- multicast → commence par `01-00-5E` ;
- unicast → MAC du destinataire s'il est sur **le même réseau**, sinon MAC de la **passerelle par défaut**.

**18) Réception d'une trame** ★ : le PC lit d'abord la **MAC destination** → broadcast : accepte / multicast : seulement s'il est membre du groupe / unicast : MAC dest = la sienne → accepte, sinon → rejette.

### Partie 4 — Fonctionnement d'un switch
Son « cerveau » = la **table d'adresses MAC** : **@MAC ↔ n° de port**, **vide à l'allumage**. Deux phases :
1. **Apprentissage avec la MAC source** : inconnue → ajoutée avec le port d'arrivée ; déjà connue → minuterie remise à zéro.
2. **Transfert avec la MAC destination** : inconnue ou broadcast → envoi sur **tous les ports sauf celui d'arrivée** / connue → envoi **uniquement sur son port**.
Le switch n'apprend un PC que si une trame de ce PC passe par lui.

**Exercice** : PC-A (S1 Fa0/1) envoie à PC-B (S1 Fa0/3), puis PC-B répond. S1 Fa0/4 ↔ S2 Fa0/1.
- A → B : S1 apprend A sur Fa0/1 et inonde ; S2 apprend A sur Fa0/1 et inonde.
- B → A : S1 apprend B sur Fa0/3 et connaît A → envoie seulement sur Fa0/1. S2 ne voit rien passer.
- **Résultat** : S1 = `0060.7009.B495 → Fa0/1`, `00D0.9772.82E3 → Fa0/3` / S2 = `0060.7009.B495 → Fa0/1`.
