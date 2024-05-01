# -*- coding: utf-8 -*-
"""champions league data with ELO.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1URgxN1JStUAChlqEk1VJaslmCYsnyoPF
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Carico il dataset per vedere le prime righe e riassumere la sua struttura
file_path = 'Champions League data with ELO.csv'
data = pd.read_csv(file_path)

# Visualizzo le prime righe e le informazioni generali sul dataset
data_head = data.head()
data_info = data.info()
data_description = data.describe()

(data_head, data_info, data_description)

#Tento di leggere il CSV con una codifica diversa: ISO-8859-1
try:
    data_iso = pd.read_csv(file_path, encoding='ISO-8859-1')
except Exception as e_iso:
    error_iso = str(e_iso)

# Tento di leggere il CSV con un'altra codifica: Windows-1252
try:
    data_windows = pd.read_csv(file_path, encoding='Windows-1252')
except Exception as e_windows:
    error_windows = str(e_windows)

# Verifico quali, eventualmente, sono andati a buon fine e riassumo i dati
if 'data_iso' in locals():
    data_head_iso = data_iso.head()
    data_info_iso = data_iso.info()
    data_description_iso = data_iso.describe()
    successful_encoding = 'ISO-8859-1'
elif 'data_windows' in locals():
    data_head_windows = data_windows.head()
    data_info_windows = data_windows.info()
    data_description_windows = data_windows.describe()
    successful_encoding = 'Windows-1252'
else:
    data_head_iso, data_head_windows, error_iso, error_windows, successful_encoding = None, None, error_iso, error_windows, None

(data_head_iso, data_info_iso, data_description_iso, data_head_windows, data_info_windows, data_description_windows, error_iso, error_windows, successful_encoding)

data_iso.head()

# Traccio la relazione tra Finish (posizione finale nella competizione) e ranking ELO con gli assi invertiti.
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Finish', y='ELO', data=data_iso, alpha=0.6)

plt.title('Correlazione tra Finish e ELO Ranking')
plt.xlabel('Finish (Posizione Finale)')
plt.ylabel('ELO Ranking')

plt.grid(True)
plt.show()

"""Questo grafico consente di vedere come squadre con un ranking ELO più alto tendono generalmente a classificarsi meglio nelle competizioni.

"""

# Aggiungo una retta di regressione al grafico a dispersione di Finish vs ELO
plt.figure(figsize=(10, 6))
sns.regplot(x='Finish', y='ELO', data=data_iso, scatter_kws={'alpha':0.6})

plt.title('Correlazione tra Finish e ELO Ranking con Retta di Regressione')
plt.xlabel('Finish (Posizione Finale)')
plt.ylabel('ELO Ranking')

plt.grid(True)
plt.show()

"""Questa retta aiuta a visualizzare meglio la tendenza generale che mostra come un ranking ELO più alto sia associato a posizioni migliori nella competizione. La pendenza negativa della retta di regressione conferma ulteriormente la correlazione inversa tra le due variabili"""

# Traccio il risultato finale rispetto all'Heritage_Score con una retta di regressione e calcolo dell'R-quadro.
plt.figure(figsize=(10, 6))
reg_plot = sns.regplot(x='Finish', y='Heritgae_Score', data=data_iso, scatter_kws={'alpha':0.6}, line_kws={'color': 'red'})


from sklearn.metrics import r2_score

# Ottengo i dati della retta di regressione
reg_line_x = reg_plot.get_lines()[0].get_xdata()
reg_line_y = reg_plot.get_lines()[0].get_ydata()

# Calcolo l'R-quadro
r_squared = r2_score(data_iso['Heritgae_Score'], np.interp(data_iso['Finish'], reg_line_x, reg_line_y))

plt.title('Correlazione tra Finish e Heritage Score con Retta di Regressione')
plt.xlabel('Finish (Posizione Finale)')
plt.ylabel('Heritage Score')
plt.grid(True)
plt.show()

print("L'R quadro vale:", r_squared)

