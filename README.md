Contact Management System (Python)

A simple, efficient, and user-friendly Contact Management System built using Python.
This project allows users to store, manage, search, and organize contacts with full file persistence.

🚀 Project Features

Add, update, delete, and view contacts

Store contact details (Phone, Email, Address, Group)

Partial name search

Phone number cleaning & validation

Group-based classification (Friends, Family, Work, etc.)

Statistics dashboard

Export contacts to CSV

JSON file storage (data saved automatically)

Menu-driven interface

🛠️ Technologies Used

Python 3

JSON (for data storage)

CSV (for export feature)

File Handling

Dictionaries

Datetime module

📂 Project Structure
Contact-Management-System/
│
├── contacts_manager.py     # Main application
├── contacts_data.json      # Saved contacts (auto-created)
├── contacts.csv            # Exported contacts
└── README.md               # Project documentation

▶️ How to Run the Project

Install Python 3

Download or clone the repository

Open terminal in project folder

Run the file:

python contacts_manager.py

📋 Menu Options
Option	Function
1	Add New Contact
2	Search Contact
3	Update Contact
4	Delete Contact
5	View All Contacts
6	Export to CSV
7	View Statistics
8	Exit
📦 Data Storage

Contacts are stored in contacts_data.json in this format:

{
    "Ujjwal Kumar": {
        "phone": "7250446373",
        "email": "rajujjwal1804@gmail.com",
        "address": "Patna, Bihar",
        "group": "Family",
        "updated": "2026-01-05 13:15:53.200832"
    }
}

📊 Statistics Module

The system provides:

Total contacts

Group-wise contact count

Recently updated contacts (last 7 days)

📤 CSV Export

All contacts can be exported to contacts.csv which can be opened in Excel.

🎯 Learning Objectives

This project demonstrates:

Python dictionaries

CRUD operations

File handling

Data validation

Menu-driven programs

Real-world project structure

👨‍💻 Developed By

ujjuu
Engineering Student
