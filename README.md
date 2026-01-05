Contact Management System

A simple, efficient, and user-friendly Contact Management System built using Python.
This project allows users to store, manage, search, and organize contacts with full CRUD operations and file persistence.

🚀 Features

Add new contacts with validation

Search contacts using partial name matching

Update existing contacts

Delete contacts with confirmation

View all contacts in formatted display

Save and load contacts automatically using JSON

Export contacts to CSV

Group contacts (Friends, Family, Work, Other)

View contact statistics

User-friendly menu system

Error handling and input validation

🛠️ Technologies Used

Python 3

Dictionaries

File Handling

JSON

CSV

Datetime module

📂 Project Structure
week3-contact-manager/
│
├── contacts_manager.py     # Main program
├── contacts_data.json      # Contact storage file (auto generated)
├── contacts.csv            # Exported contacts
└── README.md               # Project documentation

▶️ How to Run
Step 1 – Open terminal in project folder
cd week3-contact-manager

Step 2 – Run the program
python contacts_manager.py

📋 Menu Options
Option	Action
1	Add New Contact
2	Search Contact
3	Update Contact
4	Delete Contact
5	View All Contacts
6	Export to CSV
7	View Statistics
8	Exit
📦 Data Storage Format

Contacts are saved in contacts_data.json like this:

{
  "John Doe": {
    "phone": "12345678900",
    "email": "john@example.com",
    "address": "123 Main Street",
    "group": "Friends",
    "updated": "2025-01-05 10:25:33"
  }
}

📊 Statistics Module

The system shows:

Total number of contacts

Group-wise count (Friends, Work, Family, etc.)

Recently updated contacts (last 7 days)

📤 CSV Export

All contacts can be exported to contacts.csv which can be opened in Excel or Google Sheets.

🎯 Learning Outcomes

This project demonstrates:

Dictionary-based data storage

CRUD operations

Input validation

File handling (JSON & CSV)

Modular programming using functions

Menu-driven application design

👨‍💻 Developed By

ujjuu
Engineering Student
