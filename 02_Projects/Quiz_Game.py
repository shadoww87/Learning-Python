import json 
from pathlib import Path
database = "questions.json"
data = {"question": []}

if Path(database).exists():
    with open(database, 'r') as f:
        content = f.read()
        if content:
            data = json.loads(content)
score = 0
for i in data['question']:
    print(f"\nQuestion: {i['question']}")
    print(f"1. {i['options'][0]}")
    print(f"2. {i['options'][1]}")
    print(f"3. {i['options'][2]}")
    print(f"4. {i['options'][3]}")
    try:
        ans = int(input("\nEnter your answer 1/2/3/4: "))
        if ans < 1 or ans > 4:
            print("\nInvalid choice")
            continue
    except ValueError:
        print("Please enter a number")
        continue
    answer = i['options'][ans - 1] 
    if i['answer'] == answer:
        print("Correct!")
        score+=1
    else:
        print(f"Wrong! The correct answer is: {i['answer']}")
print(f"\nYour final score is: {score}/{len(data['question'])}") 
print(f"Percentage: {score/len(data['question'])*100:.1f}%")
