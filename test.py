import pandas as pd
from sklearn import datasets

# Charger le jeu de données Iris
iris = datasets.load_iris()

# Créer un DataFrame à partir du jeu de données Iris
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Ajouter les cibles (espèces d'iris) au DataFrame
df['target'] = iris.target

# Mapper les cibles aux noms des espèces d'iris
target_names = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}
df['target_names'] = df['target'].map(target_names)

# Afficher les premières lignes du DataFrame
print(df.head())