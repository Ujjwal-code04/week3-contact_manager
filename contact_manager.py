import json
import os
import csv
from datetime import datetime

FILE_NAME = "contacts_data.json"
contacts = {}
def load_contacts():
    global contacts
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            contacts = json.load(f)
    else:
        print(" No existing contacts file found. Starting fresh.")

def save_contacts():
    with open(FILE_NAME, "w") as f:
        json.dump(contacts, f, indent=4)
    print("Contacts saved to contacts_data.json")
def clean_phone(phone):
    return "".join(filter(str.isdigit, phone))

def valid_name(name):
    return len(name.strip()) > 0

def valid_phone(phone):
    return clean_phone(phone).isdigit() and len(clean_phone(phone)) >= 10

def add_contact():
    print("\n--- ADD NEW CONTACT ---")
    name = input("Enter contact name: ").title()

    if not valid_name(name):
        print(" Invalid name!")
        return

    phone = input("Enter phone number: ")
    if not valid_phone(phone):
        print(" Invalid phone number!")
        return
    phone = clean_phone(phone)

    email = input("Enter email (optional, press Enter to skip): ")
    address = input("Enter address (optional): ")
    group = input("Enter group (Friends/Work/Family/Other): ").title()

    contacts[name] = {
        "phone": phone,
        "email": email,
        "address": address,
        "group": group,
        "updated": str(datetime.now())
    }

    save_contacts()
    print(f" Contact '{name}' added successfully!")

def view_all():
    print(f"\n--- ALL CONTACTS ({len(contacts)} total) ---")
    print("=" * 60)

    for name, data in contacts.items():
        print(f"👤 {name}")
        print(f"   📞 {data['phone']}")
        print(f"   📧 {data['email']}")
        print(f"   👥 {data['group']}")
        print("-" * 40)

def search_contact():
    key = input("Enter name to search: ").lower()
    found = []

    for name, data in contacts.items():
        if key in name.lower():
            found.append((name, data))

    print(f"\nFound {len(found)} contact(s):")
    print("-" * 50)

    for i, (name, data) in enumerate(found, 1):
        print(f"{i}. {name}")
        print(f"   📞 Phone: {data['phone']}")
        print(f"   📧 Email: {data['email']}")
        print(f"   📍 Address: {data['address']}")
        print(f"   👥 Group: {data['group']}")

def statistics():
    print("\n--- CONTACT STATISTICS ---")
    print("Total Contacts:", len(contacts))

    groups = {}
    recent = 0

    for data in contacts.values():
        groups[data["group"]] = groups.get(data["group"], 0) + 1
        if (datetime.now() - datetime.fromisoformat(data["updated"])).days <= 7:
            recent += 1

    print("\nContacts by Group:")
    for g, c in groups.items():
        print(f"  {g}: {c} contact(s)")

    print("\nRecently Updated (last 7 days):", recent)

def delete_contact():
    name = input("Enter name to delete: ").title()
    if name in contacts:
        del contacts[name]
        save_contacts()
        print("✅ Contact deleted")
    else:
        print("❌ Contact not found")

def export_csv():
    with open("contacts.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Phone", "Email", "Address", "Group"])
        for name, data in contacts.items():
            writer.writerow([name, data["phone"], data["email"], data["address"], data["group"]])
    print("✅ Contacts exported to CSV")


def menu():
    while True:
        print("\n==============================")
        print("          MAIN MENU")
        print("==============================")
        print("1. Add New Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. View All Contacts")
        print("6. Export to CSV")
        print("7. View Statistics")
        print("8. Exit")
        print("==============================")

        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            view_all()
        elif choice == "6":
            export_csv()
        elif choice == "7":
            statistics()
        elif choice == "8":
            save_contacts()
            print("\nThank you for using Contact Management System!")
            break
        else:
            print("❌ Invalid choice")


print("=" * 50)
print("      CONTACT MANAGEMENT SYSTEM")
print("=" * 50)

load_contacts()
menu()
