# Udacity-BookStore
  - Udacity-BookStore est une bibliotheque virtuelle pour les etudiants udacity leur permettant de consulter la lister des livres disponible, poster un livre, 
  rechercher un livre, mettre a jour les informations concernant un livre et de le supprimer
## pour commencer
### Pre-requis Developement local
Les développeurs utilisant ce projet doivent déjà avoir Python3, pip et node installés sur leurs machines locales
#### Backend
Depuis le dossier backend executer `pip3 intall -r requirements.txt`. tous les packages requis sont inclus dans le fichier requirements.txt
pour lancer cette application executer les commandes suivant:
  - pour les utilisateurs windows
  set FLASK_APP=flaskr
  set FLASK_ENV=development
  flask run
  - pour les utilisateur linux
  export FLASK_APP=flaskr
  export FLASK_ENV=development
  flask run
Ces commandes mettent l'application en développement et ordonnent à notre application d'utiliser le fichier '__init__.py' dans notre dossier flaskr. Travailler en mode développement affiche un débogueur interactif dans la console et redémarre le serveur chaque fois que des modifications sont apportées. L'application est exécutée sur 'http://127.0.0.1:5000/' par défaut et est un proxy dans la configuration frontend.

#### Frontend
Depuis le dossier frontend, executer les commandes suivantes pour lancer le client frontend:
```
npm install // only once to install dependencies
npm start 
```

par defaut, le frontend se lancera sur localhost:3000. 
### Tests
Pour exécuter des tests, accédez au dossier principal et exécutez les commandes suivantes :
```
dropdb bookshelf_test
createdb bookshelf_test
psql bookshelf_test < books.psql
python test_flaskr.py
```
La première fois que vous exécutez les tests, omettez la commande dropdb.

Tous les tests sont conservés dans ce fichier et doivent être maintenus au fur et à mesure que des mises à jour sont apportées aux fonctionnalités de l'application.

## pour commencer

### Error Handling
Les erreurs sont renvoyées sous forme d'objets JSON au format suivant :
```
{
    "success": False, 
    "error": 400,
    "message": "bad request"
}
```
L'API renvoie trois types d'erreur lorsque les demandes échouent:
- 400: Bad Request / requete errone
- 404: Resource Not Found / ressource non trouver
- 422: Not Processable / intraitable

### Endpoints / points de terminaison
#### GET /books
- Généralités: 
- Renvoie une liste d'objets de livre, la valeur de réussite et le nombre total de livres 
- Les résultats sont paginés par groupes de 8. Incluez un argument de demande pour choisir le numéro de page, à partir de 1. 
- Exemple : 'curl http://127.0.0.1:5000/books'

``` {
  "books": [
    {
      "author": "Stephen King",
      "id": 1,
      "rating": 5,
      "title": "The Outsider: A Novel"
    },
    {
      "author": "Lisa Halliday",
      "id": 2,
      "rating": 5,
      "title": "Asymmetry: A Novel"
    },
    {
      "author": "Kristin Hannah",
      "id": 3,
      "rating": 5,
      "title": "The Great Alone"
    },
    {
      "author": "Tara Westover",
      "id": 4,
      "rating": 5,
      "title": "Educated: A Memoir"
    },
    {
      "author": "Jojo Moyes",
      "id": 5,
      "rating": 5,
      "title": "Still Me: A Novel"
    },
    {
      "author": "Leila Slimani",
      "id": 6,
      "rating": 5,
      "title": "Lullaby"
    },
    {
      "author": "Amitava Kumar",
      "id": 7,
      "rating": 5,
      "title": "Immigrant, Montana"
    },
    {
      "author": "Madeline Miller",
      "id": 8,
      "rating": 5,
      "title": "CIRCE"
    }
  ],
"success": true,
"total_books": 18
}
```

#### POST /books
- Generalites:
    - Crée un nouveau livre en utilisant le titre, l'auteur et la note soumis. Renvoie l'ID du livre créé, la valeur de réussite, le nombre total de livres et la liste de livres en fonction du numéro de page actuel pour mettre à jour le frontend.
- `curl http://127.0.0.1:5000/books -X POST -H "Content-Type: application/json" -d '{"title":"Neverwhere", "author":"Neil Gaiman", "rating":"5"}'`
```
{
  "books": [
    {
      "author": "Neil Gaiman",
      "id": 24,
      "rating": 5,
      "title": "Neverwhere"
    }
  ],
  "created": 24,
  "success": true,
  "total_books": 19
}
```
#### DELETE /books/{book_id}
- Generalites:
    - Supprime le livre de l'ID donné s'il existe. Renvoie l'ID du livre supprimé, la valeur de réussite, le nombre total de livres et la liste des livres en fonction du numéro de page actuel pour mettre à jour le frontend. 
- `curl -X DELETE http://127.0.0.1:5000/books/16?page=2`
```
{
  "books": [
    {
      "author": "Gina Apostol",
      "id": 9,
      "rating": 5,
      "title": "Insurrecto: A Novel"
    },
    {
      "author": "Tayari Jones",
      "id": 10,
      "rating": 5,
      "title": "An American Marriage"
    },
    {
      "author": "Jordan B. Peterson",
      "id": 11,
      "rating": 5,
      "title": "12 Rules for Life: An Antidote to Chaos"
    },
    {
      "author": "Kiese Laymon",
      "id": 12,
      "rating": 1,
      "title": "Heavy: An American Memoir"
    },
    {
      "author": "Emily Giffin",
      "id": 13,
      "rating": 4,
      "title": "All We Ever Wanted"
    },
    {
      "author": "Jose Andres",
      "id": 14,
      "rating": 4,
      "title": "We Fed an Island"
    },
    {
      "author": "Rachel Kushner",
      "id": 15,
      "rating": 1,
      "title": "The Mars Room"
    }
  ],
  "deleted": 16,
  "success": true,
  "total_books": 15
}
```
#### PATCH /books/{book_id}
- General:
    - Le cas échéant, met à jour la note du livre spécifié. Renvoie la valeur de réussite et l'ID du livre modifié. 
- `curl http://127.0.0.1:5000/books/15 -X PATCH -H "Content-Type: application/json" -d '{"rating":"1"}'`
```
{
  "id": 15,
  "success": true
}
```
#### POST /books/search
-Generalites:
   - afficher la liste des livres dont le titre correspond(non sensible a la casse) au mot envoyer via la methode post du user
- `curl  http://127.0.0.1:5000//books/search -X POST -H "Content-Type: application/json" -d '{"title":"rachel kushner"}'`
```
{
  "books": [{
     "author": "Rachel Kushner",
      "id": 15,
      "rating": 1,
      "title": "The Mars Room"
  }],
  "success": true,
  "count": 1
}
```