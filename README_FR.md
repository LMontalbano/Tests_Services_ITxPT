# Tests Services ITxPT

Projet d'un logiciel embarqué permettant de tester les services 
[NTP](https://wiki.itxpt.org/index.php?title=S02P02-Time_-_v2.1.1), 
[GNSS](https://wiki.itxpt.org/index.php?title=S02P03-GNSSLocation_-_v2.1.1), 
[AVMS](https://wiki.itxpt.org/index.php?title=S02P06-AVMS_-_v2.1.1) 
et [APC](https://wiki.itxpt.org/index.php?title=S02P07-APC_-_v2.1.1) 
de la norme [ITxPT](https://itxpt.org/) au
sein de la nouvelle flotte de bus électrique de 
[Keolis Métropole Orléans](https://www.reseau-tao.fr/index.php?).

## Qu'est-ce que l'ITxPT ?
Face à l'augmentation du nombre d'équipements embarqués au sein des transports public, un besoin de normaliser les
communications se fit sentir.
L'association [ITxPT](https://itxpt.org/) a été créé pour faciliter l'intégration et la communication entre les 
systèmes. Son rôle est d'accompagner tous les acteurs du marché des transports publics dans le déploiement des systèmes
informatiques plug and play, modulaire et avec une interopérabilité complète. 


## Démarrage

### Pré-requis

Il n'y a pas réellement de pré-requis afin d'utiliser le projet, vous pouvez retrouver un .exe du logiciel afin que
n'importe qui puisse ouvrir cet outil.

Néanmoins, si toute fois vous voulez modifier le code il vous faudra au minimum : 

- Python 3
- Les librairies présentes dans le [requirements.txt](https://github.com/LMontalbano/Tests_Services_ITxPT/blob/main/requirements.txt)

### Installation

Pour installer le logiciel sur votre machine il vous suffit, soit de **Cloner** 
le projet, soit de le **Télécharger** en [ZIP](https://github.com/LMontalbano/Tests_Services_ITxPT/archive/refs/heads/main.zip).

- Pour **Cloner** le projet vous pouvez exécuter la commande
``git clone https://github.com/LMontalbano/Tests_Services_ITxPT.git`` dans un terminal.
  

- Si vous choisissez de **Télécharger** le projet en 
[ZIP](https://github.com/LMontalbano/Tests_Services_ITxPT/archive/refs/heads/main.zip), rendez-vous dans vos
**Téléchargement**, puis dézippez le dossier ``Tests_Services_ITxPT.zip``. 

### Lancement du logiciel

Le chemin pour accéder au fichier exécutable est le suivant : ``Tests_Services_ITxPT/App/dist/``, ensuite vous pouvez
simplement double-cliquer sur le fichier ``Tests_Services_ITxPT.exe``.

Vous pouvez également lancer le logiciel via un terminal :
- ``$ cd Tests_Services_ITxPT/IHM``
- ``$ py Tests_Services_ITxPT.pyw``

## Utilisation
Une fois le logiciel démarrer, vous vous retrouverez face à cette fenêtre :


![Alt text](https://github.com/LMontalbano/Tests_Services_ITxPT/blob/main/Docs/app_screenshot.png?raw=true "app_screenshot")

Il y à différents éléments sur la fenêtre principale du logiciel, nous allons les détailler si dessous :

- Deux inputs :
  - **Local Address** : L'adresse IP local de la machine
  - **SAE Address** : L'adresse IP de l'UC SAE
	

- Le logo de Keolis Orléans Métropole


- Six boutons:
  - **Test NTP** : Lance 5 itérations du Test NTP ([détails](https://github.com/LMontalbano/Tests_Services_ITxPT/Docs/explanation/explanation_NTP.md))
  - **Test GNSS** : Lance 5 itérations du Test GNSS ([détails](https://github.com/LMontalbano/Tests_Services_ITxPT/Docs/explanation/explanation_GNSS.md))
  - **Test AVMS** : Lance le Test AVMS ([détails](https://github.com/LMontalbano/Tests_Services_ITxPT/Docs/explanation/explanation_AVMS.md))
  - **Cancel Test AVMS** : Permet de cancel le Test AVMS
  - **Test APC** : Lance le Test APC (_pas encore implémenté_) ([détails](https://github.com/LMontalbano/Tests_Services_ITxPT/Docs/explanation/explanation_APC.md))
  - **All Test** : Lance 5 itérations de chaque test les un après les autres
    

- Une fenêtre d'affichage
	

- Le lien github du projet

## Technologies utiliser
Le projet est entièrement codé en [Python](https://www.python.org/).

Pour la partie IHM, la librairie [Tkinter](https://docs.python.org/3/library/tkinter.html) a été choisie.

Pour la création du .exe, la librairie [PyInstaller](https://www.pyinstaller.org/) a été choisie.



## Status/ Versions
Le projet est en cours de développement et n'est pas encore en production.

## Auteurs
Liste des [contributeurs](https://github.com/LMontalbano/Tests_Services_ITxPT/graphs/contributors) : 
- Léonard Montalbano ([LMontalbano](https://github.com/LMontalbano))
- Pierre Lagarde ([avouspierre](https://github.com/avouspierre))

## License

Ce projet est sous licence ``MIT`` - voir le fichier [LICENSE.md](LICENSE.md) pour plus d'informations.


