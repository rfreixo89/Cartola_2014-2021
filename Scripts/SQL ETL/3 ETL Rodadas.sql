

-- Dropa tabelas caso existam
DROP TABLE IF EXISTS cartola.rodadas_tmp;
DROP TABLE IF EXISTS cartola.rodadas;





-- cria tabela temporaria rodadas

create external table cartola.rodadas_tmp (
AtletaID string
,Apelido string
,Nome string
,Clube string
,Posicao string
,Preco string
,Rodada string
,Jogos string
,Status string
,Pontos string
,PontosMedia string
,PrecoVariacao string
,PlacarVisitante string
,PlacarCasa string
,A string
,CA string
,CV string
,DD string
,DP string
,FC string
,FD string
,FF string
,FS string
,FT string
,G string
,GC string
,GS string 
,I string
,PI string
,PP string
,DS string
,SG string
,DE string
,PC string
,ano string
,dia string
,dt_Atualizacao string )
row format delimited fields terminated by ',' stored as textfile location '/datalake/cartola_dados/rodadas'
TBLPROPERTIES ("skip.header.line.count"="1");


-- cria tabela rodadas
create  table cartola.rodadas (
AtletaID int
,Apelido string
,Nome string
,Clube string
,Posicao string
,Preco float
,Rodada string
,Jogos string
,Status string
,Pontos float
,PontosMedia float
,PrecoVariacao float
,PlacarVisitante int
,PlacarCasa int
,A int
,CA int
,CV int
,DD int
,DP int
,FC int
,FD int
,FF int
,FS int
,FT int
,G int
,GC int
,GS int 
,I int
,PI int
,PP int
,DS int
,SG int
,DE int
,PC int
,dia int
,dt_Atualizacao string
) partitioned by (ano int);


-- insere registros particionados

insert into  cartola.rodadas partition(ano)



select 
 cast( AtletaID as int)
,Apelido 
,Nome 
,Clube 
,Posicao 
, cast( Preco as float)
,Rodada 
,Jogos 
,Status 
, cast( Pontos as float)
, cast( PontosMedia as float)
, cast( PrecoVariacao as float)
, cast( PlacarVisitante as int)
, cast( PlacarCasa as int)
,cast(A as int)
,cast(CA as int)
,cast(CV as int)
,cast(DD as int)
,cast(DP as int)
,cast(FC as int)
,cast(FD as int)
,cast(FF as int)
,cast(FS as int)
,cast(FT as int)
,cast(G as int)
,cast(GC as int)
,cast(GS as int) 
,cast(I as int)
,cast(PI as int)
,cast(PP as int)
,cast(DS as int)
,cast(SG as int)
,cast(DE as int)
,cast(PC as int)
,cast(dia as int)
,dt_Atualizacao 
,cast(ano as int)

from rodadas_tmp;

DROP TABLE IF EXISTS cartola.rodadas_tmp;
