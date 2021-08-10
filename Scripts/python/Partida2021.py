## importa bibliotecas
import json
import numpy as np

import pandas as pd
import requests
import time



pd.set_option('display.width', 300)
pd.set_option('display.max_columns',1000)
ano='2021'
rodada = 1
url_list = pd.DataFrame
url_list = ['https://api.cartolafc.globo.com/partidas/1'
    , 'https://api.cartolafc.globo.com/partidas/2'
    , 'https://api.cartolafc.globo.com/partidas/3'
    , 'https://api.cartolafc.globo.com/partidas/4'
    , 'https://api.cartolafc.globo.com/partidas/5'
    , 'https://api.cartolafc.globo.com/partidas/6'
    , 'https://api.cartolafc.globo.com/partidas/7'
    , 'https://api.cartolafc.globo.com/partidas/8'
    , 'https://api.cartolafc.globo.com/partidas/9'
    , 'https://api.cartolafc.globo.com/partidas/10'
    , 'https://api.cartolafc.globo.com/partidas/11'
    , 'https://api.cartolafc.globo.com/partidas/12'
    , 'https://api.cartolafc.globo.com/partidas/13'
    , 'https://api.cartolafc.globo.com/partidas/14'
    , 'https://api.cartolafc.globo.com/partidas/15'
    , 'https://api.cartolafc.globo.com/partidas/16'
    , 'https://api.cartolafc.globo.com/partidas/17'
    , 'https://api.cartolafc.globo.com/partidas/18'
    , 'https://api.cartolafc.globo.com/partidas/19'
    , 'https://api.cartolafc.globo.com/partidas/20'
    , 'https://api.cartolafc.globo.com/partidas/21'
    , 'https://api.cartolafc.globo.com/partidas/22'
    , 'https://api.cartolafc.globo.com/partidas/23'
    , 'https://api.cartolafc.globo.com/partidas/24'
    , 'https://api.cartolafc.globo.com/partidas/25'
    , 'https://api.cartolafc.globo.com/partidas/26'
    , 'https://api.cartolafc.globo.com/partidas/27'
    , 'https://api.cartolafc.globo.com/partidas/28'
    , 'https://api.cartolafc.globo.com/partidas/29'
    , 'https://api.cartolafc.globo.com/partidas/30'
    , 'https://api.cartolafc.globo.com/partidas/31'
    , 'https://api.cartolafc.globo.com/partidas/32'
    , 'https://api.cartolafc.globo.com/partidas/33'
    , 'https://api.cartolafc.globo.com/partidas/34'
    , 'https://api.cartolafc.globo.com/partidas/35'
    , 'https://api.cartolafc.globo.com/partidas/36'
    , 'https://api.cartolafc.globo.com/partidas/37'
    , 'https://api.cartolafc.globo.com/partidas/38']


#def partidas_func(teste):

for url in url_list:

    path_brutos = '/tmp/stage/partidas_{}_de_{}_raw.json'.format(ano, rodada)
    path_limpos = '/tmp/stage/partidas_{}_de_{}_clean.csv'.format(ano, rodada)
    rodada = rodada + 1

    # pega resultado json da API
    response = requests.get(url)
    data = response.json()

    #salva em json
    with open(path_brutos, 'w') as f:
        json.dump(data, f)

    # Atribui a variavel valor da rodada

    df_rodada = data['rodada']
    df_clubes = data['clubes']








    ## ETL Informações da partida
    df = pd.DataFrame(data['partidas'])
    df_clean = df.drop(['transmissao', 'aproveitamento_visitante', 'aproveitamento_mandante','status_transmissao_tr',
                        'inicio_cronometro_tr','status_cronometro_tr','clube_visitante_posicao',
                        'timestamp', 'clube_casa_posicao','periodo_tr','partida_id'], axis=1)
    # add colunas
    df_clean['Rodada'] = df_rodada
    df_clean['dt_Atualizacao'] = time.strftime("%d/%m/%Y")
    df_clean['Jogo']=None
    df_clean['Resultado']=None
    df_clean['ano'] = ano



    ## Renomeia colunas
    df_clean=df_clean.rename(columns={ 'round' : 'Rodada', 'partida_data' : 'PartidaData',
                                  'clube_casa_id': 'TimeCasa', 'clube_visitante_id': 'TimeVisitante',
                                       'local': 'Arena', 'placar_oficial_mandante': 'PlacarCasa',
                                       'placar_oficial_visitante' : 'PlacarVisitante'
                                       })

    # Reorg e drop coluna score

    df_clean = df_clean[['Jogo', 'Rodada', 'PartidaData', 'TimeCasa', 'PlacarCasa', 'PlacarVisitante',
                         'TimeVisitante', 'Arena', 'Resultado', 'valida', 'dt_Atualizacao','ano']]



    ## Salva arquivos limpos
    df_clean.to_csv(path_limpos, index=False)










