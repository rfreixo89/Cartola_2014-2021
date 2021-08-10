drop table if exists Clubes_id_2014_2018;
drop table if exists Clubes_id_2014_2018_tmp;

drop table if exists Clubes_id_2021;
drop table if exists Clubes_id_2021_tmp;

create external table Clubes_id_2014_2018_tmp (
NomeCBF string
,NomeCartola string
,NomeCompleto string
,Cod_2014_2016 string
,Cod_2018 string
,Cod_2018_2020 string
,id string
,abreviacao string
)
row format delimited fields terminated by ',' stored as textfile location '/datalake/cartola_dados/2014_2020/clubes'
TBLPROPERTIES ("skip.header.line.count"="1");





create external table Clubes_id_2021_tmp (
Cod_2021 string
,NomeCompleto string
,Abreviacao string
,NomeCartola string

)
row format delimited fields terminated by ',' stored as textfile location '/datalake/cartola_dados/2021/clubes'
TBLPROPERTIES ("skip.header.line.count"="1");


create table Clubes_id_2021 as select * from Clubes_id_2021_tmp ;
create table Clubes_id_2014_2018 as select * from Clubes_id_2014_2018_tmp; 



drop table Clubes_id_2021_tmp;

drop table Clubes_id_2014_2018_tmp; 

