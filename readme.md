"""LesGaragistesDuSud

- auth
  - Role admin
  - Role Client(conducteur)
- voitures
  - disponnible
- location (user)
  - rendre un vehicule
    - payement apres le
      rendu
    - mise a jour de la
      disponibilité
      et kilometrage
  - cherche un vehicule
    - filtrer par marque
- administration (admin only)
  - CRUD des vehicules
    - afficher le vehicule
    - si location afficher
      le conducteur
      la location
      (date, durée...)
- deconnection

vehicule:
id
brand
model
kilometrage
dailyPrice
User
id
username
civilité
firstName
lastName
birthDate
password (hash)
role : Admin//Driver

"""

## SuperUser

- username: admin
- password: admin
- email: admin@LesGaragistesDuSud.fr

## Fixtures

`py manage.py loaddata backend/fixtures/data`
