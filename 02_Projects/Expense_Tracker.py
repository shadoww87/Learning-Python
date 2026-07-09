# Expense Tracker — features to build:

# Add expense (amount, category, description, date)
# View all expenses
# View total spent
# Filter by category
# Save/load from JSON file 


import json
from pathlib import Path

database = "expenses.json"
data = {"expenses" : []}

if Path(database).exists():
    with open(database,'r') as file:
        content = file.read()
        if content:
            data = json.loads(content)

def save():
    with open(database,"w") as f:
        json.dump(data,f,indent = 4)

def category():
    print("\nPress 1 for FOOD expense")
    print("Press 2 for TRANSPORT expense")
    print("Press 3 for SHOPPING expense")
    print("Press 4 for HEALTH expense")
    print("Press 5 for EDUCATION expense")
    print("Press 6 for ENTERTAINMENT expense")
    print("Press 7 for BILLS expense")
    print("Press 8 for OTHER expense")


def expense():
    amt = float(input("\nEnter amount spent : "))
    category()
    cat = int(input("\nChoose category : "))
    if cat < 1 or cat > 8:
        print("Invalid category")
        return
    categories = ["Food", "Transport", "Shopping", "Health", "Education", "Entertainment", "Bills", "Other"]
    categ = categories[cat - 1] 
    desc = input("Description : ")
    date = input("Date : ")

    data['expenses'].append({
        "Amount" : amt,
        "Category" : categ,
        "Description" : desc,
        "Date(DD/MM/YY)" : date
    })
    save()
    print(f"\nExpense of {amt} added successfully")

def view():
    if not data['expenses']:
        print("No expenses yet")
        return
    
    for i in data['expenses']:
        print(f"\n    Amount : {i['Amount']}")
        print(f"   Category : {i['Category']}")
        print(f"   Description : {i['Description']}")
        print(f"   Date(DD/MM/YY) : {i['Date(DD/MM/YY)']}")
        
def total():
    if not data['expenses']:
        print("No expenses yet")
        return
    total = 0
    for i in data['expenses']:
        total += i['Amount']
    print(f"\nTotal Expenses : {total}")
    

def spec_cat():
    t=0
    category()
    categories = ["Food", "Transport", "Shopping", "Health", "Education", "Entertainment", "Bills", "Other"]
    cat = int(input("Choose category : "))
    if cat < 1 or cat > 8:
        print("Invalid category")
        return
    categ = categories[cat - 1]
    for i in data['expenses']:
        if i['Category'] == categ:
            print(f"\n    Amount : {i['Amount']}")
            print(f"   Category : {i['Category']}")
            print(f"   Description : {i['Description']}")
            print(f"   Date(DD/MM/YY) : {i['Date(DD/MM/YY)']}") 
            t+=1
    if t==0:
        print(f"\nNo expenses in {categ}")
        return

while True:
    print("\nPress 1 to Add expense")
    print("Press 2 to View all expenses")
    print("Press 3 to View total spent")
    print("Press 4 to View expense of specific category")
    print("Press 5 to exit")
    
    try:
        choice = int(input("\nPlease enter your choice : "))
    except ValueError:
        print("Invalid Choice")
        continue


    if choice == 1:
        expense()

    elif choice == 2:
        view()

    elif choice == 3:
        total()

    elif choice == 4:
        spec_cat()

    elif choice == 5:
        print("Exit successfull")
        break

    else:
        print("Invalid Choice")
        continue


