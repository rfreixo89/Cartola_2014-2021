## importa bibliotecas
import json
import pandas as pd
import requests
import time

url_list = 'https://api.cartolafc.globo.com/clubes'
ano_clube ='2021'
path_brutos = 'D:/Freixo/OneDrive/OneDrive/Documentos/FIAP/Teste/Clubes_{}_raw.json'.format(ano_clube)
path_limpos = 'D:/Freixo/OneDrive/OneDrive/Documentos/FIAP/Teste/Clubes_de_{}_clean.csv'.format(ano_clube)

# pega resultado json da API
response = requests.get(url_list)
data = response.json()

## Salva o Json
#with open(path_brutos, 'w') as f:
#    json.dump(data,f)


## Separa em DataFrame
df = pd.DataFrame(data)
# df_clean=df
df_clean = df.drop(['escudos'])

# inverte colunas e rows
df_col = df_clean.transpose()


# add colunas
df_col['dt_Atualizacao'] = time.strftime("%d/%m/%Y")




df_col =df_col.rename(columns={'nome': 'NomeCompleto', 'id': 'Cod_2021',
                             'nome_fantasia': 'NomeCartola',
                             'nome.cartola': 'NomeCartola'
})

print(df_col.head(20))
#df_col.to_csv(str(path_limpos), index=False)




