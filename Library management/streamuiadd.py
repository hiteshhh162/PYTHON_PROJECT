# ================================
# LIBRARY MANAGEMENT SYSTEM
# STREAMLIT VERSION
# ================================

import streamlit as st
import json
import random
import string
from pathlib import Path
from datetime import datetime


# =================================
# LIBRARY CLASS
# =================================

class Library:

    database = "library.json"

    data = {
        "books": [],
        "members": []
    }

    # =============================
    # LOAD DATA
    # =============================
    if Path(database).exists():

        with open(database, "r") as f:

            content = f.read().strip()

            if content:
                data = json.loads(content)

    else:

        with open(database, "w") as f:
            json.dump(data, f, indent=4)

    # =============================
    # SAVE DATA
    # =============================
    @classmethod
    def save_data(cls):

        with open(cls.database, "w") as f:

            json.dump(cls.data, f, indent=4)

    # =============================
    # GENERATE RANDOM ID
    # =============================
    @staticmethod
    def gen_id(prefix="B"):

        random_id = ""

        for i in range(5):

            random_id += random.choice(
                string.ascii_uppercase + string.digits
            )

        return prefix + "-" + random_id

    # =============================
    # ADD BOOK
    # =============================
    def add_book(self, title, author, copies):

        book = {

            "id": Library.gen_id(),

            "title": title,

            "author": author,

            "total_copies": copies,

            "Available_copies": copies,

            "added_on": datetime.now().strftime("%d-%m-%Y")

        }

        Library.data["books"].append(book)

        Library.save_data()

    # =============================
    # ADD MEMBER
    # =============================
    def add_member(self, name, email):

        member = {

            "id": Library.gen_id("M"),

            "name": name,

            "email": email,

            "borrowed": []

        }

        Library.data["members"].append(member)

        Library.save_data()

    # =============================
    # BORROW BOOK
    # =============================
    def borrow_book(self, member_id, book_id):

        members = [
            m for m in Library.data["members"]
            if m["id"] == member_id
        ]

        if not members:
            return "Member ID not found"

        member = members[0]

        books = [
            b for b in Library.data["books"]
            if b["id"] == book_id
        ]

        if not books:
            return "Book ID not found"

        book = books[0]

        if book["Available_copies"] <= 0:
            return "No copies available"

        borrow_entry = {

            "book_id": book["id"],

            "title": book["title"],

            "borrow_on": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

        }

        member["borrowed"].append(borrow_entry)

        book["Available_copies"] -= 1

        Library.save_data()

        return "Book Borrowed Successfully"

    # =============================
    # RETURN BOOK
    # =============================
    def return_book(self, member_id, book_id):

        members = [
            m for m in Library.data["members"]
            if m["id"] == member_id
        ]

        if not members:
            return "Member ID not found"

        member = members[0]

        borrowed_books = member["borrowed"]

        selected_book = None

        for b in borrowed_books:

            if b["book_id"] == book_id:
                selected_book = b
                break

        if not selected_book:
            return "This member did not borrow this book"

        member["borrowed"].remove(selected_book)

        books = [
            bk for bk in Library.data["books"]
            if bk["id"] == book_id
        ]

        if books:
            books[0]["Available_copies"] += 1

        Library.save_data()

        return "Book Returned Successfully"


# =================================
# OBJECT
# =================================

obj = Library()

# =================================
# STREAMLIT UI
# =================================

st.set_page_config(
    page_title="Library Management System",
    layout="centered"
)

st.title("📚 Library Management System")

menu = st.sidebar.selectbox(

    "Choose Option",

    [
        "Add Book",
        "View Books",
        "Add Member",
        "View Members",
        "Borrow Book",
        "Return Book"
    ]
)

# =================================
# ADD BOOK
# =================================

if menu == "Add Book":

    st.header("➕ Add New Book")

    title = st.text_input("Enter Book Title")

    author = st.text_input("Enter Author Name")

    copies = st.number_input(
        "Enter Number Of Copies",
        min_value=1,
        step=1
    )

    if st.button("Add Book"):

        obj.add_book(title, author, copies)

        st.success("Book Added Successfully ✅")

# =================================
# VIEW BOOKS
# =================================

elif menu == "View Books":

    st.header("📖 Books List")

    books = Library.data["books"]

    if books:

        for b in books:

            with st.container():

                st.subheader(b["title"])

                st.write(f"🆔 ID : {b['id']}")

                st.write(f"✍️ Author : {b['author']}")

                st.write(
                    f"📚 Copies : "
                    f"{b['Available_copies']}/"
                    f"{b['total_copies']}"
                )

                st.write(f"📅 Added On : {b['added_on']}")

                st.divider()

    else:

        st.warning("No Books Found")

# =================================
# ADD MEMBER
# =================================

elif menu == "Add Member":

    st.header("👤 Add New Member")

    name = st.text_input("Enter Member Name")

    email = st.text_input("Enter Email")

    if st.button("Add Member"):

        obj.add_member(name, email)

        st.success("Member Added Successfully ✅")

# =================================
# VIEW MEMBERS
# =================================

elif menu == "View Members":

    st.header("👥 Members List")

    members = Library.data["members"]

    if members:

        for m in members:

            with st.container():

                st.subheader(m["name"])

                st.write(f"🆔 ID : {m['id']}")

                st.write(f"📧 Email : {m['email']}")

                st.write(
                    f"📚 Borrowed Books : "
                    f"{len(m['borrowed'])}"
                )

                if m["borrowed"]:

                    st.write("Borrowed Books:")

                    for b in m["borrowed"]:

                        st.write(
                            f"• {b['title']} "
                            f"({b['book_id']})"
                        )

                st.divider()

    else:

        st.warning("No Members Found")

# =================================
# BORROW BOOK
# =================================

elif menu == "Borrow Book":

    st.header("📚 Borrow Book")

    member_id = st.text_input("Enter Member ID")

    book_id = st.text_input("Enter Book ID")

    if st.button("Borrow"):

        result = obj.borrow_book(
            member_id,
            book_id
        )

        st.success(result)

# =================================
# RETURN BOOK
# =================================

elif menu == "Return Book":

    st.header("🔄 Return Book")

    member_id = st.text_input("Enter Member ID")

    book_id = st.text_input("Enter Book ID")

    if st.button("Return Book"):

        result = obj.return_book(
            member_id,
            book_id
        )

        st.success(result)