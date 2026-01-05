Contact Management System
Project Description
A comprehensive contact management system built with Python using dictionaries and functions. This system allows users to manage their contacts with full CRUD operations, search functionality, and data persistence.

What I Learned
Functions: Creating reusable, organized code blocks
Dictionaries: Storing and retrieving data using key-value pairs
String Methods: Advanced text manipulation and formatting
File Operations: Saving and loading data from JSON files
Input Validation: Ensuring data quality and preventing errors
Error Handling: Gracefully handling unexpected situations
Features
✓- Add new contacts with validation
✓- Search contacts by name (partial matching supported)
✓- Update existing contact information
✓- Delete contacts with confirmation
✓- View all contacts in formatted display
✓- Save contacts to JSON file automatically
✓- Load contacts from file on startup
✓- Export contacts to CSV format
✓- Contact statistics and analytics
✓- Phone number and email validation
✓- User-friendly menu interface
✓- Error handling for all operations
How to Run
bash Copy
# Navigate to project folder
cd week3-contact-manager

# Install any requirements
pip install -r requirements.txt  # (if needed)

# Run the program
python contacts_manager.py

# Run tests
python test_contacts.py
Data Structure
python Copy
contacts = {
    "John Doe": {
        "phone": "+1234567890",
        "email": "john@example.com",
        "address": "123 Main St",
        "group": "Friends"
    },
    "Jane Smith": {
        "phone": "+0987654321",
        "email": "jane@example.com",
        "address": "456 Oak Ave",
        "group": "Work"
    }
}
Sample Menu
Code Copy
==================================================
      CONTACT MANAGEMENT SYSTEM
==================================================
✅ No existing contacts file found. Starting fresh.

==============================
          MAIN MENU
==============================
1. Add New Contact
2. Search Contact
3. Update Contact
4. Delete Contact
5. View All Contacts
6. Export to CSV
7. View Statistics
8. Exit
==============================
Enter your choice (1-8): 1

--- ADD NEW CONTACT ---
Enter contact name: Ujjwal Kumar
Enter phone number: 7250446373
Enter email (optional, press Enter to skip): rajujjwal1804@gmail.com
Enter address (optional): Patna, Bihar
Enter group (Friends/Work/Family/Other): Family
✅ Contacts saved to contacts_data.json
✅ Contact 'Ujjwal Kumar' added successfully!

==============================
          MAIN MENU
==============================
1. Add New Contact
2. Search Contact
3. Update Contact
4. Delete Contact
5. View All Contacts
6. Export to CSV
7. View Statistics
8. Exit
==============================
Enter your choice (1-8): 5

--- ALL CONTACTS (1 total) ---
============================================================
👤 Ujjwal Kumar
   📞 7250446373
   📧 rajujjwal1804@gmail.com
   👥 Family
----------------------------------------

==============================
          MAIN MENU
==============================
1. Add New Contact
2. Search Contact
3. Update Contact
4. Delete Contact
5. View All Contacts
6. Export to CSV
7. View Statistics
8. Exit
==============================
Enter your choice (1-8): 1

--- ADD NEW CONTACT ---
Enter contact name: Shreya
Enter phone number: 9595465665
Enter email (optional, press Enter to skip): shreya@gmail.com
Enter address (optional): main street 
Enter group (Friends/Work/Family/Other): family
✅ Contacts saved to contacts_data.json
✅ Contact 'Shreya' added successfully!

==============================
          MAIN MENU
==============================
1. Add New Contact
2. Search Contact
3. Update Contact
4. Delete Contact
5. View All Contacts
6. Export to CSV
7. View Statistics
8. Exit
==============================
Enter your choice (1-8): 5

--- ALL CONTACTS (2 total) ---
============================================================
👤 Ujjwal Kumar
   📞 7250446373
   📧 rajujjwal1804@gmail.com
   👥 Family
----------------------------------------
👤 Shreya
   📞 9595465665
   📧 shreya@gmail.com
   👥 Family
----------------------------------------

==============================
          MAIN MENU
==============================
1. Add New Contact
2. Search Contact
3. Update Contact
4. Delete Contact
5. View All Contacts
6. Export to CSV
7. View Statistics
8. Exit
==============================
Enter your choice (1-8): 2
Enter name to search: shreya

Found 1 contact(s):
--------------------------------------------------
1. Shreya
   📞 Phone: 9595465665
   📧 Email: shreya@gmail.com
   📍 Address: main street
   👥 Group: Family

==============================
          MAIN MENU
==============================
1. Add New Contact
          MAIN MENU
==============================
1. Add New Contact
2. Search Contact
3. Update Contact
4. Delete Contact
5. View All Contacts
6. Export to CSV
7. View Statistics
8. Exit
==============================
Enter your choice (1-8):

Statistics:
- Total Contacts:2
- Friends: 0 contacts
- Work: 0 contacts
- Family: 2 contacts
- 
Challenges & Solutions
Challenge: Handling duplicate contact names

Solution: Added option to view all matches and select which to update

Challenge: Phone number validation across different formats

Solution: Created flexible validation function supporting multiple formats

Challenge: Efficient search with partial matching

Solution: Used dictionary comprehension with lower() for case-insensitive search

Challenge: Data persistence with JSON

Solution: Used json module with proper error handling for file operations

