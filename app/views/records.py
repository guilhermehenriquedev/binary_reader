import logging
from rest_framework.permissions import AllowAny
from rest_framework import viewsets, status
from app.repository.echi_records import EchiRecords
from rest_framework.response import Response
from app.usecases.ticket_manager import TicketManager
from rest_framework.decorators import action

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
fh = logging.FileHandler('log/application.log')
fh.setFormatter(formatter)
logger.addHandler(fh)


class RecordsViewSet(viewsets.ViewSet):
    ''' Endpoint para exibir dados da tabela echi_records '''

    permission_classes = (AllowAny,)

    def list(self, request):
        ''' Listagem geral '''
        try:
            logger.info('Consultando dados na tabela echi_records')
            data = EchiRecords.get_all_records()

        except Exception as err:
            logger.error(f'Houve um erro na busca dos dados {err}')
            return Response(data={'error': err}, status=status.HTTP_400_BAD_REQUEST)

        return Response(data=data, status=status.HTTP_200_OK)


    @action(detail=False, methods=['get'], url_path='echi_convert')
    def echi_convert(self, request):
        try:
            #Chama o gerenciador e conversor dos bilhetes
            logger.info('Iniciando leitura, conversão e inserção de binário na tabela echi_records, a partir da view')
            TicketManager().execute()

        except Exception as err:
            logger.error(f'Houve um erro na execução da view echi_convert {err}')
            return Response(data={'error': err}, status=status.HTTP_400_BAD_REQUEST)
            
        logger.info('Ação de leitura, conversão e inserção realizada com sucesso!')
        return Response(data="Execução realizada com sucesso!", status=status.HTTP_200_OK)