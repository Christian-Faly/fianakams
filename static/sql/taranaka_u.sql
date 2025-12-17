select * from
(
select id, 1 as haja, 0 as fizokiana_dada, fizokiana, anarana, fanampiny 
from olonas_olona 
where id =2
union select id, 2 as haja, 1 as fizokiana_dada, fizokiana, anarana, fanampiny 
from olonas_olona 
where ray= 2
union select zafy.id,  3 as haja, zanaka.fizokiana, zafy.fizokiana, zafy.anarana, zafy.fanampiny 
from olonas_olona as zanaka  
join olonas_olona as zafy on zanaka.id = zafy.ray 
where zanaka.ray= 2
) as a
order by fizokiana_dada, fizokiana