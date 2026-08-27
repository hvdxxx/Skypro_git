def filter_by_state(operations: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Фильтрует список словарей операций по значению ключа state"""
    return [operation for operation in operations if operation.get("state") == state]

def sort_by_date(operations: list[dict], reverse: bool = True) -> list[dict]:
    """Сортирует список словарей операций по дате"""
    return sorted(operations, key=lambda operation: operation["date"], reverse=reverse)

data = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

print("С EXECUTED", filter_by_state(data))

print("С CANCELED", filter_by_state(data, 'CANCELED'))

print(sort_by_date(data))

print(sort_by_date(data, reverse=False))