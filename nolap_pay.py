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