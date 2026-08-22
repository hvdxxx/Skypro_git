from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_info: str) -> str:
    """Маскирует номер карты счета в строке с названием"""
    parts = account_info.split()

    if len(parts) < 2:
        raise ValueError("Строка должна содержать название и номер")

    name = " ".join(parts[:-1])
    number = parts[-1]

    if name.lower() == "счет":
        masked_number = get_mask_account(number)
    else:
        masked_number = get_mask_card_number(number)

    return f"{name} {masked_number}"


def get_date(date_string: str) -> str:
    """Преобразует дату из формата ISO в формат ДД.ММ.ГГГГ"""
    date_part = date_string.split("T")[0]
    year, month, day = date_part.split("-")
    return f"{day}.{month}.{year}"

print(mask_account_card("Visa Platinum 7000792289606361"))