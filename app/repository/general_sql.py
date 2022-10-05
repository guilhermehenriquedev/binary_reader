import psycopg2, logging
from ech.settings import *
from app.helpers.sql import dictfetchall

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
fh = logging.FileHandler('log/application.log')
fh.setFormatter(formatter)
logger.addHandler(fh)

def query_select(sql=None):
    ''' Executa comandos sql na tabela ech '''

    logger.debug(f'Executando ação de busca no banco de dados a partir do sql ....: {sql}')
    conn = psycopg2.connect(
        dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()   
    

    data = dictfetchall(cur)
    
    # Fecha as conexões
    cur.close
    conn.close()

    return data if data else None


def query_insert(sql=None):
    ''' Executa comandos sql na tabela ech '''

    logger.debug(f'Executando ação de inserção no banco de dados a partir do sql ....: {sql}')
    conn = psycopg2.connect(
        dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()   
        
    # Fecha as conexões
    cur.close
    conn.close()

    return 'Inserção ok'

if __name__ == '__main__':

    from app.repository.general_sql import Query
    _sql = """ INSERT INTO ech.echi_logs
                (no_bilhete, dth_processamento)
                VALUES('teste', '2022-06-09 17:50');
            """
    query = Query()
    query.execute(_sql)