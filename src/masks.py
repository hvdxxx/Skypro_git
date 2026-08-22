def get_mask_card_number(card_number: str) -> str:
    """Функция, маскирующий номер карты"""
    card_number = card_number.replace(" ", "")
    if len(card_number) == 16 and card_number.isdigit() == True:
        first_block = card_number[:4]
        second_block = card_number[4:6] + "**"
        third_block = "****"
        fourth_block = card_number[-4:]
        return f"{first_block} {second_block} {third_block} {fourth_block}"
    else:
        return "Длина номера карты не совпадает"


def get_mask_account(account_id: str) -> str:
    """Функция, маскирует счет"""
    account_number = account_id.replace(" ", "")
    if len(account_id) == 20 and account_id.isdigit() == True:
        mask_number = "**" + account_number[-4:]
        return mask_number
    else:
        return "Длина номера аккаунта не совпадает"


#print(get_mask_card_number("7000792289606361"))
#print(get_mask_account("73654108430135874305"))
