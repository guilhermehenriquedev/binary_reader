import os
import shutil
import logging
from ech.settings import DIRECTORY_FILE, DIRECTORY_HISTORY
from app.helpers.utils import (convert_binary_to_int, 
                               convert_binary_to_string)
from app.helpers.camposrecords import campos_records
from app.repository.echi_records import EchiRecords


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
fh = logging.FileHandler('log/application.log')
fh.setFormatter(formatter)
logger.addHandler(fh)


class TicketManager():
    
    def __init__(self, directory=DIRECTORY_FILE, historico=DIRECTORY_HISTORY):
        self.directory = directory
        self.historico = historico

    def identify_binary_type_and_convert(self, binary=None, type=None):
        ''' Função responsável por identificar o tipo do binario e converter para seu respectivo tipo '''
        try:
            if type == "int":
                return convert_binary_to_int(data=binary)
            elif type == "char":
                return convert_binary_to_string(data=binary)
        except Exception as err:
            logger.error(f'Houve um erro na identificação do binário....: {err}')


    def move_archive(self, archive_name=None):
        ''' Função responsável por mover arquivo tratado para uma pasta de historico'''
        try:
            logger.debug('Movendo arquivo para o diretório de processados')    
            source = self.directory + archive_name
            destination = self.historico + archive_name
            shutil.move(source, destination)
        except Exception as err:
            logger.error(f'Houve um erro ao mover o arquivo...: {err}')


    def execute(self):
        ''' Executa todo o caso de uso para gerenciamento dos bilhetes '''

        os.chdir(self.directory)
        # Percorre todos os arquivos do diretorio
        for file in os.listdir():
            try:
                # Abre o arquivo corrente
                with open(file, "rb") as f:
                    logger.debug(f'Entrando no arquivo...: {f.name}')
                    values = []

                    for key in campos_records:
                        field_size = campos_records[key][0]
                        field_type = campos_records[key][1]
                        
                        byte = f.read(field_size)
                        value_key = self.identify_binary_type_and_convert(binary=byte, type=field_type)
                        
                        values.append(value_key) 

                    #Faz a inserção dos dados na tabela echi_records
                    EchiRecords.insert_record(values=tuple(values))
                    
                    # Grava dados na tabela de historico de logs (echi_log)
                    
                    #retira arquivo do FTP e move para uma pasta dos arquivos processados
                    self.move_archive(archive_name=f.name)
                    logger.info(f'Conversão do arquivo {f.name} realizada com sucesso e gravado no banco de dados!')

            except Exception as err:
                logger.error(f'Houve um erro na execução...: {err}')

if __name__ == '__main__':
    from app.usecases.ticket_manager import TicketManager
    echi_converter = TicketManager()
    echi_converter.execute()