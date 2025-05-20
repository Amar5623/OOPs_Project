# Python Contact Book

## Overview

This project is a console-based Contact Book application built using Object-Oriented Programming (OOP) principles in Python. It demonstrates how to move from writing basic functions to building a complete system made of interacting objects.

OOP allows us to design code that models real-world entities - each object has data (attributes) and behavior (methods).

## Core Classes

### Contact
- Represents a single person's contact details (name, phone number, email)
- Implements a `__str__` method to format contact information in a readable way

### ContactBook
- Manages a collection of Contact objects
- Provides methods to:
  - `add_contact()` - Add a new contact to the book
  - `view_contacts()` - Display all saved contacts
  - `search_contact()` - Find contacts by name
  - `delete_contact()` - Remove a contact by name


## How to Run

Save the code to a file named `contact_book.py` and run it using Python:

```bash
python contact_book.py
```
Follow the on-screen menu to interact with your contact book. You can add, view, search, and delete contacts through a simple numbered menu system.

## Example Usage

The application presents a menu-driven interface where users can:
1. Add new contacts with name, phone, and email information
2. View a list of all saved contacts
3. Search for specific contacts by name
4. Delete unwanted contacts
5. Exit the application

This project serves as a practical introduction to building software systems using object-oriented design principles.
