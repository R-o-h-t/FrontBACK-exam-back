superuser:

    **login** : admin

    **password** : admin

    **email** : admin@meubleDu31.fr

De lister tous les meubles :

    **GET** api/furnitures

D'ajouter un meuble

    **POST** api/furnitures

De Supprimer un meuble

    **DELETE** api/furnitures/:id

De changer le statut du meuble

    **POST** api/furnitures/status/:id

    status : 'AVAILABLE' | 'SOLD'

    si SOLD => CA du magasin =
