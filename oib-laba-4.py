# |5|4006234246b4fd2b2833d740927ab20465afad862c74b1a88ec0869bde5c836c|Mastercard|Дебетовая|Альфа-банк|0254|sha256|

import multiprocessing as mp
import hashlib
from tqdm import tqdm

data = {
    'hash': '4006234246b4fd2b2833d740927ab20465afad862c74b1a88ec0869bde5c836c',
    'last_num': '0254'
}

BIN = ['510126', '519778', '521178','522828','523701',
       '530331', '530827','548673', '548674', '552175', 
       '555928', '555933', '555949', '555957', '555921'
]

def check_hash(x: int)-> int:
    for b in BIN:
        if hashlib.sha256(f'{b}{x}{data["last_num"]}'.encode()).hexdigest() == data["hash"]:
            return x
        else: return False
    
if __name__ == '__main__':
    cores = mp.cpu_count()
    print('max cores = ', cores)
    for i in range(99999, 10000000):
        if (check_hash(i) != False): print('Number of card: ', i)
    
    if check_hash('000000') != False:
             print('Number of card: 000000')
    
    # with mp.Pool(processes=5) as p:
    #     for result in p.map(check_hash, range(99999, 10000000)):
    #         if result != False:
    #             print('Number of card: ', result)
    #             p.terminate()
    #             break
    #     if check_hash('000000') != False:
    #         print('Number of card: 000000')