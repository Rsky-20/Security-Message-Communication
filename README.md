# Security-Message-Communication
![Logo](https://drive.google.com/u/1/uc?id=1_RBn08Q8TRMmDEA_SXCWhVPL9TN0cznh&export=download)
> # Description du projet
    Le Porjet Security Message Community est une messagerie instannée basé sur le module socket.
    SMC permet à deux personnes, pocédant le client fournie, de dialoguer de façon sécurisé et 
    instantanné à traver une interface console.
    
> # Utilisation
    Afin de pouvoir jouir pleinnement du projet, il faut un environnement python configuré avec les 
    modules : datetime, select, socket.
    Une fois ces modules correctement installé dans votre environnement python,
    lancé votre IDLE ou autre programme similaire permettant d'ouvrir et lancé python.
    Python 3.5 ou supérieur est nécessaire pour le bon fonctionnement du projet
    
    > sur console cmd ou PowerShell : 
    
        --> console 1 (console serveur):
            PS C:\WINDOWS\system32> cd /le/chemin/de/votre/server
            PS C:\le\chemin\de\votre\server> python server.py  
            
        Le serveur est prêt à recevoir les messages qui lui seront envoyé afin de les stocker et 
        translettre à l'autre client
            
            
        --> console 2 et 3 (console client):
            PS C:\WINDOWS\system32> cd /le/chemin/de/votre/clientA|clientB
            PS C:\le\chemin\de\votre\clientA|clientB> python clientA|B.py  (nommé client.py)
        
        Le client A se connecte au serveur et est en attente 
        Une fois que le client B s'est connecté, le dialogue peut commencer.
        
                                                        _________________________________________________
     
    > sur Pycharm ou IDLE :
        Executé les fichier python dans l'ordre suivant:
            > serveur.py --> client A --> client B
        
        Le serveur sera sur écoute, le client A puis le client B seront connecté au serveur et prêt pour emploit
***
        
Le client A (client qui se connecte en premier) doit obligatoirement commencer la discussion.
Le client B pourra alors aussi envoyer un message après  que le client A ai envoyé son message.

Les clients auront 1 messages de décallage. 

***
## [Fonctionnement du projet]

Le projet fonctionne grace au module socket. On a 3 programmes / script distint, le serveur, le client A et le client B.
Dans la version actuelle, le projet n'accepte que 2 client de façon opérationnel (au delà de 2 la messagerie 
instantannée sera innopérant).
Le serveur est conçu pour accepter n client, leur dialogue est basé sur le principe du ping-pong.
L'utilisateur George écrit son message sur le client A, le message passe par un algoritme de chiffrement directement 
intégré au client A. Puis le client connecté au serveur envoie le message chiffré à celui-ci. Le serveur reçoit 
le message chiffré et la stocke sur un fichier log.txt uniquement géré par le serveur. Le serveur renvoie au client A
le dernier message reçu avant celui envoyé par le client A. Une fois le message envoyé c'est au tour du Jacque qui a 
le client B d'interragir avec le serveur.

Pour plus d'information sur le code, merci de bien vouloir lire la documentation dans le code.

---

### Partie Requête 

> Notre projet comporte deux type de requêtes formant la communication ou canal.
    Requête 1 : la requête envoyé par le client au serveur. A ce moment là le client envoie le message déjà chiffré 
    au serveur et le serveur reçoit 
    Requête 2 : La requête 'Réponse' est l'envoie des données contenues et stockés par le serveur vers le client

Il y'a bien 2 requêtes pour une communication entre client/serveur.
Donc afin de communiquer, le shéma de communication se répète. Un client envoie puis reçoit et attend de pouvoir 
re-communiquer avec le serveur une fois qu'il sera disposé à communiquer (une fois que l'autre client aura finit sa 
communication avec le serveur).

Exemple des requêtes de façon générale  :
    
    Démarrage Serveur
    Démarrage Client A puis connexion
    George utilise le client A
    Démarrage Client B puis connexion
    Jacque utile le client B
    
    Communication Client A / Serveur
    
    Client A => envoie un message donnée par l'utilisateur (déjà chiffré en amont)
    Serveur => Reçoit les donnée du Client A puis les traites (il les stocks et les met dans un format utilisable)
    
    Serveur => Envoie le format utilisable au Client A 
    Client A traite l'information
    
    _______________________________
    
    Communication Client A / Serveur
    
    Client B => envoie un message donnée par l'utilisateur (déjà chiffré en amont)
    Serveur => Reçoit les donnée du Client B puis les traites (il les stocks et les met dans un format utilisable)
    
    Serveur => Envoie le format utilisable au Client B 
    Client B traite l'information
    
    ________________________________
    
    Le dernier message présent sur le serveur étant celui du Client A, le Client B a donc bien le message de son ami
    
Exemple concrêt des requêtes :

    Démarrage Serveur
    Démarrage Client A puis connexion
    George utilise le client A
    Démarrage Client B puis connexion
    Jacque utile le client B
    
    Client A => Chiffre : Bonjour Jacque, c'est George 
    (après chiffrement)=> Envoie : 2020-11-20T12:28:53.316399|[CLIENT 127.0.0.1:52420]@vox)oPZEOmf'P[ZEfI[j-E0[oZb[
    
    Serveur => Reçoit : 2020-11-20T12:28:53.316399|[CLIENT 127.0.0.1:52420]@vox)oPZEOmf'P[ZEfI[j-E0[oZb[
    Serveur => Traite ce qu'il a reçu
    Serveur => Envoie : {du vide car il n'y avait pas de message enregistré avant}
    
    Client A => Reçoit : {du vide car il n'y avait pas de message enregistré avant}
    Client A => Dechiffre : {du vide car il n'y avait pas de message enregistré avant}
    
    __________________________________
    
    Client B => Chiffre : Bonjour George, comment vas-tu ? 
    (après chiffrement)=> Envoie : 2020-11-20T12:35:07.286946|[CLIENT 127.0.0.1:52421]@vox)oPZE0[oZb[ZEfoyy[x-ECmj4-PE_
    
    Serveur => Reçoit : 2020-11-20T12:35:07.286946|[CLIENT 127.0.0.1:52421]@vox)oPZE0[oZb[ZEfoyy[x-ECmj4-PE_
    Serveur => Traite ce qu'il a reçu
    Serveur => Envoie :[CLIENT 127.0.0.1:52420]@vox)oPZEOmf'P[ZEfI[j-E0[oZb[
    
    Client B => Reçoit :[CLIENT 127.0.0.1:52420]@vox)oPZEOmf'P[ZEfI[j-E0[oZb[
    Client B => Dechiffre : Bonjour Jacque, c'est George
    
    Voilà ! George et Jacque communiquent ensemble.
    
### Schéma Requête
![img](https://drive.google.com/u/0/uc?id=1R4cPoFPLW0rEQL7jQ7qNs6pqlG9m9eQE&export=download)


    

    
