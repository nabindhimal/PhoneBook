import json, os

CONTACT_FILE = "contacts.json"


def load_contacts():
    if os.path.exists(CONTACT_FILE):
        with open(CONTACT_FILE, "r") as file:
            return json.load(file)
    return {}


def save_contacts():
    # existing_contacts = load_contacts()
    contacts.update(contacts)
    with open(CONTACT_FILE, "w") as file:
        json.dump(contacts, file)


contacts = load_contacts()


def main():
    tasks = {1: 'Add Contact', 2: 'Delete Contact', 3: 'Find Contact', 4: 'Update Contact', 5: 'View Contact',
             6: 'Exit'}


    while True:
        print("\n")
        print(tasks)
        choice = int(input('Choose an option: '))

        if choice == 1:
            add_contact()
        elif choice == 2:
            delete_contact()
        elif choice == 3:
            find_contact()
        elif choice == 4:
            update_contact()
        elif choice == 5:
            view_contact()
        elif choice == 6:
            exit(0)
        else:
            print('Invalid choice.')


def add_contact():
    try:
        name = input("Enter name: ")
        email = input("Enter email: ")
        number = input("Enter number: ")
        contacts[email] = {'name': name, 'number': number}
        save_contacts()
    except KeyError:
        print("Email already exists. Please enter a different email.")


def delete_contact():
    email = input("Enter email: ")
    if email in contacts:
        del contacts[email]
        save_contacts()
        print(f"Contact with {email} removed.")
    else:
        print("No contact with that email is available.")


def find_contact():
    try:
        email = input("Enter email: ")
        print(contacts[email])
    except KeyError:
        print("Email not found.")


def view_contact():
    print(contacts)


def update_contact():
    try:
        email = input("Enter email of the contact to update: ")
        name = input("Enter new name: ")
        number = input("Enter new number: ")
        contacts[email] = {'name': name, 'number': number}
        save_contacts()
        print("Contact Updated Successfully!")
    except KeyError:
        print("Invalid email.")


main()
