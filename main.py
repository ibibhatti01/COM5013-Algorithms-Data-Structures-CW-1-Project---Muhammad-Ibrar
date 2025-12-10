# main.py

from contact_book import ContactBook
from contact import Contact

def print_menu():
    print("\n" + "-" * 40)
    print("      CONTACT MANAGEMENT SYSTEM")
    print("-" * 40)
    print("1. Add contact")
    print("2. Update contact")
    print("3. Remove contact")
    print("4. Search by email")
    print("5. Search by name")
    print("6. List all contacts")
    print("0. Exit")
    print("-" * 40)


def main() -> None:
    book = ContactBook()
    print("Welcome to the Contacts App")

    while True:
        print_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            name = input("Name: ").strip()
            email = input("Email: ").strip()
            phone = input("Phone: ").strip()
            address = input("Address: ").strip()
            contact = Contact(name=name, email=email, phone=phone, address=address)
            if book.add_contact(contact):
                print("Contact added.")
            else:
                print("A contact with that email already exists.")

        elif choice == "2":
            email = input("Email of contact to update: ").strip()
            print("Leave a field blank to keep existing value.")
            existing = book.find_by_email(email)
            if not existing:
                print("No such contact.")
                continue
            name = input(f"New name [{existing.name}]: ").strip() or existing.name
            phone = input(f"New phone [{existing.phone}]: ").strip() or existing.phone
            address = input(f"New address [{existing.address}]: ").strip() or existing.address
            book.update_contact(email, name=name, phone=phone, address=address)
            print("Contact updated.")

        elif choice == "3":
            email = input("Email of contact to remove: ").strip()
            if book.remove_contact(email):
                print("Contact removed.")
            else:
                print("No such contact.")

        elif choice == "4":
            email = input("Email to search: ").strip()
            contact = book.find_by_email(email)
            print(contact if contact else "No such contact.")

        elif choice == "5":
            name = input("Name to search: ").strip()
            matches = book.find_by_name(name)
            if not matches:
                print("No contacts found.")
            else:
                for c in matches:
                    print(c)

        elif choice == "6":
            for c in book.list_sorted_by_name():
                print(c)

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
