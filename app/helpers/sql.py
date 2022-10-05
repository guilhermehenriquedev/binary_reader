#Cases para serem utilizados no projeto como helpers de comandos sql


def dictfetchall(cursor):
    ''' Retorna registros do cursor como uma lista de dicionarios '''
    columns = [col[0] for col in cursor.description]

    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]