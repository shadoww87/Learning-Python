from pathlib import Path
import os

def create_file():
    try:
        name= input("Enter the name of file :- ")
        path = Path(name)

        if not path.exists():
            with open(path,"w") as file:
                data = input("Enter what you want to write :- ")
                file.write(data)
                print("\nFile created successfully")
        else:
            print("Error file already exists")
    except Exception as bitch:
        print(f"An error has occured as {bitch}")


def read_file():
    try:
        name = input("Enter your file name :- ")
        path = Path(name)

        if path.exists():
            with open(path,"r") as file:
                content = file.read()
                print(f"Your file contents are :- \n{content}")
        else:
            print("Error no such file exists")
    except Exception as bitch:
        print(f"An error has occured as {bitch}")


def update_file():
    try:
        name = input("Enter your file name :- ")
        path = Path(name)

        if path.exists():
            print("OPERATIONS :- \n1. Renaming the file \n2. Appending the content \n3. Overwriting the file")
            choice = (int(input("Enter your choice :- ")))

            if choice == 1:
                newname = input("Enter new name for the file :- ")
                newpath = Path(newname)

                if not newpath.exists():
                    path.rename(newpath)
                    print("\nRenamed Successfully!")
                else:
                    print("Error! file already exists")

            elif choice==2:
                with open(path,"a") as file:
                    data = input("Enter what you want to append :- ")
                    file.write(f"\n{data}")
                    print("\nSuccessfully appended!")

            elif choice == 3:
                with open(path,"w") as file:
                    data = input("Enter what you want to overwrite :- ")
                    file.write(f"\n{data}")
                    print("\nSuccessfully overwritten!")

        else:
            print("Error file does not exists")
            
    except Exception as bitch:
        print(f"An error has occured as {bitch}")


def delete_file():
    try:
        name = input("Enter your file name :- ")
        path = Path(name)

        if path.exists():
            path.unlink()
            print("\nFile deleted succesfully")
        else:
            print("File does not exists")
    except Exception as bitch:
        print(f"An error has occured as {bitch}")


print("press 1 for creating a file \npress 2 for reading a file \npress 3 for updating a file \npress 4 for deleting a file")

choice= int(input("\nchoose any option :- "))

if choice==1:
    create_file()
elif choice==2:
    read_file()
elif choice==3:
    update_file()
elif choice==4:
    delete_file()