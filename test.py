import qgrid
import pandas as pd
url = 'https://github.com/chris1610/pbpython/blob/master/data/2018_Sales_Total_v2.xlsx?raw=True'
df = pd.read_excel(url)

widget = qgrid.show_grid(df)
widget