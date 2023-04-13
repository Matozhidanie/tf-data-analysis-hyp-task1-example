import pandas as pd
import numpy as np


chat_id = 481557740 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # уровень значимости
    uroven = 0.08

    # конверсия историческая
    conv_history = x_success / x_cnt
    # print(conv_history)

    # конверсия со скриптом
    conv_script = y_success / y_cnt
    # print(conv_script)

    # при гипотезе принимаем p = p0 (роста со скриптом нет)
    # тестируем отклонение вверх (есть ли рост?) - альтернатива правосторонняя

    # гипотеза p<=p0
    # альтернатива p>p0

    # вычисления разницы в процентах
    raznica = round((conv_script - conv_history), 3)
    # print(round((conv_script - conv_history), 3))

    if raznica > uroven:
        otvet = bool(1) # гипотезу отклоняем (скрипт работает)
    else:
        otvet = bool(0) # гипотезу не отклоняем (скрипт фигня)

    return otvet
