import json
import os
from re import split

from classes import MyErrors

parent_dir = os.path.pardir
JSON_FILE: str = os.path.join(parent_dir, 'conditates.json')


def get_data_json():
    with open(JSON_FILE, encoding='utf-8') as file:
        data = json.load(file)

    return data


def data_request(*args):
    """
    на основе входных данных делает выборку из json
    :param args:
    :return:
    """
    # получем все данные из json
    data: list = get_data_json()
    # если аргументы в функцию не переданны
    if not args:
        return data
    # если переданный агрумент типа int(т.е id кандитата)
    elif isinstance(args[0], int):
        for elem in data:
            if elem['id'] == args[0]:
                return elem
        else:
            raise MyErrors("ID NOT FIND")
    # если переданный агрумент типа string (т.е навык(и) кандитата)
    elif isinstance(args[0], str):
        skills: list = split(',| +', args[0])
        res: list = []
        for elem in data:
            for i in range(len(skills)):
                if skills[i].lower() in elem["skills"].lower():
                    res.append(elem)

        if res:
            return res
        else:
            raise MyErrors("SKILLS NOT FIND")
