# Documentation

Le livrable est partagé en deux parties:
* Une partie Python décrite ci-dessous dans la doc
* Une partie SQL situé dans le répertoire `sql` et aussi décrite à la fin de cette doc.

## Documentation Python

### Code et organization
* Fichier `__init__.py` pour pouvoir faire des imports en cas de réutilisations.
* Le fichier `requirements.txt` contient les dépendances à installer.
* Les fichiers sources sont dans le répertoire `datasources`.
* Le graph json est le répertoire `outputs`.
* Le code proposé est principalement situé dans le répertoire **servier** et dans le module **data_prep.py** avec les fonctions principales contenant une **doc string**:
    * `read_pandas_csv`: Lecture des datasources et generation d'un dataframe pour faciliter le parsing.
    * `pubmed_journal_search`: cherche le médicament dans le dataset **pubmed** et enregistre les publications en journal.
    * `clinical_trial_search`: cherche le médicament dans le dataset **clinical trials**.
    * `clean_results`: Nettoyage du résultat final avant de créer le JSON.
    * `write_json`: Ecrie le graph sous format de JSON.
    * Un bloc main accompagne le code pour un exemple d'éxecution.
* Le traitement ad-hoc est situé dans le module **popular_journal.py** avec les fonctions principales contenant une **doc string**.

### Choix
* Utilisation des dataframes pour faciliter le parsing et la récupération des valeurs(titre, date ...)
* Création de deux fonctions distinces (pubmed/journaux et clinical trials), dans le sens où en serait interessé par uniquement un des deux sans forcément traiter l'autre. Potentiellement on pourrait ajouter un `if statement` et garder une seule fonction mais ca engendrai le fait d'avoir des valeurs `hardcoded` et entacherai la réutilisation.


### Tests
* Des tests unitaires simples accompagnent le code.


### Bonnes pratiques
* Importation sans wildcard.
* Respect PEP8 et convention python de nommage.

### Pour aller plus loins (Question 6)
* Dans le cas ou en aurait plusieurs fichier, il serai pertinent d'utiliser du multiprocessing. On aura ici un pool de process qui sera égale au nombre de fichiers et ainsi on appliquera les différentes fontions de la pipeline pour traiter chaque fichier.
* Dans le cas ou en aurait un grand fichier je passerai plutot par **Spark**, puisqu'il fait la lazy evaluation et ne lira pas la data du premier coup.


## Documentation SQL

Les requêtres SQL développés restent assez simples et comme bonne pratique, utilisation des CTE pour une meilleur organisation du code.