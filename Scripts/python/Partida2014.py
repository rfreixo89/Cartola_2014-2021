import csv
import requests
import pandas as pd
import time



pd.set_option('display.width', 300)
pd.set_option('display.max_columns',1000)
### Variaveis
ano=2014
url = 'https://raw.githubusercontent.com/henriquepgomide/caRtola/master/data/{}/{}_partidas.csv'.format(ano,ano)
path_brutos = '/tmp/stage/partidas_{}_raw.csv'.format(ano)
path_limpos = '/tmp/stage/partidas_{}_clean.csv'.format(ano)


df = pd.read_csv(url)
df.to_csv(path_brutos, index=False)

df_clean=df

## Separa o Score criando colunas para ele
df_clean['PlacarCasa']=df_clean['score'].str.split('x').str[0]
df_clean['PlacarCasa']=pd.to_numeric(df_clean['PlacarCasa'])
df_clean['PlacarVisitante']=df_clean['score'].str.split('x').str[-1]
df_clean['PlacarVisitante']=pd.to_numeric(df_clean['PlacarVisitante'])

# Cria Coluna resultado
df_clean['Resultado']=None
df_clean['dt_Atualizacao']=time.strftime("%d/%m/%Y")
df_clean['valida']=None
df_clean['ano']=ano
# Renomeia as colunas para seguir um padrão
df_clean=df_clean.rename(columns={'game' : 'Jogo', 'round' : 'Rodada', 'date' : 'PartidaData',
                                  'home_team' : 'TimeCasa', 'away_team' : 'TimeVisitante', 'arena' : 'Arena' })

# Reorg e drop coluna score

df_clean = df_clean[['Jogo','Rodada' ,'PartidaData', 'TimeCasa', 'PlacarCasa' , 'PlacarVisitante' ,
                     'TimeVisitante', 'Arena', 'Resultado','valida', 'dt_Atualizacao','ano'] ]
# Salva arquivos limpos

df_clean.to_csv(path_limpos, index=False)