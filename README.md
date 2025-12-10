COM5013 – Algorithms & Data Structures CW1 Project
Contacts Management System (Python)

This repository contains my implementation for the COM5013 Algorithms & Data Structures Coursework 1.
The project focuses on designing and evaluating suitable data structures and algorithms, followed by an implementation in Python with testing and version control.

Project Overview:

This application is a simple Contacts Management System that allows users to:

Add new contacts

Update existing contacts

Remove contacts

Search for contacts by email or name

List all contacts sorted alphabetically by name

The project demonstrates an understanding of:

Algorithmic performance using Big-O notation

Appropriate selection of data structures

Implementation in an object-oriented style


Testing using Python:

Use of GitHub for version control, documentation and project planning

For full documentation, see the Wiki pages.


Key Data Structures & Algorithms (Summary)

Contacts are stored using a Python dictionary (hash map), providing fast O(1) average-time lookup by email.

Searching by name uses a linear search over stored contacts.

Contacts are sorted alphabetically using Python’s built-in sort (Timsort, O(n log n)).

Additional algorithms (e.g., bubble sort) are included for comparison and analysis.

Detailed explanations are available in the Data Structures & Algorithms section of the Wiki.


How to Run the Program:

1. Clone the repository
git clone https://github.com/ibibhatti01/COM5013-Algorithms-Data-Structures-CW-1-Project---Muhammad-Ibrar.git
cd COM5013-Algorithms-Data-Structures-CW-1-Project---Muhammad-Ibrar

2. Run the tests
python tests.py

3. Run the application
python main.py


Then follow the on-screen menu to manage contacts.


Testing:

The tests.py script includes tests covering:

Adding, updating and deleting contacts

Searching by email and name

Error handling (e.g., duplicate emails, invalid removals)

Empty structure behaviour

Sorting and output correctness

More information is available on the Testing Strategy page in the Wiki.


Repository Structure:

contact.py          # Contact class
contact_book.py     # Core data structure for storing contacts
algorithms.py       # Search and sorting algorithms
main.py             # Command-line interface for the application
tests.py            # Basic test suite
.gitignore          # Git ignore rules


Documentation (GitHub Wiki)

The GitHub Wiki provides full documentation, including:

Project Overview

Data Structures & Algorithms

Testing Strategy

Access it here:
Wiki → https://github.com/ibibhatti01/COM5013-Algorithms-Data-Structures-CW-1-Project---Muhammad-Ibrar/wiki


Version Control & Issues:

This project uses:

Meaningful commit messages

GitHub Issues to track features, improvements and bugs

Wiki for documentation

This supports good software engineering practice and meets coursework requirements.


Author

Muhammad Ibrar
Student ID: 22539610
COM5013 – Algorithms & Data Structures


Final Notes:

This project demonstrates:

Understanding of data structures

Evaluation of algorithm performance

Appropriate design choices based on context

A fully functioning Python implementation

Testing and version control discipline
