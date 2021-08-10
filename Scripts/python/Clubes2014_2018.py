import csv
import requests
import pandas as pd
import time




url = 'https://raw.githubusercontent.com/henriquepgomide/caRtola/master/data/times_ids.csv'
path_brutos = '/tmp/stage/clubes_ids_raw.csv'
path_limpos = '/tmp/stage/clubes_ids_clean.csv'


# Lê os dados CSV brutos e salva em uma pasta temporaria antes do ETL

df = pd.read_csv(url)
#df.to_csv(path_brutos, index=False)

df_clean =df.rename(columns={'nome.completo': 'NomeCompleto', 'cod.older': 'Cod_2014_2016',
                             'cod.2017': 'Cod_2017', 'cod.2018': 'cod_2018', 'nome.cbf': 'NomeCBF',
                             'nome.cartola': 'NomeCartola'
})

df_clean = df_clean.drop(columns={'escudos.60x60', 'escudos.30x30', 'escudos.45x45'}, axis=1)


df_clean.to_csv(path_limpos, index=False)
#print(df_clean)


