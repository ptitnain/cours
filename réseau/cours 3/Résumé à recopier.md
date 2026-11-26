**LE JEUNE Louis — UID : ____________**
Réseaux Informatiques 1 — Chapitre 3 : La couche réseau, routage, FLSM et VLSM — 02/11/2026

---

### Partie 1 — Le paquet IPv4

La couche réseau livre les paquets de la source originale à la destination finale. Le protocole **IP** est sans connexion, fait de l'acheminement « au mieux », ne dépend pas du support et n'offre **aucune fiabilité** (pas d'accusé de réception).

L'IPv4 n'a que 2³² ≈ 4 milliards d'adresses, d'où la séparation entre adresses **publiques** (routées sur Internet) et **privées** (internes uniquement) : **10.0.0.0/8**, **172.16.0.0/12** et **192.168.0.0/16**. Le **NAT**, placé sur le routeur, traduit les adresses privées en l'adresse publique donnée par le FAI. Il existe aussi le **loopback** 127.0.0.1, pour tester sa propre pile TCP/IP, et le **lien local** 169.254.x.x (APIPA), que Windows s'attribue quand il n'y a pas de serveur DHCP.

Dans l'en-tête IPv4, il faut retenir : la **version** (4 ou 6), le **TTL**, décrémenté à chaque routeur (à 0, le paquet est rejeté), le **protocole** transporté (ICMP = 1, TCP = 6, UDP = 17) et les **@IP source et destination** (32 bits chacune).
L'IP source est toujours unicast. L'IP de destination peut être unicast, multicast (224 à 239) ou broadcast (adresse de diffusion).

### Partie 2 — Le routage

Un hôte peut s'envoyer un paquet à lui-même (loopback), l'envoyer à un hôte de son réseau (pas besoin de routeur) ou à un hôte distant : il passe alors par sa **passerelle par défaut**, c'est-à-dire « la porte » du réseau. Elle est donnée par DHCP ou configurée à la main, et crée une **route par défaut** dans la table de routage de l'hôte (`route print`).
Le routeur, lui, consulte sa table (`show ip route`) qui contient trois types de routes : **directement connectées** (C), **distantes** (apprises en statique S ou en dynamique, par exemple O pour OSPF) et la **route par défaut 0.0.0.0/0**, utilisée en dernier recours. Si aucune route ne correspond et qu'il n'y a pas de route par défaut, le paquet est abandonné. Quand plusieurs routes correspondent, le routeur choisit le **préfixe le plus long** (*longest prefix match*), car c'est la plus précise.
Le **routage statique** se configure à la main (`ip route <réseau> <masque> <next hop>`) : il est adapté aux petits réseaux, mais si un lien tombe, rien ne bascule. Le **routage dynamique** (OSPF, RIP, EIGRP…) découvre les réseaux tout seul et trouve un autre chemin en cas de panne.

### Partie 3 — Le sous-réseautage

Le routeur ne transmet pas les broadcasts : chaque interface de routeur délimite donc un **domaine de diffusion**. Si ce domaine est trop grand, les broadcasts saturent le réseau. On le découpe alors en **sous-réseaux** en empruntant des bits de la partie hôte. Chaque bit emprunté double le nombre de sous-réseaux et divise le nombre d'hôtes par deux.

**Tableau à mémoriser** ★ (à partir d'un /24) : /25 → 2 × 126 hôtes, /26 → 4 × 62, /27 → 8 × 30, /28 → 16 × 14, /29 → 32 × 6, /30 → 64 × 2.
Pour choisir le masque, il faut toujours compter **+2 adresses** (réseau et broadcast) : 15 hôtes demandent 17 adresses, donc un /27 et pas un /28.

- **FLSM** (masque fixe) : on choisit un seul masque qui satisfait à la fois le nombre de sous-réseaux et le plus grand besoin en hôtes. C'est simple, mais ça **gaspille** des adresses (un lien entre routeurs n'a besoin que de 2 adresses sur 30).
- **VLSM** (masque variable) : chaque sous-réseau reçoit le masque adapté à son besoin, **en commençant par le plus grand**. Les liens entre routeurs prennent un /30.

*Exercice* (192.168.100.0/24, VLSM) :

| Service | Besoin (+2) | Préfixe | @ réseau | Plage utilisable | Broadcast |
|---|---|---|---|---|---|
| Marketing | 32 | /27 | .0 | .1 – .30 | .31 |
| Ingénierie | 25 | /27 | .32 | .33 – .62 | .63 |
| Comptabilité | 17 | /27 | .64 | .65 – .94 | .95 |
| RH | 14 | /28 | .96 | .97 – .110 | .111 |
| SI | 10 | /28 | .112 | .113 – .126 | .127 |
