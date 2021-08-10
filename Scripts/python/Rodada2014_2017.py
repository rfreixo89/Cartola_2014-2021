import csv
import requests
import pandas as pd
import time



### Variaveis
url = 'https://raw.githubusercontent.com/henriquepgomide/caRtola/master/data/dados_agregados_limpos.csv'
path_brutos = '/tmp/stage/rodada_2014_2017_raw.csv'
path_limpos = '/tmp/stage/rodada_2014_2017_clean.csv'


### Lê os dados CSV brutos e salva em uma pasta temporaria antes do ETL

df = pd.read_csv(url)
df.to_csv(path_brutos, index=False)

## Inicio do tratamento de dados
##Criando esquema


## removendo colunas avg.
col_avg = [c for c in df.columns if c.lower()[:4] != 'avg.']
df_clean= df[col_avg]

## removendo colunas especificas
df_clean=df_clean.drop(columns=['pred.away.score','pred.home.score',
                                'risk_points','variable','home.attack','home.defend', 'Participou'])

## renomeando colunas
df_clean=df_clean.rename(columns={'away.score.x':'PlacarVisitante',
                                  'home.score.x' : 'PlacarCasa',
                                  'ClubeID' : 'Clube',
                                  'RB' : 'DS', ## Padronização nova nomeclatura cartorla
                                  'PE' : 'PI' ## Padronização nova nomeclatura cartorla
                                   })

## ADD column
df_clean['Nome'] = None
if 'DE' not in df_clean:
    df_clean['DE'] = None
    df_clean['DE'] = pd.to_numeric(df_clean['DE'])
if 'PC' not in df_clean:
    df_clean['PC'] = None
    df_clean['PC'] = pd.to_numeric(df_clean['PC'])
df_clean['dt_Atualizacao'] = time.strftime("%d/%m/%Y")



## Definindo ordem dos esquemas
df_clean=df_clean[
    ['AtletaID', 'Apelido', 'Nome', 'Clube', 'Posicao', 'Preco', 'Rodada', 'Jogos', 'Status',
     'Pontos',
     'PontosMedia', 'PrecoVariacao', 'PlacarVisitante', 'PlacarCasa', 'A', 'CA', 'CV', 'DD', 'DP', 'FC',
     'FD', 'FF', 'FS', 'FT', 'G', 'GC', 'GS', 'I', 'PI', 'PP', 'DS', 'SG', 'DE', 'PC', 'ano', 'dia',
     'dt_Atualizacao']
]



## Preenchendo com 0 valores nulos Função testa se o tipo da colluna é numerica e se for preenche com zero se não for informa sem valor

df_clean = df_clean.apply(lambda x: x.fillna(0) if x.dtype.kind in 'biufc' else x.fillna('NaN'))


## Salva arquivo DADOs limpos
df_clean.to_csv(path_limpos, index=False)
