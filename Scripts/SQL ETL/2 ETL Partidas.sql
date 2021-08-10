




-- Drop tables temporarias

drop table if exists partidas_tmp;
drop table if exists partidas;




 -- cria tabelas externas
 
 
 
create external table partidas_tmp (
Jogo string
,Rodada  string
,PartidaData string
,TimeCasa string
,PlacarCasa  string
,PlacarVisitante string
,TimeVisitante string
,Arena string
,Resultado string
,valida string
,dt_Atualizacao string
,ano string
) 

row format delimited fields terminated by ',' stored as textfile location '/datalake/cartola_dados/partidas'
TBLPROPERTIES ("skip.header.line.count"="1");

-- Cria tabela particionada 

create  table partidas (
Jogo int
,Rodada  int
,PartidaData string
,TimeCasa string
,PlacarCasa  int
,PlacarVisitante int
,TimeVisitante string
,Arena string
,Resultado string
,valida string
,dt_Atualizacao string
) partitioned by (ano int);

-- insere na tabela particionada anos de 2014 a 2018
-- Libera criação de particion






insert into partidas partition (ano)
 
 select  
 cast(Jogo as int)
,cast(Rodada as int)
,partidadata
,
Case
When timecasa ='Atletico - PR' then 'Atlético - PR'
when timecasa <> 'Atletico - PR' then timecasa
end
, cast(PlacarCasa  as int) ,cast(PlacarVisitante as int) ,

Case
When timevisitante ='Atletico - PR' then 'Atlético - PR'
when timevisitante <> 'Atletico - PR' then timecasa 
end, 
arena,
CASE
WHEN placarcasa > placarvisitante then  'Vitoria Mandante'
WHEN placarcasa = placarvisitante then 'Empate'
WHEN placarcasa < placarvisitante then  'Vitoria Visitante' 
end 
,valida 
,dt_Atualizacao 
,cast(ano as int)   from partidas_tmp
where ano in('2014','2015','2016','2017','2018');


-- insere na tabela particionada anos de 2019 a 2020



insert into partidas partition (ano)


SELECT cast(pt.jogo as int), cast(pt.rodada as int), pt.partidadata, 

case 
when c14.nomecbf is not null and c14.cod_2018 ='293' then 'Atlético - PR'
when c14.cod_2018 ='293' then 'Atlético - PR'
when c14.nomecbf is not null then c14.nomecbf
when c14.nomecbf is null then c21.nomecartola
end

, cast(pt.placarcasa as int), cast(pt.placarvisitante as int), 

Case
when c14_2.nomecbf is not null and c14_2.cod_2018 ='293' then 'Atlético - PR'
when c14_2.nomecbf is not null then c14_2.nomecbf
when c14_2.nomecbf is null then c21_2.nomecartola
end

,pt.arena,

CASE 
WHEN pt.placarcasa > pt.placarvisitante then  'Vitoria Mandante'
WHEN pt.placarcasa = pt.placarvisitante then 'Empate'
WHEN pt.placarcasa < pt.placarvisitante then  'Vitoria Visitante'

end 

, pt.valida , pt.dt_atualizacao,cast(pt.ano as int) 

FROM cartola.partidas_tmp pt
join cartola.clubes_id_2021 c21 on ( pt.timevisitante = c21.cod_2021) 
join cartola.clubes_id_2021 c21_2 on (pt.timecasa = c21_2.cod_2021)
left join clubes_id_2014_2018 c14 on (upper(c14.nomecartola)= upper(c21.nomecartola))
left join clubes_id_2014_2018 c14_2 on (upper(c14_2.nomecartola)= upper(c21_2.nomecartola))
where pt.ano in('2020','2019','2021')
;





drop table if exists partidas_tmp;

