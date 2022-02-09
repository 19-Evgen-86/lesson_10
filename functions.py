import json

JSON_FILE = 'conditates.json'


def get_data_json():
    with open(JSON_FILE, encoding='utf-8') as file:
        data = json.load(file)

    return data


def data_request(*args):
    """
     на основе входных данных делает выборку из json и передает их в функцию view
    """

    data = get_data_json()
    if not args:
        return data
    elif isinstance(args[0], int):
        for el in data:
            if el['id'] == args[0]:
                return el
    elif isinstance(args[0], str):
        res = []
        for el in data:
            if args[0] in el["skills"]:
                res.append(el)
        return res
