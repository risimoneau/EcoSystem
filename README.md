# EcoSystem
- Description du projet

    Ce projet est basé sur un model de régression logistique de prédiction binaire sur les risques de développer oui ou non une maladie du coeur.
    Il est basé sur les données founis sur le site de Kaggle : https://www.kaggle.com/code/georgyzubkov/heart-disease-exploratory-data-analysis
    Dans un but ultime, nous pourrions ajouter une validation dans le temps des préditions versu la réalité et les soumettre à nouveau au modèle pour qu'il apprenne par "renforcement" ou tout simplement comme nouvelle données d'entrainement.


- Explication de l'architechture

    La base de données d'entrainement étiquetée comporte cette liste de colonnes/données/valeurs:
    - HeartDisease : l'étiquette si oui ou non le patient à développé une maladie du coeur
    - BMI : l'indice de masse corporelle
    - PhysicalHealth : nombres de jours dans le mois ou le patient c'est senti en mauvaise forme
    - MentalHealth : nombres de jours dans le mois où le patient c'est senti mal mentalement
    - SleepTime : nombre d'heures moyenne de someils
    - Smoking : valeur binaire Vrai pour fumeur ou Faux pour non fumeur
    - AlcoholDrinking : valeur binaire Vrai pour buveur d'alcool ou Faux pour non buveur d'alcool
    - Stroke : valeur binaire à savoir si le patient à déjà eu un accident vasculaire cérébral.
    - DiffWalking : valeur binaire si le patient à de la difficulter à marcher ou monter les escaliers
    - Diabetic : à quatres valeur possible
        - Oui le patient à le diabète
        - Non le patient n'a pas le diabète
        - Non, mais est à la limite
        - Oui pendant une grosesse
    - PhysicalActivity : Activitées physique pendant les 30 derniers jours en dehors du travail
    - Asthma : valeur binaire si le patient souffre d'asthme
    - KidneyDisease : valeur binaire si le patient à un problème de reins
    - SkinCancer : valeur binaire si le patient à ou à déjà eu le cancer de la peau
    - Sex : valeur binaire à savoir le sex du patient 
    - AgeCategory : la catégorie d'âge classé par ces catégories:
        - 18-24
        - 25-29
        - 30-34
        - 35-39
        - 40-44
        - 45-49
        - 50-54
        - 55-59
        - 60-64
        - 65-69
        - 70-74
        - 75-79
        - 80 or older
    - GenHealth : niveau de santé générale classé par ces catégories:
        - Excellent
        - Very good
        - Good
        - Fair
        - Poor
    - Race : la race du patient classé dans ces catégories:
        - White
        - American Indian/Alaskan Native
        - Asian
        - Black
        - Hispanic
        - Other

    Les données soumisent par l'utilisateur devront avoir la même structure sauf bien sur la donnée à prédire "l'étiquette" qui est la valeur "HeartDisease"
    Les données de sortie ont une colonne ajouter appelé "Predict_Heart_Disease" qui prédis si oui ou non le patient va développer une maladie du coeur.


- Étape à suivre pour exécuter
    
    Le projet contient déjà un model pré-entrainé, donc nous pouvons simplement lui soumettre des données structurées comme décris plus haut et
    le résultat sera un nouveau fichiers étiqueté "HD_Result.csv" avec les prédictions appelé "Predict_Heart_Desease".
    Le fichier Dockerfile contient déjà la commande pour faire rouler ce processus.
    Il commence par demander le nom du fichier csv structuré, le valide et créer le fichier de prédictions.
    Si nous voulons ré-entrainer le model, nous pouvons exécuter le programe "train_model.py". Il demandera le fichier d'entrainement et créera les fichiers de test et d'entraiement et le nouveau fichier du model mise à jour "model.h5".


- Schéma du pipeline
    voir le fichier Schema pipeline.pptx
