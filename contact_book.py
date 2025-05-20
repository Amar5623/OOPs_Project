class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
    
    def __str__(self):
        return f"Name: {self.name}\nPhone: {self.phone}\nEmail: {self.email}"


class ContactBook:
    def __init__(self):
        self.contacts = []
    
    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"Contact {contact.name} added successfully!")
    
    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
            return
        
        print("\n===== CONTACTS =====")
        for i, contact in enumerate(self.contacts, 1):
            print(f"\nContact #{i}")
            print(contact)
            print("-------------------")
    
    def search_contact(self, name):
        found_contacts = []
        for contact in self.contacts:
            if name.lower() in contact.name.lower():
                found_contacts.append(contact)
        
        if not found_contacts:
            print(f"No contacts found with name '{name}'")
            return
        
        print(f"\nFound {len(found_contacts)} contact(s):")
        for i, contact in enumerate(found_contacts, 1):
            print(f"\nResult #{i}")
            print(contact)
            print("-------------------")
    
    def delete_contact(self, name):
        for i, contact in enumerate(self.contacts):
            if contact.name.lower() == name.lower():
                deleted_contact = self.contacts.pop(i)
                print(f"Contact '{deleted_contact.name}' deleted successfully!")
                return
        
        print(f"No contact found with name '{name}'")


def main():
    book = ContactBook()
    
    while True:
        print("\n===== CONTACT BOOK =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        
        choice = input("\nChoose an option (1-5): ")
        
        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            contact = Contact(name, phone, email)
            book.add_contact(contact)
        
        elif choice == "2":
            book.view_contacts()
        
        elif choice == "3":
            name = input("Enter name to search: ")
            book.search_contact(name)
        
        elif choice == "4":
            name = input("Enter name to delete: ")
            book.delete_contact(name)
        
        elif choice == "5":
            print("Thank you for using Contact Book. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()