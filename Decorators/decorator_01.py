from datetime import datetime

def logger(income_function):
    '''
    Декоратор для логирования выполняемых функций.
    Для использования декоратора разместите его над нужной функцией @logger.
    Log файл создаётся с именем logfile.txt
    :param income_function:
    :return:
    '''
    def log_function(*args, **kwargs):
        d_log = datetime.now().strftime('%d-%m-%y')
        t_log = datetime.now().strftime('%H:%M')
        result = income_function(*args, **kwargs)
        text = f'{d_log} {t_log}: Запущена функция "{income_function.__name__}" c аргументами: {[arg for arg in args]}.' \
               f'Функция вернула значение {result} \n'
        with open('../logfile.txt', mode='a', encoding='UTF-8') as file:
            file.write(text)
        return result
    return log_function

@logger
def square(a):
    res = a * a
    return res

@logger
def sum_f(*args):
    return sum(args)

print(sum_f(3,4,5))
print(square(5))