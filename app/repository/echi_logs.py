from app.repository.general_sql import *


class EchiLogs():

    def create_table_if_not_exist(self):
        ''' Cria tabela de logs caso nao exista '''
        _sql = """CREATE TABLE ech.echi_logs (
                id bigserial not null,
                no_bilhete varchar(50),
                dth_processamento timestamp default null,
                qt_registros integer,
                CONSTRAINT logs_pkey PRIMARY KEY (id));
            """

        data = query(sql=_sql)
        return data

    def get_all_logs(self):
        ''' Busca todos os registros dos logs '''
        _sql = """ select * from ech.echi_logs;"""
        data = query_select(sql=_sql)
        return data if data else None

    def insert_logs(self, values=None):
        ''' Insere os logs na tabela '''
        _sql = f""" INSERT INTO ech.echi_logs
                    (no_bilhete, dth_processamento, qt_registros)
                    VALUES{values};
                """
        data = query_insert(sql=_sql)
        return data