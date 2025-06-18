import sys

def initial_phonebook():
    rows = int(input("Please enter an initial number of contacts: "))
    phone_book = []

    for i in range(rows):
        print(f"\nEnter contact {i + 1} details:")
        contact = []

        name = input("Name* : ").strip()
        if not name:
            sys.exit("Name is a mandatory field. Exiting due to blank field.")
        contact.append(name)

        number = input("Enter number* : ").strip()
        contact.append(number if number else None)

        email = input("Enter email* : ").strip()
        contact.append(email if email else None)

        dob = input("Enter date of birth (dd/mm/yy): ").strip()
        contact.append(dob if dob else None)

        category = input("Enter category (family/friends/college): ").strip()
        contact.append(category if category else None)

        phone_book.append(contact)

    return phone_book

def menu():
    print("\n" + "." * 60)
    print("\t\tSMARTPHONE DIRECTORY")
    print("." * 60)
    print("You can now perform the following operations on this phonebook:\n")
    print("1. Add a new contact")
    print("2. Remove an existing contact")
    print("3. Delete all contacts")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Exit phonebook")
    choice = int(input("Please enter your choice: "))
    return choice

def add_contact(pb):
    contact = []

    name = input("Enter name* : ").strip()
    if not name:
        sys.exit("Name is a mandatory field. Exiting due to blank field.")
    contact.append(name)

    number = input("Enter number* : ").strip()
    contact.append(number if number else None)

    email = input("Enter email* : ").strip()
    contact.append(email if email else None)

    dob = input("Enter date of birth (dd/mm/yy): ").strip()
    contact.append(dob if dob else None)

    category = input("Enter category (family/friends/college): ").strip()
    contact.append(category if category else None)

    pb.append(contact)
    return pb

def remove_contact(pb):
    name_to_remove = input("Enter the name of the contact you wish to remove: ")
    for i, contact in enumerate(pb):
        if contact[0].lower() == name_to_remove.lower():
            removed = pb.pop(i)
            print("Contact removed:", removed)
            return pb
    print("Contact not found.")
    return pb

def delete_all(pb):
    pb.clear()
    print("All contacts deleted.")
    return pb

def search_existing(pb):
    print("Search by:\n1. Name\n2. Number\n3. Email\n4. DOB\n5. Category")
    choice = int(input("Enter search criteria: "))
    value = input("Enter the search value: ").strip()

    matches = []
    for contact in pb:
        if contact[choice - 1] and contact[choice - 1].lower() == value.lower():
            matches.append(contact)

    if matches:
        display_all(matches)
    else:
        print("No matching contact found.")

def display_all(pb):
    if not pb:
        print("Phonebook is empty.")
    else:
        print("\nAll contacts:")
        for contact in pb:
            print(contact)

def thanks():
    print("." * 60)
    print("Thank you for using the smartphone directory system.")
    print("Goodbye, have a nice day!")
    print("." * 60)
    sys.exit()

# Main driver code
print("." * 60)
print("Welcome to the Smartphone Directory System")
print("." * 60)

pb = initial_phonebook()
while True:
    ch = menu()
    if ch == 1:
        pb = add_contact(pb)
    elif ch == 2:
        pb = remove_contact(pb)
    elif ch == 3:
        pb = delete_all(pb)
    elif ch == 4:
        search_existing(pb)
    elif ch == 5:
        display_all(pb)
    elif ch == 6:
        thanks()
    else:
        print("Invalid choice. Please try again.")
    