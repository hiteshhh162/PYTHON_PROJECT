import json
import random
import string
from pathlib import Path
from datetime import datetime


class Library:

    database = "library.json"

    data = {
        "books": [],
        "members": []
    }

    # =========================
    # LOAD EXISTING DATA
    # =========================
    if Path(database).exists():

        with open(database, "r") as f:

            content = f.read().strip()

            if content:
                data = json.loads(content)

    else:

        with open(database, "w") as f:

            json.dump(data, f, indent=4)

    # =========================
    # GENERATE RANDOM ID
    # =========================
    @staticmethod
    def gen_id(prefix="B"):

        random_id = ""

        for i in range(5):

            random_id += random.choice(
                string.ascii_uppercase + string.digits
            )

        return prefix + "-" + random_id

    # =========================
    # SAVE DATA
    # =========================
    @classmethod
    def save_data(cls):

        with open(cls.database, "w") as f:

            json.dump(cls.data, f, indent=4)

    # =========================
    # ADD BOOK
    # =========================
    def add_book(self):

        title = input("Enter Book Title : ")

        author = input("Enter Author Name : ")

        copies = int(
            input("Enter Number Of Copies : ")
        )

        book = {

            "id": Library.gen_id(),

            "title": title,

            "author": author,

            "total_copies": copies,

            "Available_copies": copies,

            "added_on": datetime.now().strftime(
                "%d-%m-%Y"
            )
        }

        Library.data["books"].append(book)

        Library.save_data()

        print("\nBook Added Successfully ✅")

    # =========================
    # LIST BOOKS
    # =========================
    def list_books(self):

        if not Library.data["books"]:

            print("\nNo Books Found")
            return

        print("\n" + "=" * 60)

        for b in Library.data["books"]:

            print(
                f"{b['id']:12} "
                f"{b['title'][:24]:25} "
                f"{b['author'][:19]:20} "
                f"{b['Available_copies']}/"
                f"{b['total_copies']}"
            )

        print("=" * 60)

    # =========================
    # ADD MEMBER
    # =========================
    def add_member(self):

        name = input("Enter Member Name : ")

        email = input("Enter Email : ")

        member = {

            "id": Library.gen_id("M"),

            "name": name,

            "email": email,

            "borrowed": []
        }

        Library.data["members"].append(member)

        Library.save_data()

        print("\nMember Added Successfully ✅")

    # =========================
    # LIST MEMBERS
    # =========================
    def list_member(self):

        if not Library.data["members"]:

            print("\nNo Members Found")
            return

        print("\n" + "=" * 60)

        for m in Library.data["members"]:

            print(
                f"{m['id']:12} "
                f"{m['name'][:24]:25} "
                f"{m['email'][:25]}"
            )

            print("Borrowed Books : ")

            if m["borrowed"]:

                for b in m["borrowed"]:

                    print(
                        f" - {b['title']} "
                        f"({b['book_id']})"
                    )

            else:

                print(" No Borrowed Books")

            print("-" * 60)

    # =========================
    # BORROW BOOK
    # =========================
    def borrow(self):

        member_id = input(
            "Enter Member ID : "
        ).strip()

        members = [

            m for m in Library.data["members"]

            if m["id"] == member_id
        ]

        if not members:

            print("\nMember ID Not Found")
            return

        member = members[0]

        book_id = input(
            "Enter Book ID : "
        ).strip()

        books = [

            b for b in Library.data["books"]

            if b["id"] == book_id
        ]

        if not books:

            print("\nBook ID Not Found")
            return

        book = books[0]

        if book["Available_copies"] <= 0:

            print("\nNo Copies Available")
            return

        borrow_entry = {

            "book_id": book["id"],

            "title": book["title"],

            "borrow_on": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        }

        member["borrowed"].append(
            borrow_entry
        )

        book["Available_copies"] -= 1

        Library.save_data()

        print("\nBook Borrowed Successfully ✅")

    # =========================
    # RETURN BOOK
    # =========================
    def return_book(self):

        member_id = input(
            "Enter Member ID : "
        ).strip()

        members = [

            m for m in Library.data["members"]

            if m["id"] == member_id
        ]

        if not members:

            print("\nMember ID Not Found")
            return

        member = members[0]

        if not member["borrowed"]:

            print("\nNo Borrowed Books")
            return

        print("\nBorrowed Books : ")

        for i, b in enumerate(
            member["borrowed"],
            start=1
        ):

            print(
                f"{i}. "
                f"{b['title']} "
                f"({b['book_id']})"
            )

        try:

            choice = int(
                input(
                    "\nEnter Number To Return : "
                )
            )

            selected = member[
                "borrowed"
            ].pop(choice - 1)

        except Exception:

            print("\nInvalid Choice")
            return

        books = [

            bk for bk in Library.data["books"]

            if bk["id"] == selected["book_id"]
        ]

        if books:

            books[0]["Available_copies"] += 1

        Library.save_data()

        print("\nBook Returned Successfully ✅")


# =========================
# OBJECT
# =========================
obj = Library()

# =========================
# MAIN LOOP
# =========================
while True:

    print("\n" + "=" * 50)

    print("📚 LIBRARY MANAGEMENT SYSTEM 📚")

    print("=" * 50)

    print("1 -> Add Book")

    print("2 -> List Books")

    print("3 -> Add Member")

    print("4 -> List Members")

    print("5 -> Borrow Book")

    print("6 -> Return Book")

    print("0 -> Exit")

    print("-" * 50)

    try:

        choice = int(
            input(
                "Enter Your Choice : "
            )
        )

        if choice == 1:

            obj.add_book()

        elif choice == 2:

            obj.list_books()

        elif choice == 3:

            obj.add_member()

        elif choice == 4:

            obj.list_member()

        elif choice == 5:

            obj.borrow()

        elif choice == 6:

            obj.return_book()

        elif choice == 0:

            print("\nProgram Closed Successfully")

            break

        else:

            print("\nInvalid Choice")

    except Exception as err:

        print(f"\nError : {err}")