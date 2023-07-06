"""Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: имена str, ставка
int, премия str с указанием процентов вида “10.25%”. В результате получаем словарь с именем в качестве ключа
и суммой премии в качестве значения. Сумма рассчитывается"""
from typing import List, Dict


def prem(names: List[str], cash: List[int], percent: List[str]) -> Dict[str, float]:
    return {name: money / 100 * perc for name, money, perc in zip(names, cash, (float(i[:-1]) for i in percent))}


list1: List[str] = ['Денис', 'Никита', 'Ольга', 'Пётр']
list2: List[int] = [100, 150, 200, 250]
list3: List[str] = ['10.25%', '12.25%', '15.25%', '20.25%']

print(prem(list1, list2, list3))
