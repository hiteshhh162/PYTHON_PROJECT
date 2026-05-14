from pathlib import Path
import shutil


# =========================
# CREATE FOLDER
# =========================
def create_folder():
    try:
        name = input("Please Enter your folder name : ")

        p = Path(name)

        if not p.exists():
            p.mkdir()
            print("Folder Created Successfully")
        else:
            print("Folder already exists")

    except Exception as err:
        print(f"Sorry an error occurred as {err}")


# =========================
# READ FILES & FOLDERS
# =========================
def read_file_folder():
    p = Path(".")

    items = list(p.rglob("*"))

    if not items:
        print("No files or folders found")
    else:
        for i, v in enumerate(items):
            print(f"{i + 1} : {v}")


# =========================
# UPDATE FOLDER
# =========================
def update_folder():
    read_file_folder()

    try:
        old_name = input("Enter your folder name you want to update : ")

        p = Path(old_name)

        if p.exists() and p.is_dir():

            new_name = input("Enter your new folder name : ")

            new_p = Path(new_name)

            if not new_p.exists():
                p.rename(new_p)
                print("Your folder updated successfully")
            else:
                print("Folder name already exists")

        else:
            print("Sorry no such folder exists")

    except Exception as err:
        print(f"An Error occurred as {err}")


# =========================
# DELETE FOLDER
# =========================
def delete_folder():
    try:
        read_file_folder()

        name = input("Enter folder name you want to delete : ")

        p = Path(name)

        if p.exists() and p.is_dir():

            # DELETE FOLDER EVEN IF FILES EXIST
            shutil.rmtree(p)

            print("Your Folder deleted successfully")

        else:
            print("Sorry your folder was not found")

    except Exception as err:
        print(f"There was an error as {err}")


# =========================
# READ FILE
# =========================
def read_file():
    try:
        read_file_folder()

        name = input("Enter a file name you want to read : ")

        p = Path(name)

        if p.exists() and p.is_file():

            with open(name, 'r', encoding='utf-8') as fs:
                content = fs.read()

                print("\nYour file content is...\n")
                print(content)

        else:
            print("File not found")

    except Exception as err:
        print(f"An Error occurred as {err}")


# =========================
# CREATE FILE
# =========================
def create_file():
    try:
        read_file_folder()

        name = input("Enter a file name you want to create : ")

        p = Path(name)

        if not p.exists():

            with open(name, "w", encoding='utf-8') as fs:

                data = input("Enter data you want to add in file : ")

                fs.write(data)

            print("Your file was successfully created")

        else:
            print("This file name already exists")

    except Exception as err:
        print(f"An error occurred as {err}")


# =========================
# UPDATE FILE
# =========================
def update_file():
    try:
        read_file_folder()

        name = input("Enter file name you want to update : ")

        p = Path(name)

        if p.exists() and p.is_file():

            print("\nOptions :-")
            print("1 -> Rename the file")
            print("2 -> Append data in file")
            print("3 -> Overwrite file content")

            choice = int(input("Enter your choice : "))

            # RENAME FILE
            if choice == 1:

                new_name = input("Enter your new file name with extension : ")

                new_p = Path(new_name)

                if not new_p.exists():

                    p.rename(new_p)

                    print("Your file renamed successfully")

                else:
                    print("Sorry this file name already exists")

            # APPEND DATA
            elif choice == 2:

                with open(name, 'a', encoding='utf-8') as fs:

                    data = input("What do you want to append : ")

                    fs.write("\n" + data)

                print("File appended successfully")

            # OVERWRITE FILE
            elif choice == 3:

                with open(name, 'w', encoding='utf-8') as fs:

                    data = input("Enter new content : ")

                    fs.write(data)

                print("File overwritten successfully")

            else:
                print("Invalid choice")

        else:
            print("File not found")

    except Exception as err:
        print(f"An Error occurred as {err}")


# =========================
# DELETE FILE
# =========================
def delete_file():
    try:
        read_file_folder()

        name = input("Enter a file name with extension you want to delete : ")

        p = Path(name)

        if p.exists() and p.is_file():

            p.unlink()

            print("File deleted successfully")

        else:
            print("Your file was not found")

    except Exception as err:
        print(f"An Error Occurred as {err}")


# =========================
# MAIN PROGRAM
# =========================
while True:

    print("\n========== FILE & FOLDER MANAGER ==========")

    print("1 -> Create a folder")
    print("2 -> Read files & folders")
    print("3 -> Update folder name")
    print("4 -> Delete folder")
    print("5 -> Create a file")
    print("6 -> Read a file")
    print("7 -> Update a file")
    print("8 -> Delete a file")
    print("9 -> Exit")

    try:

        choice = int(input("\nEnter your choice : "))

        if choice == 1:
            create_folder()

        elif choice == 2:
            read_file_folder()

        elif choice == 3:
            update_folder()

        elif choice == 4:
            delete_folder()

        elif choice == 5:
            create_file()

        elif choice == 6:
            read_file()

        elif choice == 7:
            update_file()

        elif choice == 8:
            delete_file()

        elif choice == 9:
            print("Program Closed Successfully")
            break

        else:
            print("Invalid Choice")

    except Exception as err:
        print(f"An error occurred as {err}")