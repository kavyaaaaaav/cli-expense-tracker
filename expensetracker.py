import json
from datetime import datetime
FILE='expenses.json'
def load():
    f=open(FILE,'r')
    return json.load(f)
def save(data):
    f=open(FILE,'w')
    json.dump(data,f)
def add():
    desc=input('enter description')
    amt=float(input('enter amount'))
    data=load()
    expense = {
    "id": len(data) + 1,
    "date": str(datetime.now().date()),
    "desc": desc,
    "amt": amt
}
    data.append(expense)
    save(data)
    print('ADDED')
def show():
    data=load()
    print('\nID    DATE    DESC    AMOUNT')
    for e in data:
        print(f"{e['id']}   {e['date']}  {e['desc']}    ${e['amt']}")
def delete():
    iddel = int(input("Enter ID to be deleted: "))
    data = load()  # assuming load() returns a list of dicts

    for i in data:
        if i['id'] == iddel:
            data.remove(i)
            print(f"Entry with ID {iddel} deleted.")
            break
    else:
        print(f"No entry found with ID {iddel}.")

    save(data)  # assuming save() writes the updated list back
# summary
def summary():
    data = load()
    total = sum(e["amt"] for e in data)
    print(f"Total expenses: ${total}")


# menu loop
while True:
    print("\n1.Add  2.Show  3.Delete  4.Summary  5.Exit")
    choice = input("Choose: ")

    if choice == "1":
        add()
    elif choice == "2":
        show()
    elif choice == "3":
        delete()
    elif choice == "4":
        summary()
    elif choice == "5":
        break
    else:
        print("Invalid 😭")
    
    

