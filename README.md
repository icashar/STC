🏎️ Système tours-Chrono
==============================

Ce projet a été développé dans le cadre d'un défi de conception en géni, dont l'objectif était de créer un système de suivi des tours fiable et économique pour une compétition de courses de voitures télécommandées entre étudiants Les systèmes commerciaux étant trop coûteux et complexes, nous avons conçu une solution sur mesure utilisant un capteur de lumière à l'arrivée et des carrosseries de voiture imprimées en 3D avec un code couleur pour détecter le passage de chaque voiture.

Le système enregistre le nombre de tours, les temps au tour et détermine le vainqueur de la course. Il comprend également une interface simple pour afficher le classement actuel et la progression de la course en temps réel, conçue pour être lisible et conviviale pendant l'événement.

Ce projet a mis l'accent sur la simplicité, la performance et l'apprentissage pratique grâce à des capteurs, à Arduino et à une conception d'interface utilisateur simple.

Notre MakerRepo: https://makerepo.com/EthanLeroux/2423.systme-chronotours

Instructions - Détection de Couleur
=========================

Partie 1 : WebServer dans Arduino IDE
-------------------------------------
1. Ouvrez Arduino IDE et ouvrez le fichier **ColorDetectionTest**.
2. Remplacez le SSID et le mot de passe par votre identifiant réseau.
3. Sélection du module ESP32 :
   - Allez dans **Outils → Carte**.
   - Sélectionnez **ESP32 WROVER Module**.
   - Définissez **Partition Scheme** sur « Huge APP (3MB No OTA) ».
   - Définissez **Upload Speed** sur « 115200 ».
4. Assurez-vous que la carte est bien **ESP32 Wrover Kit** et qu’un port **COM** approprié est sélectionné.
5. Maintenez le bouton **Reset** de l’ESP32 enfoncé et cliquez sur **Upload**.
6. Maintenez le bouton Reset enfoncé.
7. Lorsque la console affiche **"Connecting…"**, relâchez le bouton Reset.
8. Attendez que la console affiche **"Hard Resetting via RTS pin…"**.
9. Si vous n’aviez pas déjà ouvert le **Serial Monitor**, suivez ces étapes :
   - Cliquez sur **Outils** dans la barre d’outils.
   - Descendez et cliquez sur **Serial Monitor**.
10. Cliquez sur le bouton **Reset** une fois de plus.
11. Le Serial Monitor affichera une adresse IP (exemple : http://192.168.1.100).
12. **Copiez cette adresse**, elle vous sera utile dans les prochaines étapes.

Partie 2 : Préparation à l’analyse en Python
--------------------------------------------
1. Pour que la caméra en direct soit visible sur l’ordinateur, nous devons utiliser un script Python.
2. Première étape : installer Python
   - Allez sur **python.org** et téléchargez Python.
   - Installez Python après le téléchargement.
3. Ouvrez le **Command Prompt** et installez les bibliothèques nécessaires :
   - Tapez : `pip install numpy` et appuyez sur Entrée.
   - Ensuite tapez : `pip install opencv-python` et appuyez sur Entrée.
   - Fermez le Command Prompt après l’installation.

Partie 3 : Détection avec Python
--------------------------------
1. Ouvrez un éditeur de code (par exemple **VS Code**).
2. Ouvrez le fichier **SystDectCouleur** situé dans le dossier **STC**.
3. Dans le fichier, remplacez le champ correspondant avec l’adresse IP obtenue à l’étape 9 de la Partie 1.
4. Cliquez sur **Run** : le programme devrait commencer à capter le signal.
