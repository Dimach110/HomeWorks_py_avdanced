import time
from tqdm import tqdm

def calculate_salary(n=int(10)):
    '''
    :param n: Количество операция расчёта
    :return: Ничего
    '''
    print("Осуществляется расчёт заработной платы... не выключайте компьютер пока з/п не будет перечислена ;-)")
    for i in tqdm(range(n)):
        time.sleep(0.5)
    print("Расчёт заработной платы выполнен. Если желаете перечислить, приходите завтра.")

