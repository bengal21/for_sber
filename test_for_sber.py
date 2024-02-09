import json
from typing import List

with open('operations.json', 'r', encoding='utf8') as f:
    data = json.load(f)


def sorting_by_date(data: List) -> List:
    index_for_del = 0
    for i in data:
        if 'date' not in i:
            index_for_del = data.index(i)
    data.pop(index_for_del)
    data.sort(key=lambda x: x['date'], reverse=True)
    return data


def right_date(date: str) -> str:
    formatted_date = date.split("T")[0]
    result = formatted_date.replace('-', '.')
    return '.'.join(result.split('.')[::-1])


def hide_account_number_whom(number: str) -> str:
    hidden_number = number.split(' ')[0] + ' ' + '**' + number[-4:]
    return hidden_number


def hide_account_number_who(number: str) -> str:
    hidden_number = number.split(' ')
    if len(hidden_number) < 3:
        str_hidden_number = hidden_number[0] + ' ' + hidden_number[1][4] + ' ' + hidden_number[1][4:6] + '** ****' + ' ' + hidden_number[1][-4:]
        return str_hidden_number
    else:
        str_hidden_number = hidden_number[0] + ' ' + hidden_number[1] + ' ' + hidden_number[2][:4] + ' ' + hidden_number[2][4:6] + '** ****' + ' ' + hidden_number[2][-4:]
        return str_hidden_number


def print_message(n: int) -> List:
    result_l = []
    counter = 0
    for d in sorting_by_date(data):
        if counter == n:
            break
        date = right_date(d.get('date'))
        description = d.get('description')
        amount = d.get('operationAmount').get('amount')
        currency = d.get('operationAmount').get('currency').get('name')
        who = hide_account_number_who(d.get('from', description))
        whom = hide_account_number_whom(d.get('to'))
        if d.get('state') != 'CANCELED' and d.get('from'):
            result = f'{date} {description}\n{who} -> {whom}\n{amount} {currency}\n'
            result_l.append(result)
            counter += 1
        elif d.get('state') != 'CANCELED':
            result1 = f'{date} {description}\n{whom}\n{amount} {currency}\n'
            result_l.append(result1)
            counter += 1
    return result_l


for i in print_message(5):
    print(i)
