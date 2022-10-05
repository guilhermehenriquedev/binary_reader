from app.repository.general_sql import *

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
fh = logging.FileHandler('log/application.log')
fh.setFormatter(formatter)
logger.addHandler(fh)

class EchiRecords():

    def create_table_if_not_exist(self):
        logger.info('Criando banco de dados echi_records caso ele não exista')
        _sql = """ 
                CREATE TABLE IF NOT EXISTS ech.echi_records (
                id bigserial,
                acd integer,
                acwtime bigint,
                agentskilllevel integer,
                agentsurplus integer,
                agt_released integer,
                ans_attrib_id varchar(21),
                ans_locid integer,
                ansholdtime bigint,
                anslogin varchar(17),
                ansreason integer,
                asai_uui varchar(97),
                assist integer,
                audio integer,
                call_disp integer,
                callid integer,
                calling_ii varchar(3),
                calling_pty varchar(25),
                conference integer,
                consulttime integer,
                cwc1 character varying(17) COLLATE pg_catalog."default",
                cwc2 character varying(17) COLLATE pg_catalog."default",
                cwc3 character varying(17) COLLATE pg_catalog."default",
                cwc4 character varying(17) COLLATE pg_catalog."default",
                cwc5 character varying(17) COLLATE pg_catalog."default",
                da_queued integer,
                dialed_num varchar(25),
                dispivector integer,
                disppriority integer,
                dispsklevel integer,
                dispsplit integer,
                disptime integer,
                dispvdn varchar(17),
                duration integer,
                ecd_control integer,
                ecd_info integer,
                ecd_num integer,
                ecd_str varchar(17),
                eq_locid integer,
                eqloc varchar (10),
                event1 integer,
                event2 integer,
                event3 integer,
                event4 integer,
                event5 integer,
                event6 integer,
                event7 integer,
                event8 integer,
                event9 integer,
                firstvdn varchar(17),
                firstvector integer,
                held integer,
                holdabn integer,
                icrresent integer,
                icrpullreason integer,
                interruptdel integer,
                lastcwc varchar(17),
                lastdigits varchar(17),
                lastobserver varchar(17),
                malicious integer,
                netintime integer,
                obs_attrib_id varchar(21),
                obs_locid integer,
                observingcall integer,
                orig_attrib_id varchar(21),
                orig_locid integer,
                origholdtime integer,
                origlogin varchar(17),
                origreason integer,
                prefskilllevel integer,
                queuetime integer,
                ringtime integer,
                segment integer,
                segstart integer,
                segstart_utc integer,
                segstop integer,
                segstop_utc integer,
                split1 integer,
                split2 integer,
                split3 integer,
                talktime integer,
                tenant integer,
                tkgrp integer,
                transferred integer,
                ucid varchar(21),
                uui_len integer,
                vdn2 character varying(17) COLLATE pg_catalog."default",
                vdn3 character varying(17) COLLATE pg_catalog."default",
                vdn4 character varying(17) COLLATE pg_catalog."default",
                vdn5 character varying(17) COLLATE pg_catalog."default",
                vdn6 character varying(17) COLLATE pg_catalog."default",
                vdn7 character varying(17) COLLATE pg_catalog."default",
                vdn8 character varying(17) COLLATE pg_catalog."default",
                vdn9 character varying(17) COLLATE pg_catalog."default",
                CONSTRAINT records_pkey PRIMARY KEY (id)
            );
        """
        data = query(sql=_sql)
        return data


    def get_all_records():
        ''' Retorna todos os registros da tabela echi_records '''
        
        _sql = """ select * from ech.echi_records """
        data = query_select(sql=_sql)

        return data


    def insert_record(values=None):
        ''' Função responsável por inserir os dados na tabela echi_records '''
        
        print('valores da inserção de dados....: ', values)
        _sql = f""" insert into ech.echi_records 
                (acd, acwtime, agentskilllevel, agentsurplus, agt_released, ans_attrib_id, ans_locid, ansholdtime, anslogin, ansreason, asai_uui, assist, audio, call_disp, callid, calling_ii, calling_pty, conference, consulttime, cwc1, cwc2, cwc3, cwc4, cwc5, da_queued, dialed_num, dispivector, disppriority, dispsklevel, dispsplit, disptime, dispvdn, duration, ecd_control, ecd_info, ecd_num, ecd_str, eq_locid, eqloc, event1, event2, event3, event4, event5, event6, event7, event8, event9, firstvdn, firstvector, held, holdabn, icrresent, icrpullreason, interruptdel, lastcwc, lastdigits, lastobserver, malicious, netintime, obs_attrib_id, obs_locid, observingcall, orig_attrib_id, orig_locid, origholdtime, origlogin, origreason, prefskilllevel, queuetime, ringtime, segment, segstart, segstart_utc, segstop, segstop_utc, split1, split2, split3, talktime, tenant, tkgrp, transferred, ucid, uui_len, vdn2, vdn3, vdn4, vdn5, vdn6, vdn7, vdn8, vdn9)
                values{values} """
        data = query_insert(sql=_sql)
        return data
 