select dadabe.id as id_dadabe, dadabe.anarana as anarana_dadabe, dadabe.fanampiny as fanampiny_dadabe,
 zanaka.id as id_zanaka, zanaka.anarana as anarana_zanaka, zanaka.fanampiny as fanampiny_zanaka,
 zafy.id as id_zafy, zafy.anarana as anarana_zafy, zafy.fanampiny as fanampiny_zafy
 
from olonas_olona as dadabe
left join olonas_olona as zanaka on dadabe.id = zanaka.ray
left join olonas_olona as zafy on zanaka.id = zafy.ray
where dadabe.id =2