text = "Загальний дохід працівника складається з\
    декількох частин: 1000.01 як основний дохід,\
    доповнений додатковими надходженнями 27.45 і 324.00 доларів."

from typing import Callable
import re

def generator_numbers(text: str):
    text_list = text.split(" ")
    numbers = r'\b\d+\.\d+\b'
    num = re.findall(numbers, text)
    for n in num:
        yield float(n)

def sum_profit(text: str, func: Callable):
    return f'Загальний дохід: {sum(func(text))}'

g = sum_profit(text, generator_numbers)
print(g)
