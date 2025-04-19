 Cette application est une ToDo List développée en Python avec le framework Flask, respectant l'architecture Modèle-Vue-Contrôleur (MVC).

Elle permet aux utilisateurs de :

  ✅ Ajouter des tâches avec un titre et une description.

  🔁 Marquer une tâche comme complétée ou non complétée via une case à cocher.

  ✏️ Modifier le titre et la description d’une tâche existante.

  ❌ Supprimer une tâche.

  ⏱️ Voir les tâches dans l’ordre chronologique, avec les plus récentes en haut.

🛠️ Technologies utilisées
  Python 
  Flask
  SQLite (base de données locale)
  HTML5 / CSS3
  
📂 Structure du projet
├── controller.py         # Contrôleur : routes et logique
├── model.py                       # Modèle : interactions avec SQLite
├── templates/
│   ├── index.html                 # Vue principale : affichage des tâches
├── static/
│   └── style.css                  # Fichier CSS pour le design
├── database/
│   └── list.db                    # Base de données SQLite

📌 Objectifs pédagogiques
Ce projet a été réalisé dans un cadre universitaire pour :

  Apprendre la structuration d’une application avec Flask.
  Comprendre et appliquer l’architecture MVC.
  Gérer des données dynamiques avec une base SQLite.
  Manipuler les formulaires web et les interactions utilisateur.

