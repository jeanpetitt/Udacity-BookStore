## Udacity-BookStore

### pour commencer
- URL de base : à l'heure actuelle, cette application ne peut être exécutée que localement et n'est pas hébergée en tant qu'URL de base. L'application backend est hébergée par défaut, 'http://127.0.0.1:5000/', qui est définie comme proxy dans la configuration frontale. - Authentification : Cette version de l'application ne nécessite pas d'authentification ou de clés API.. 

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