import json
import logging

def get_settings(settings_file: str) -> dict:
    """функция получения словаря для дальнейшего взаимодействия с файлами

    Args:
        settings_file (str): путь к файлу

    Returns:
        dict: словарь с путями файлов
    """
    settings = None
    try:
        with open(settings_file) as json_file:
            settings = json.load(json_file)
        logging.info('Settings wes successfully loaded')
    except IOError:
        logging.warning(f'Error reading file {settings_file}')
    return settings

def get_text(file_name: str) -> str:
    """функция получения текста из файла

    Args:
        file_name (str): путь к файлу

    Returns:
        str: получаемая строка
    """
    text = ""
    try:
        with open(file_name, mode='r') as text_file:
            text = text_file.read()
        logging.info('Text was successfully loaded')
    except IOError:
        logging.warning(f'Error reading file {file_name}')
    return text

def get_tuple(file_name: str) -> tuple:
    """функция получения кортежа из файла

    Args:
        file_name (str): путь к файлу

    Returns:
        tuple: кортеж с данными
    """
    arr = ()
    try:
        with open(file_name, mode='r') as text_file:
            arr = text_file.readlines()
        arr = tuple(map(int, arr))
        logging.info('Tuple was successfully loaded')
    except IOError:
        logging.warning(f'Error reading file {file_name}')
    return arr