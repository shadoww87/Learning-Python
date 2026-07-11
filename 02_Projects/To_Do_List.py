# To-Do List features:

# Add task — just a task name/description
# View all tasks — show pending and completed separately
# Mark task as complete — change status from pending to done
# Delete task — remove a task entirely
# Save/load from JSON file — tasks persist between runs

import json
from pathlib import Path

database = "to_do_list.json"
data = {"List" : []}

if Path(database).exists():
    with open(database,'r') as file:
        content = file.read()
        if content:
            data = json.loads(content)

def save():
    with open(database,"w") as f:
        json.dump(data,f,indent = 4)

def addTask():
    task = input("\nEnter task name: ").lower()
    
    data['List'].append({
        "Task" : task,
        "Status" : "pending"
    })
    print(f"Task ({task}) added successfully")
    save()

def viewTask():
    if not data['List']:
        print("\nNo TASKS yet")
        return
    
    print("\nList of pending tasks")
    for i in data['List']:
        if i['Status'] == "pending":
            print(f"\n  Task : {i['Task']}")
            print(f"  Status : {i['Status']}")

    print("\nList of completed tasks")
    for i in data['List']:
        if i['Status'] == "complete":
            print(f"\n  Task : {i['Task']}")
            print(f"  Status : {i['Status']}\n")

def updateStatus():
    task = input("\nEnter task name to be updated: ").lower()
    t=0

    for i in data['List']:
        if i['Task'] == task:
            i['Status'] = "complete"
            t+=1
    
    if t == 0:
        print("\nNo such task exists")
        return
    save()

def delete():
    task = input("\nEnter task name to be deleted: ").lower()
    found = False
    for i in data['List']:
        if i['Task'] == task:
            found = True
            break

    if not found:
        print("\nNo such task exists")
        return

    data['List'] = [i for i in data['List'] if i['Task'] != task]
    print(f"\nTask ({task}) deleted successfully")
    save()


while True:
    print("\nPress 1 to ADD TASK")
    print("Press 2 to VIEW ALL TASK")
    print("Press 3 to MARK TASK AS COMPLETE")
    print("Press 4 to DELETE TASK")
    print("Press 5 to EXIT")

    try:
        choice = int(input("\nPlease input your choice :- "))
    except ValueError:
        print("\nPlease enter a number")
        continue 

    if choice == 1: 
        addTask()

    elif choice == 2: 
        viewTask()

    elif choice == 3: 
        updateStatus()

    elif choice == 4: 
        delete()

    elif choice == 5: 
        break

    else:
        print("\nEnter valid choice")
        continue