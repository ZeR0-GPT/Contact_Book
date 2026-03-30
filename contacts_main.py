from contacts_database import create_table
from contacts import add_contact, search_contact, delete_contact, get_all_contacts

def main():
    create_table()
    while True:
        print("\n1. Add Contact  2. Search  3. Delete  4. View All  5. Quit")
        choice = input("Choose: ")
        if choice == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            add_contact(name, phone, email)
            print("Contact added!")
        elif choice == "2":
            name = input("Search by name: ")
            results = search_contact(name)
            if results:
                for row in results:
                    print(f"[{row[0]}] {row[1]} |  {row[2]} |  {row[3]}")
            else:
                print("No contacts found.")
        elif choice == "3":
            contact_id = int(input("Contact ID to delete: "))
            delete_contact(contact_id)
            print("Deleted!")
        elif choice == "4":
            for row in get_all_contacts():
                print(f"[{row[0]}] {row[1]} |  {row[2]} |  {row[3]}")
        elif choice == "5":
            break

if __name__ == "__main__":
    main()