# Documentation

Le livrable est partagé en deux parties:
* Une partie Python décrite ci-dessous dans la doc
* Une partie SQL situé dans le répertoire `sql_test` et aussi décrite plus bas dans cette doc.

## Documentation Python

## Code et organization
* Fichier `__init__.py` pour pouvoir importer des fonctions en cas de réutilisations (import).
* Le fichier `requirements.txt` contient les dépendances à installer.
* Les fichiers sources sont dans le répertoire `datasources`.
* Le code proposé est principalement situé dans le module **data_prep** avec les fonctions principales contenant une **doc string**:
    * `read_pandas_csv`: Lecture des datasources et generation d'un dataframe.
    * `drug_search`: cherche le médicament dans les datasets **pubmed** et **clinical_trials** 
    * `write_json`: Ecrie le graph sous format de json

## Choix
* Utilisation des dataframes pour faciliter le parsing et la récupération des valeurs(titre, date ...)


## Tests
* Des tests unitaires accompagnent le code.


## Bonnes pratiques
* Importation sans wildcard.
* Respect PEP8 et convention python de nommage.

## Pour aller plus loins (Question 6)
* Si on est face à une grande volumétrie, première chose il ne faudra pas itérer sur l'ensemble du DataFrame. 


## Documentation SQL

Les requêtres SQL développés restent assez simples et comme bonne pratique, utilisation des CTE pour une meilleur organisation du code.