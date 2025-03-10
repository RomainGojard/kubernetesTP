# Utiliser l'image officielle Python comme image parente
FROM python:3.8

# Définir le répertoire de travail dans le conteneur
WORKDIR /todoappGB

# Copier les fichiers du projet dans le conteneur
COPY . /todoappGB 

# Installer les dépendances
RUN pip install -r requirements.txt

# Exposer le port sur lequel l'application s'exécute
EXPOSE 8000

# Commande pour démarrer l'application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]