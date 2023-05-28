from matplotlib import pyplot as plt
import time
import hashlib
import numpy as np
import multiprocessing as mp


data = {
    'hash': '4006234246b4fd2b2833d740927ab20465afad862c74b1a88ec0869bde5c836c',
    'last_num': '0254'
}

BIN = ['510126', '519778', '521178','522828','523701',
       '530331', '530827','548673', '548674', '552175', 
       '555928', '555933', '555949', '555957', '555921'
]

def check_hash(x: int)-> tuple:
    x = str(x).zfill(6)
    for b in BIN:
        if hashlib.sha256(f'{b}{x}{data["last_num"]}'.encode()).hexdigest() == data["hash"]:
            return (b, x)
    return False
    
def find_card_num() -> str:
    with mp.Pool(processes = 5) as p:
        for result in p.map(check_hash, range(0, 1000000)):
            if result != False:
                print(f'Number of card: {result[0]}-{result[1]}-{data["last_num"]}')
                p.terminate()
                return (str(f'{result[0]}-{result[1]}-{data["last_num"]}'))
                
    
def time_research() -> np.ndarray:
    research_times = np.zeros(shape=0)
    for c in range(1, 21):  
        start = time.time() 
        with mp.Pool(processes = c) as p:
            for result in p.map(check_hash, range(0, 1000000)):
                if result != False:
                    end = time.time()
                    research_times = np.append(research_times,  end - start)
                    #logging.info(f'Number of card: {result}, cores = {c}')
                    print(f'Number of card: {result[0]}-{result[1]}-{data["last_num"]}, cores = {c}')
                    p.terminate()
                    break
    return research_times

def create_bar(times: np.ndarray) -> None:
    x = np.arange(1, 21, step=1)
    plt.figure(figsize=(30, 5))
    plt.ylabel('time')
    plt.xlabel('cores')
    plt.title('research times')
    plt.bar(x, times, color='green', width = 0.5) 
    plt.savefig('researches.png')