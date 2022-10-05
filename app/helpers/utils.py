import binascii


def convert_binary_to_string(data=None):
    ''' Captura o codigo binaario e converte para string '''

    str_val = binascii.b2a_base64(data, newline=True).decode('ascii').replace('\n', '')
    return str_val


def convert_binary_to_int(data=None):
    ''' Captutra o codigo binario e converte para inteiro '''
    int_val = int.from_bytes(data, "little")
    return int_val
