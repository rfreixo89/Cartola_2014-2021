## importa bibliotecas

import pandas as pd
import requests
import time


pd.set_option('display.width', 300)
pd.set_option('display.max_columns',1000)
##set variaveis
ano='2019'
rodada = 1
url_list = pd.DataFrame
url_list = [
  'https://raw.githubusercontent.com/henriquepgomide/caRtola/master/data/{}/rodada-1.csv'.format(ano)
, 'https://raw.githubusercontent.com/henriquepgomide/caRtola/master/data/{}/rodada-2.csv'.format(ano)
, 'https://raw.githubusercontent.com/henriquepgomide/caRtola/master/data/{}/rodada-3.csv'.format(ano)
, 'https://raw.githubusercontent.com/henriquepgomide/caRtola/master/data/{}/rodada-4.csv'.format(ano)
, 'https://raw.githubusercontent.com/henriquepgomide/caRtola/master/data/{}/rodada-5.csv'.format(ano)
, 'https://raw.githubusercontent.com/henriquepgomide/caRtola/master/data/{}/rodada-6.csv'.format(ano)
, 'https://raw.githubusercontent.com/henriquepgomide/caRtola/master/data/{}/rodada-7.csv'.format(ano)
, 'https://raw.githubusercontent.com/henriquepgomide/caRtola/master/data/{}/rodada-8.csv'.format(ano)
, 'https://raw.githubusercontent.com/henriquepgomide/caRtola/master/data/{}/rodada-9.csv'.format(ano)
, 'https://raw.githubusercontent.com/henriquepgomide/caRtola/master/data/{}/rodada-10.csv'.format(ano)
, 'https://raw.githubusercontent.com/henriquepgomide/caRtola/master/data/{}/rodada-11.csv'.format(ano)
, 'https://raw.githubusercontent.com/henriquepgomide/caRtola/master/data/{}/rodada-12.csv'.format(ano)
, 'https://raw.githubusercontent.com/henriquepgomide/caRtola/master/data/{}/rodada-13.csv'.format(ano)
, 'https://raw.githubusercontent.com/henriquepgomide/caRtola/master/data/{}/rodada-14.csv'.format(ano)
, 'https://raw.githubusercontent.com/henriquepgomide/caRtola/master/data/{}/rodada-15.csv'.format(ano)
, 'https://raw.githubusercontent.com/henriquepgomide/caRtola/master/data/{}/rodada-16.csv'.format(ano)
, 'https://raw.githubusercontent.com/henriquepgomide/caRtola/master/data/{}/rodada-17.csv'.format(ano)
, 'https://raw.githubusercontent.com/henriquepgomide/caRtola/master/data/{}/rodada-18.csv'.format(ano)
, 'https://raw.githubusercontent.com/henriquepgomide/caRtola/master/data/{}/rodada-19.csv'.format(ano)
, 'https://raw.githubusercontent.com/henriquepgomide/caRtola/master/data/{}/rodada-20.csv'.format(ano)
, 'https://raw.githubusercontent.com/henriquepgomide/caRtola/master/data/{}/rodada-21.csv'.format(ano)
, 'https://raw.githubusercontent.com/henriquepgomide/caRtola/master/data/{}/rodada-22.csv'.format(ano)
, 'https://raw.githubusercontent.com/henriquepgomide/caRtola/master/data/{}/rodada-23.csv'.format(ano)
, 'https://raw.githubusercontent.com/henriquepgomide/caRtola/master/data/{}/rodada-24.csv'.format(ano)
, 'https://raw.githubusercontent.com/henriquepgomide/caRtola/master/data/{}/rodada-25.csv'.format(ano)
, 'https://raw.githubusercontent.com/henriquepgomide/caRtola/master/data/{}/rodada-26.csv'.format(ano)
, 'https://raw.githubusercontent.com/henriquepgomide/caRtola/master/data/{}/rodada-27.csv'.format(ano)
, 'https://raw.githubusercontent.com/henriquepgomide/caRtola/master/data/{}/rodada-28.csv'.format(ano)
, 'https://raw.githubusercontent.com/henriquepgomide/caRtola/master/data/{}/rodada-29.csv'.format(ano)
, 'https://raw.githubusercontent.com/henriquepgomide/caRtola/master/data/{}/rodada-30.csv'.format(ano)
, 'https://raw.githubusercontent.com/henriquepgomide/caRtola/master/data/{}/rodada-31.csv'.format(ano)
, 'https://raw.githubusercontent.com/henriquepgomide/caRtola/master/data/{}/rodada-32.csv'.format(ano)
, 'https://raw.githubusercontent.com/henriquepgomide/caRtola/master/data/{}/rodada-33.csv'.format(ano)
, 'https://raw.githubusercontent.com/henriquepgomide/caRtola/master/data/{}/rodada-34.csv'.format(ano)
, 'https://raw.githubusercontent.com/henriquepgomide/caRtola/master/data/{}/rodada-35.csv'.format(ano)
, 'https://raw.githubusercontent.com/henriquepgomide/caRtola/master/data/{}/rodada-36.csv'.format(ano)
, 'https://raw.githubusercontent.com/henriquepgomide/caRtola/master/data/{}/rodada-37.csv'.format(ano)
, 'https://raw.githubusercontent.com/henriquepgomide/caRtola/master/data/{}/rodada-38.csv'.format(ano)
    ]


for url in url_list:
    ## Set Variaveis

    path_brutos = '/tmp/stage/rodada_{}_de_{}_raw.csv'.format(rodada,ano)
    path_limpos = '/tmp/stage/rodada_{}_de_{}_clean.csv'.format(rodada,ano)
    rodada = rodada + 1

    # pega resultado Brutos e salva CSV da lista
    df = pd.read_csv(url)
    df.to_csv(path_brutos, index=False)

    # Inicio da limpeza de dados

    df_Clean = df.drop(columns=['atletas.foto','atletas.slug'], axis=1)
    ## ADD Columns
    df_Clean['ano']=ano
    df_Clean['PlacarVisitante']=''
    df_Clean['PlacarCasa']=''
    df_Clean['dia']=''
    df_Clean['Jogos']=None
    df_Clean['dt_Atualizacao'] = time.strftime("%d/%m/%Y")
    ## ADD COlumns para padronizar em rodadas que não tiveram penaltis
    if 'PP' not in df_Clean:
        df_Clean['PP'] = None
        df_Clean['PP'] = pd.to_numeric(df_Clean['PP'])
    if 'DP' not in df_Clean:
        df_Clean['DP'] = None
        df_Clean['DP'] = pd.to_numeric(df_Clean['DP'])
    if 'DE' not in df_Clean:
        df_Clean['DE'] = None
        df_Clean['DE'] = pd.to_numeric(df_Clean['DE'])
    if 'PC' not in df_Clean:
        df_Clean['PC'] = None
        df_Clean['PC'] = pd.to_numeric(df_Clean['PC'])



    ## Rename columns
    df_Clean=df_Clean.rename(columns={'atletas.nome' : 'Nome',
                                        'atletas.apelido' : 'Apelido',
                                        'atletas.atleta_id' : 'AtletaID',
                                        'atletas.rodada_id' : 'Rodada',
                                        'atletas.clube_id'	: ' ClubeID',
                                        'atletas.posicao_id' : 'Posicao',
                                        'atletas.status_id' : 'Status',
                                        'atletas.pontos_num' : 'Pontos' ,
                                        'atletas.preco_num'	 : 'Preco' ,
                                        'atletas.variacao_num' : 'PrecoVariacao',
                                        'atletas.media_num'	 : 'PontosMedia',
                                        'atletas.clube.id.full.name' : 'Clube',
                                        'RB' : 'DS', ## Padronização nova nomeclatura cartorla
                                        'PE' : 'PI' ## Padronização nova nomeclatura cartorla
                                      })
    ## Reord schema
    df_Clean = df_Clean[
        ['AtletaID', 'Apelido', 'Nome', 'Clube', 'Posicao', 'Preco', 'Rodada', 'Jogos', 'Status',
         'Pontos',
         'PontosMedia', 'PrecoVariacao', 'PlacarVisitante', 'PlacarCasa', 'A', 'CA', 'CV', 'DD', 'DP', 'FC',
         'FD', 'FF', 'FS', 'FT', 'G', 'GC', 'GS', 'I', 'PI', 'PP', 'DS', 'SG', 'DE', 'PC', 'ano', 'dia',
         'dt_Atualizacao']
    ]
    ## Preenchendo com 0 valores nulos Função testa se o tipo da colluna é numerica e se for preenche com zero se não for informa sem valor

    df_Clean = df_Clean.apply(lambda x: x.fillna(0) if x.dtype.kind in 'biufc' else x.fillna('NaN'))

    ## salva arquivo pronto
    df_Clean.to_csv(path_limpos, index=False)
#print(df_Clean.head())





