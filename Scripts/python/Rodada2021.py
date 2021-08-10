## importa bibliotecas
import json

import pandas as pd
import requests
import time


def strip_left(df, suffix='scout.'):
    df.columns = df.columns.str.lstrip(suffix)

 ## Set Variaveis
ano='2021'

url_atletas = 'https://api.cartolafc.globo.com/atletas/mercado'


pd.set_option('display.width', 3000)
pd.set_option('display.max_columns',1000)
tempo = time.strftime("%Y%m%d-%H%M%S")

# pega resultado json da API atletas e salva

response = requests.get(url_atletas)
data = response.json()





# Separa os DF do JSON



#Atletas
df_atletas_tmp = data['atletas']
df_status = pd.DataFrame(data['status']).transpose()
df_posicoes = pd.DataFrame(data['posicoes']).transpose()
df_atletas = pd.json_normalize(df_atletas_tmp)
df_status = pd.DataFrame(data['status']).transpose()
df_clubes = pd.DataFrame(data['clubes']).transpose()
rodada=df_atletas['rodada_id']




## Cria nome dos arquivos
path_brutos = '/tmp/stage/rodada_{}_de_{}_raw.csv'.format(rodada[0], ano)
path_limpos = '/tmp/stage/rodada_{}_de_{}_clean.csv'.format(rodada[0], ano)
with open(path_brutos, 'w') as f:
    json.dump(data,f)


## remove a sufix da normalização


strip_left(df_atletas)



## Remove jogadores que não entraram em campo




## Renomeia colunas nos DATAFRAMES
df_posicoes = df_posicoes.rename(columns={'id':'posicao_id','abreviacao':'posicao'})
df_status = df_status.rename(columns={'nome':'status','id':'atus_id'})
df_clubes = df_clubes.rename(columns={'id':'lube_id'})


## Remove colunas
df_clubes=df_clubes.drop(['escudos','nome_fantasia'],axis=1)


## Merge os DF
df_final = pd.merge(df_posicoes,df_atletas, on='posicao_id')
df_final = pd.merge(df_status,df_final, on='atus_id')
df_final = pd.merge(df_final,df_clubes, on='lube_id')

#print(df_final.head())
df_final.to_csv(str(path_limpos),index=False)


## Remove colunas
df_final = df_final.drop(['nome_x','lug','foto','apelido_abreviado','atus_id','posicao_id','abreviacao'],axis=1)
## Renomeia colunas
df_final= df_final.rename(columns={'status'	: 'Status', 'posicao' : 'Posicao', 'atleta_id' : 'AtletaID',
                                    'rodada_id' : 'Rodada', 'lube_id' : 'ClubeID', 'pontos_num'  : 'Pontos',
                                   'preco_num' : 'Preco', 'variacao_num' : 'PrecoVariacao', 'media_num' : 'PontosMedia',
                                   'jogos_num': 'Jogos', 'apelido' : 'Apelido', 'nome_y': 'Nome', 'nome' : 'Clube'})




# add colunas

df_final['dt_Atualizacao'] = time.strftime("%d/%m/%Y")
df_final['ano'] = ano
df_final['PlacarVisitante'] = ''
df_final['PlacarCasa'] = ''
df_final['dia'] = ''
if 'CA' not in df_final:
    df_final['CA'] = None
    df_final['CA'] = pd.to_numeric(df_final['CA'])
if 'DD' not in df_final:
    df_final['DD'] = None
    df_final['DD'] = pd.to_numeric(df_final['DD'])
if 'CV' not in df_final:
    df_final['CV'] = None
    df_final['CV'] = pd.to_numeric(df_final['CV'])
if 'DP' not in df_final:
    df_final['DP'] = None
    df_final['DP'] = pd.to_numeric(df_final['DP'])
if 'FC' not in df_final:
    df_final['FC'] = None
    df_final['FC'] = pd.to_numeric(df_final['FC'])
if 'GC' not in df_final:
    df_final['GC'] = None
    df_final['GC'] = pd.to_numeric(df_final['GC'])
if 'GS' not in df_final:
    df_final['GS'] = None
    df_final['GS'] = pd.to_numeric(df_final['GS'])

if 'RB' not in df_final:
    df_final['RB'] = None
    df_final['RB'] = pd.to_numeric(df_final['RB'])

if 'SG' not in df_final:
    df_final['SG'] = None
    df_final['SG'] = pd.to_numeric(df_final['SG'])

if 'A' not in df_final:
    df_final['A'] = None
    df_final['A'] = pd.to_numeric(df_final['A'])

if 'FD' not in df_final:
    df_final['FD'] = None
    df_final['FD'] = pd.to_numeric(df_final['FD'])

if 'FF' not in df_final:
    df_final['FF'] = None
    df_final['FF'] = pd.to_numeric(df_final['FF'])

if 'FS' not in df_final:
    df_final['FS'] = None
    df_final['FS'] = pd.to_numeric(df_final['FS'])

if 'FT' not in df_final:
    df_final['FT'] = None
    df_final['FT'] = pd.to_numeric(df_final['FT'])

if 'G' not in df_final:
    df_final['G'] = None
    df_final['G'] = pd.to_numeric(df_final['G'])

if 'I' not in df_final:
    df_final['I'] = None
    df_final['I'] = pd.to_numeric(df_final['I'])

if 'PE' not in df_final:
    df_final['PE'] = None
    df_final['PE'] = pd.to_numeric(df_final['PE'])

if 'DE' not in df_final:
    df_final['DE'] = None
    df_final['DE'] = pd.to_numeric(df_final['DE'])

if 'PI' not in df_final:
    df_final['PI'] = None
    df_final['PI'] = pd.to_numeric(df_final['PI'])

if 'DS' not in df_final:
    df_final['DS'] = None
    df_final['DS'] = pd.to_numeric(df_final['DS'])

if 'PP' not in df_final:
    df_final['PP'] = None
    df_final['PP'] = pd.to_numeric(df_final['PP'])

if 'PC' not in df_final:
    df_final['PC'] = None
    df_final['PC'] = pd.to_numeric(df_final['PC'])



##print(df_final)
## Reorg schema
df_final = df_final[
       ['AtletaID', 'Apelido', 'Nome', 'Clube', 'Posicao', 'Preco', 'Rodada', 'Jogos', 'Status',
       'Pontos',
       'PontosMedia', 'PrecoVariacao', 'PlacarVisitante', 'PlacarCasa', 'A', 'CA', 'CV', 'DD', 'DP', 'FC',
         'FD', 'FF', 'FS', 'FT', 'G', 'GC', 'GS', 'I', 'PI', 'PP', 'DS', 'SG','DE','PC', 'ano', 'dia','dt_Atualizacao']
     ]

## Preenchendo com 0 valores nulos Função testa se o tipo da colluna é numerica e se for preenche com zero se não for informa sem valor

df_final = df_final.apply(lambda x: x.fillna(0) if x.dtype.kind in 'biufc' else x.fillna('Sem valor'))

df_final.to_csv(str(path_limpos),index=False)







