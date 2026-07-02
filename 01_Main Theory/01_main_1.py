a = int(input("first number :- "))
b = int(input("second number :- "))
if a > b:
    print("a is greater than b")
elif b > a:
    print("b is greater than a")
else:
    print("a and b are equal")



gender = str(input("Gender :- "))

if gender == "Male" or gender == "male" or gender == "M" or gender == "m":
    print("Good morning sir")
elif gender == "Female" or gender == "female" or gender == "F" or gender == "f":
    print("good morning mam")
else:
    print("good morning")




a =int(input("NUmber:- "))

if a%2 == 0:
    print("Number is even")
else:
    print("Number is odd")




name = str(input("Enter your name:- "))
age = int(input("Enter your age:- "))

if age < 18:
    print(f"Hello {name} you are not a valid voter")
else:
    print(f"Hello {name}you are a valid voter")



year = int(input("Year:- "))

if year%100==0:
    if year%400 ==0:
        print(f"{year} is leap year")
    else:
          print(f"{year} is not a leap year")
elif year/4 == year//4:
     print(f"{year} is leap year")
else:
     print(f"{year} is not a leap year")




temp = int(input("Temprature:- "))

if temp < 5:
    print("Freezing Cold")
elif temp < 30:
    print("Pleasant")
else:
    print("Very Hot")



n = int(input("your number:- "))
for i in range(n,n*10+1,n):
    print(i)





for i in range(1,11):
    if i == 5:
        print("break is encountered")
        break
    print(i)
else:
    print("no break was encountered")




n = int(input("Enter your number:- "))

for i in range(n+1):
    print("Hello World")




n = int(input("Numberr:- "))

for i in range(1,n+1):
    print(i)



n = int(input("Numberr:- "))

for i in range(0,n):
    print(n-i)




n = int(input("Number:- "))

for i in range(1,11):
    print(f"{n}*{i}={n*i}")




n = int(input("Number:- "))
j = 0
for i in range(1,n+1):
    j += i

print(j)



n = int(input("Number:- "))
j = 1
for i in range(1,n+1):
    j *= i

print(j)



n = int(input("Number:- "))
a = 0
b = 0

for i in range(1,n+1):
    if i%2==0:
        a += i 
    else:
        b += i

print(f"Even sum:- {a}")
print(f"Odd sum:- {b}")



n = int(input("Number:- "))

for i in range(1,n+1):
    if n%i == 0:
        print(i)




n = int(input("Number:- "))
a = 0

for i in range(1,n):
    if n%i ==0:
        a += i

if n == a:
    print(f"{n} is a perfect number")
else:
    print(f"{n} is not a perfect number")
    



n = int(input("Number:- "))

for i in range(2,n+1):
    if i == n:
        print(f"{n} is a prime number")
    elif n%i != 0:
        continue
    else:
        print(f"{n} is not a prime number")
        break



n = str(input("Word:- "))
rev = ""
for i in range(len(n)-1,-1,-1):
    rev = rev + n[i]

if rev == n:
    print(f"{n} is a pallindrome")
else:
    print(f"{n} is not a pallindrome")



a = ""
d = 0
c = 0
s = 0
for i in a:
    if (ord(i)>=48 and ord(i)<=57):
        d+=1
    elif (ord(i)>=97 and ord(i)<=122) or (ord(i)>=65 and ord(i)<=90):
        c+=1
    else:
        s+=1

print(f"Alphabets:- {c} , Digits:- {d} , Special character:- {s}")




n = int(input("Number:- "))

while n%10 != 0:
    print(n%10)
    n //= 10



n = int(input("Number:- "))
a = ""
rev = 0
while n%10 != 0:
    rev = (rev*10) + (a%10)
    n //= 10

print(a)



n = int(input("Number:- "))
b = n
a = ""
while n%10 != 0:
    a += str(n%10)
    n //= 10
print(a,b)
if int(a) == b:
    print(f"{b} is a pallindrome")
else:
    print(f"{b} is not a pallindrome")