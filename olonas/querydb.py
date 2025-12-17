from django.db import connection

def query_taranaka(id_dadabe, id_bebe):
    q = """SELECT a.* , vadiny AS id_vady, 
        CASE WHEN b.zanaka IS NOT NULL THEN b.fiantsoana_vady ELSE 'vady?' END AS fiantsoana_vady 
        FROM(
            SELECT id, 1 as haja, 0 as fizokiana_dada, 1 as fizokiana, anarana, fanampiny, fiantsoana,lahy_vavy 
            FROM olonas_olona 
            WHERE id={id_dadabe}
            UNION SELECT id, 1 as haja, 0 as fizokiana_dada, 2 as fizokiana, anarana, fanampiny, fiantsoana,lahy_vavy 
            FROM olonas_olona 
            WHERE id={id_bebe} 
            UNION SELECT id, 2 as haja, fizokiana as fizokiana_dada, fizokiana, anarana, fanampiny, fiantsoana,lahy_vavy 
            FROM olonas_olona 
            WHERE ray ={id_dadabe} AND reny={id_bebe}
            UNION SELECT zafy.id,  3 as haja, zanaka.fizokiana, zafy.fizokiana, zafy.anarana, zafy.fanampiny, zafy.fiantsoana,zafy.lahy_vavy 
            FROM olonas_olona as zanaka  
            JOIN olonas_olona as zafy on zanaka.id = zafy.ray 
            WHERE zanaka.ray = {id_dadabe} AND zanaka.reny={id_bebe}
            UNION SELECT zafy.id,  3 as haja, zanaka.fizokiana, zafy.fizokiana, zafy.anarana, zafy.fanampiny, zafy.fiantsoana,zafy.lahy_vavy 
            FROM olonas_olona as zanaka  
            JOIN olonas_olona as zafy on zanaka.id = zafy.reny 
            WHERE zanaka.ray = {id_dadabe} AND zanaka.reny={id_bebe}
        ) as a LEFT JOIN vady as b  on a.id = b.zanaka 
        ORDER BY fizokiana_dada, haja, fizokiana """.format(id_dadabe=id_dadabe, id_bebe=id_bebe)
    with connection.cursor() as cursor:
        cursor.execute(q)
        rows = cursor.fetchall()
    return rows

def query_dada(id, lahy_vavy):
    q = """SELECT a.ray, 
        CASE 
            WHEN b.id is NULL THEN
                 'dadan '||'""" + lahy_vavy + """'||'?'
            ELSE b.anarana  
        END  AS dada_lahy
        FROM olonas_olona as a
        LEFT JOIN olonas_olona as b on a.ray = b.id 
        WHERE a.id = {id}""".format(id=id)
    with connection.cursor() as cursor:
        cursor.execute(q)
        rows = cursor.fetchall()
    return rows
    
   
def query_neny(id, lahy_vavy):
    q = """SELECT a.reny, 
        CASE 
            WHEN b.id is NULL THEN 
                'nenyn '||'""" + lahy_vavy + """'||'?'
            ELSE b.anarana  
        END  AS dada_lahy
        FROM olonas_olona as a
        LEFT JOIN olonas_olona as b on a.reny = b.id 
        WHERE a.id = {id}""".format(id=id)
    with connection.cursor() as cursor:
        cursor.execute(q)
        rows = cursor.fetchall()
    return rows


def test_lahyvavy(id):
    q="select lahy_vavy from olonas_olona where id={id}".format(id=id)
    with connection.cursor() as cursor:
        cursor.execute(q)
        rows = cursor.fetchall()
        print(rows[0])
    return rows[0][0]


