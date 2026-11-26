**LE JEUNE Louis — UID : ____________**
Réseaux Informatiques 1 — Chapitre 4 : Communication Réseau Local & Réseau Distant — 25/11/2026

---

### Partie 1 — Construction Paquet & Trame

Pour envoyer un message, il faut remplir **4 adresses** : deux dans l'en-tête du paquet et deux dans l'en-tête de la trame.

Le **paquet est toujours le même**, en local comme en distant :
- **IP source** : celle de l'envoyeur ;
- **IP destination** : celle du PC final.

Pour la **trame**, seule la **MAC destination change** :
- en **local**, on envoie directement au PC final, donc c'est **sa MAC** ;
- en **distant**, on envoie d'abord au routeur, donc c'est la **MAC de la passerelle**. Le routeur refait ensuite une trame pour la suite.

La première fois qu'on veut communiquer, deux informations sont inconnues : l'**IP de destination**, trouvée grâce au **DNS**, et la **MAC de destination**, trouvée grâce à l'**ARP**.

### Partie 2 — Le DNS

C'est plus simple de retenir un nom comme *google.com* qu'une suite de chiffres. Le **serveur DNS traduit donc le nom de domaine en adresse IP** et inversement. Le PC lui envoie une **requête DNS** et reçoit une **réponse** avec l'IP.

### Partie 3 — ARP

L'**ARP** trouve la **MAC qui correspond à une IP**. Chaque PC a une **table ARP**, gardée en RAM, qui garde les correspondances IP/MAC déjà trouvées : elle est vidée au redémarrage. En local, on cherche la MAC du PC final, en distant, celle de la passerelle.

Si l'IP n'est pas dans la table, le PC met son message en attente et envoie une **requête ARP** à tout le réseau local.
Chaque machine la reçoit et compare l'IP cible à la sienne : si ce n'est pas elle, elle rejette. Seule la bonne machine répond avec une **réponse ARP** qui contient sa MAC, envoyée directement au demandeur. Le PC met alors sa table à jour et envoie son message.

★ **Requête ARP = broadcast** (envoyée à tout le réseau local).
★ **Réponse ARP = unicast** (envoyée directement au demandeur).

**ARP spoofing** : un attaquant envoie une fausse réponse ARP avec sa propre MAC à la place de celle d'une autre machine. Le PC enregistre la mauvaise MAC et lui envoie tous ses paquets. Certains switchs s'en protègent.

### Partie 4 — ICMP

L'IP ne garantit pas que les données arrivent, donc l'**ICMP** sert à **signaler les problèmes** sur le réseau. Trois messages à retenir :
- **Echo request / reply** (types 8 et 0) : utilisés par le **ping** pour tester si une machine répond ;
- **Destination inaccessible** (type 3) : code 0 = réseau, 1 = hôte, 2 = protocole, 3 = port ;
- **Délai dépassé** (type 11) : envoyé quand le **TTL tombe à 0**.

**Ping** : on teste dans l'ordre :
1. son propre PC (127.0.0.1) ;
2. la passerelle ;
3. une machine sur un réseau distant.

Le premier ping rate souvent car le PC doit d'abord trouver la MAC avec l'ARP. Si le ping ne marche pas, la machine peut quand même être joignable : beaucoup de routeurs et pare-feu bloquent l'ICMP.

### Partie 5 — DHCP

Le **DHCP** donne **automatiquement** une configuration réseau aux PC : une **IP**, le **masque**, la **passerelle** et le **DNS**. Le serveur prend dans un **pool d'adresses** et les **loue** pour une durée limitée, le **bail**. Si le bail n'est pas renouvelé, l'adresse revient dans le pool.

★ Les 4 messages, à retenir avec **DORA** :
1. **Discover** : le client cherche un serveur DHCP en broadcast ;
2. **Offer** : le serveur propose une IP ;
3. **Request** : le client accepte cette IP ;
4. **Ack** : le serveur confirme.

Pour **renouveler** son bail, le PC n'a généralement besoin que de deux messages : **Request** puis **Ack**.
