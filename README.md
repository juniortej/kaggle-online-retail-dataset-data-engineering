# Kaggle Online Retail Dataset ETL Project

Ce projet illustre une pipeline ETL complète pour le dataset en ligne de Kaggle sur la vente au détail. Il intègre des outils comme Spark pour le traitement des données volumineuses, Prefect pour l'orchestration des workflows, et PostgreSQL pour le stockage des données.

---

## Table des matières

- [Aperçu du projet](#aperçu-du-projet)
- [Structure des dossiers](#structure-des-dossiers)
- [Installation et prérequis](#installation-et-prérequis)
- [Pipeline ETL](#pipeline-etl)
  - [1. Extraction](#1-extraction)
  - [2. Prétraitement](#2-prétraitement)
  - [3. Transformation](#3-transformation)
  - [4. Chargement](#4-chargement)
- [Configuration](#configuration)
- [Comment exécuter](#comment-exécuter)
- [Hooks Pre-commit](#hooks-pre-commit)
- [Améliorations](#améliorations)

---

## Aperçu du projet

Le but de ce projet est de transformer des données brutes de vente au détail en un format structuré et exploitable. Ce processus inclut :
- Télécharger le dataset depuis Kaggle.
- Nettoyer et prétraiter les données avec Apache Spark.
- Transformer les données en tables significatives.
- Charger les données dans une base PostgreSQL pour analyse et interrogation.

---

## Structure des dossiers

```plaintext
.
├── README.md                   # Documentation du projet
├── common_tools/               # Utilitaires communs
│   ├── constants.py            # Variables constantes utilisées dans le projet
│   └── spark.py                # Initialisation de la session Spark
├── config/                     # Fichiers de configuration
│   └── config.py               # Configuration de la base de données et des variables d'environnement
├── data-modeling/              # Modèles SQL
│   └── cible.sql               # Création des tables en SQL
├── etl/                        # Logique ETL
│   ├── preprocessing.py        # Nettoyage et prétraitement des données
│   ├── processing.py           # Transformation des données
│   └── write_to_postgres.py    # Chargement des données dans PostgreSQL
├── ingestion/                  # Extraction des données
│   └── extract.py              # Téléchargement du dataset Kaggle
├── workflow/                   # Scripts d'orchestration
│   └── main.py                 # Point d'entrée principal du workflow
└── .pre-commit-config.yaml     # Hooks Pre-commit pour assurer la qualité du code
```

# Installation et Pré-requis

## Outils et Bibliothèques
- **Python** : 3.8+
- **Apache Spark** : Pour le traitement distribué des données
- **PostgreSQL** : Pour le stockage des données
- **Prefect** : Pour l'orchestration des workflows
- **Kaggle API** : Pour le téléchargement du dataset

---

## Dépendances Python
Installez les bibliothèques nécessaires avec la commande suivante :

```bash
pip install -r requirements.txt
```

## API Kaggle
Ajoutez votre fichier kaggle.json à votre répertoire utilisateur ou à un emplacement approprié, puis authentifiez-vous :

```bash 
chmod 600 path/to/kaggle.json
```

## Base PostgreSQL
Configurez une base PostgreSQL et mettez à jour le fichier .env avec vos identifiants :

```bash 
PGHOST=your_database_host
PGDATABASE=your_database_name
PGUSER=your_database_user
PGPASSWORD=your_database_password
```

## Hooks Pre-commit
Le formatage du code est assuré par black et isort :

### Installation des hooks :
```bash 
pre-commit install
```

# Comment Exécuter
## 1. Télécharger le Dataset
Exécutez le pipeline principal avec :

```bash
python workflow/main.py input_path output_path
```
input_path : Chemin vers le dataset.
output_path : Dossier où les fichiers Parquet seront sauvegardés.

## 2. Vérifier la base de données
Après exécution, vérifiez PostgreSQL pour les tables :
customers
products
transactions

## Améliorations
### Les futures améliorations pourraient inclure :

- Validation des données : Ajouter des étapes de validation avant le chargement dans PostgreSQL.
- Mises à jour incrémentielles : Gérer les mises à jour en flux ou incrémentielles.
- Mise à l'échelle : Optimiser pour des datasets plus volumineux avec un réglage Spark.