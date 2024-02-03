import json
class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        contact = {"name": name, "phone": phone, "email": email, "address": address}
        self.contacts.append(contact)
        print("Contact added successfully!")

    def view_contact_list(self):
        if not self.contacts:
            print("Contact list is empty.")
        else:
            for index, contact in enumerate(self.contacts, start=1):
                print(f"{index}. Name: {contact['name']}, Phone: {contact['phone']}")

    def search_contact(self, keyword):
        results = [contact for contact in self.contacts if keyword.lower() in contact['name'].lower() or keyword in contact['phone']]
        if results:
            for contact in results:
                print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
        else:
            print("Contact not found.")

    def update_contact(self, index, name, phone, email, address):
        if 0 < index <= len(self.contacts):
            contact = self.contacts[index - 1]
            contact.update({"name": name, "phone": phone, "email": email, "address": address})
            print("Contact updated successfully!")
        else:
            print("Invalid index.")

    def delete_contact(self, index):
        if 0 < index <= len(self.contacts):
            del self.contacts[index - 1]
            print("Contact deleted successfully!")
        else:
            print("Invalid index.")

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.contacts, file)

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                self.contacts = json.load(file)
            print("Contacts loaded successfully!")
        except FileNotFoundError:
            print("File not found.")

def display_menu():
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Save Contacts to File")
    print("7. Load Contacts from File")
    print("8. Exit")

def get_contact_details():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    return name, phone, email, address

def main():
    contact_book = ContactBook()

    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            name, phone, email, address = get_contact_details()
            contact_book.add_contact(name, phone, email, address)
        elif choice == '2':
            contact_book.view_contact_list()
        elif choice == '3':
            keyword = input("Enter name or phone number to search: ")
            contact_book.search_contact(keyword)
        elif choice == '4':
            index = int(input("Enter the index of the contact to update: "))
            name, phone, email, address = get_contact_details()
            contact_book.update_contact(index, name, phone, email, address)
        elif choice == '5':
            index = int(input("Enter the index of the contact to delete: "))
            contact_book.delete_contact(index)
        elif choice == '6':
            filename = input("Enter the filename to save contacts: ")
            contact_book.save_to_file(filename)
        elif choice == '7':
            filename = input("Enter the filename to load contacts: ")
            contact_book.load_from_file(filename)
        elif choice == '8':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()