import pandas as pd
import matplotlib.pyplot as plt
# Cargar el archivo CSV
df = pd.read_csv('Spotify Most Streamed Songs.csv')
df.columns
plt.show()
print(df.columns.tolist())