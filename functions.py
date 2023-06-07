import hashlib
import logging
import json
from matplotlib import pyplot as plt
import multiprocessing as mp
import numpy as np
import time


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


def check_hash(x: int, BIN: tuple, hash: str, last_num: str) -> tuple:
    """функция проверки хеша

    Args:
        x (int): предполагаемые цифры номера карты
        BIN (tuple): кортеж с предполагаемыми БИН 
        hash (str): значение хеша
        last_num (str): последние 4 цифры номера

    Returns:
        tuple: в случае совпадения - картеж с БИН, верным номером и последними цифрами
    """
    
    x = str(x).zfill(6)
    for b in BIN:
        if hashlib.sha256(
                f'{b}{x}{last_num}'.encode()).hexdigest() == hash:
            return (b, x, last_num)
    return False


def find_card_num(card_settings: dict) -> str:
    """функция поиска номера карты
    Args:
        card_settings (dict): набор путей фалов

    Returns:
        str: возвращет полный номер карты
    """
    
    arguments = []
    for i in range(0, 1000000):
        arguments.append((i, card_settings["bins"], card_settings["hash"], card_settings["last_numbers"]))
        
    with mp.Pool(processes=5) as p:
        for result in p.starmap(check_hash, arguments):
            if result:
                logging.info(
                    f'Number of card: {result[0]}-{result[1]}-{result[2]}')
                p.terminate()
                return (str(f'{result[0]}{result[1]}{result[2]}'))


def time_research(c: int, card_settings: dict) -> float:
    """функция посчета поиска времени, необходимого, чтобы найти номер карты при заданном количестве запускаемых процессов

    Args:
        c (int): количество процессов
        card_settings (dict): набор путей фалов

    Returns:
        float: время поиска номера карты
    """
    
    arguments = []
    for i in range(0, 1000000):
        arguments.append((i, card_settings["bins"], card_settings["hash"], card_settings["last_numbers"]))
    
    start = time.time()
    with mp.Pool(processes=c) as p:
        for result in p.starmap(check_hash, arguments):
            if result:
                end = time.time()
                logging.info(
                    f'Number of card: {result[0]}{result[1]}{result[2]}, cores = {c}')
                p.terminate()
                return end - start
    return start - time.time()


def create_bar(times: np.ndarray) -> None:
    """функция создаия графика зависимости времни поиска номера карты от количества запускаемых процессов

    Args:
        times (np.ndarray): массив времен исследования
    """
    x = np.arange(1, 21, step=1)
    plt.figure(figsize=(30, 5))
    plt.ylabel('time')
    plt.xlabel('cores')
    plt.title('research times')
    plt.bar(x, times, color='green', width=0.5)
    plt.savefig('researches.png')


def algorithm_luna(number: str) -> bool:
    """функция проверки номера карты на валидность с помощью алгоритма Луна

    Args:
        number (str): номер карты

    Returns:
        bool: логиечское значение соответствия/не соответствия
    """
    number = int(number)
    summ = 0
    i = 16
    while i >= 1:
        n = number % 10
        if i % 2 != 0:
            n *= 2
            if n >= 10:
                n -= 9
        summ += n
        number //= 10
        i -= 1
    if summ % 10 == 0:
        return True
    else:
        return False
