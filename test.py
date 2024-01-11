import pandas as pd


df = pd.DataFrame({
    'A': ['John', 'Boby', 'Mina'],
    'B': ['Masters', 'Graduate', 'Graduate'],
    'C': [27, 23, 21]
})

df.pivot('A', 'B', 'C')