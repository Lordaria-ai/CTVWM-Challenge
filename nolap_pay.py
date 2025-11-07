#GLOBAL DATADASE
user_database = {
    "0543402157": {
        "pin": "2222",
        "balance": 15000.00
    },
    "0243988660": {
        "pin": "1234",
        "balance": 10000.00
    },
    "0244989678": {
        "pin": "1235",
        "balance": 5000.00
    }
}

current_user_phone = None

def confirm_phone(phone):
    return phone.isdigit() and len(phone) == 10
def confirm_pin(pin):
    return pin.isdigit() and len(pin) == 4
def transfer_fee(amount):
    fee = 0.0075 * amount
    return min(fee, 15.00)
def withdrawal_fee(amount):
    fee = 0.01 * amount
    return min(fee, 20.00)

