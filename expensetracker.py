import json
from datetime import datetime

FILE = 'expenses.json'

def load():
    try:
        with open(FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save(data):
    with open(FILE, 'w') as f:
        json.dump(data, f, indent=2)

def add():
    desc = input('Enter description: ')
    amt = float(input('Enter amount: '))
    data = load()
    expense = {
        "id": len(data) + 1,
        "date": str(datetime.now().date()),
        "desc": desc,
        "amt": amt
    }
    data.append(expense)
    save(data)
    print('✅ Expense added!')

def show():
    data = load()
    if not data:
        print('No expenses found.')
        return
    print('\nID  | DATE        | DESCRIPTION       | AMOUNT')
    print('-' * 50)
    for e in data:
        print(f"{e['id']:<4}| {e['date']:<12}| {e['desc']:<18}| ${e['amt']:.2f}")

def delete():
    iddel = int(input('Enter ID to delete: '))
    data = load()
    for i in data:
        if i['id'] == iddel:
            data.remove(i)
            save(data)
            print(f'✅ Entry {iddel} deleted.')
            return
    print(f'❌ No entry found with ID {iddel}.')

def summary():
    data = load()
