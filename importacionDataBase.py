
import pandas as pd

archivo_csv = 'Spotify Most Streamed Songs.csv'  

df = pd.read_csv(archivo_csv)

print(df.head())

