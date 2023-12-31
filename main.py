import streamlit as st
from streamlit_extras.switch_page_button import switch_page


st.header("Olaa! 👋")
st.divider()
st.subheader("Welcome to Projects page.")
st.write("Here you can find all the projects you need to work on. Please select your project 🕸️")

with open('style.css') as f:
    st.markdown( f"<style>{f.read()}</style>", unsafe_allow_html = True)
st.divider()

st.write(
    """
1. To-Do List: Create a program that allows users to add, view, and delete tasks from a to-do list. Implement features like marking tasks as completed and saving the list to a file.

2. Word Frequency Counter: Develop a program that takes a text document as input and counts the frequency of each word. Display the most frequent words and their counts.

3. Alarm Clock: Create a program that functions as an alarm clock, allowing users to set alarms with custom sounds and snooze functionality.

4. Calculator with GUI: Extend the simple calculator project by adding a graphical user interface (GUI) using libraries like Tkinter or PyQT.

5. Password Manager: Create a program that securely stores and manages passwords for various accounts. Implement features like encryption, password generation, and master password authentication.

6. Hangman Game with Categories: Enhance the Hangman game by adding different word categories. Allow the player to choose a category before starting the game.

7. File Search Utility: Build a program that searches for files in a specified directory based on various criteria like file name, extension, or size.

8. Expense Splitter: Develop a program that helps roommates or friends split expenses and keep track of shared bills. Calculate each person's share and generate a report.

9. Recipe Manager: Create a program that allows users to manage and organize their recipes. Implement features like adding recipes, searching by ingredients, and generating shopping lists.

10. Personal Finance Manager: Develop a program that helps users track their income and expenses, categorize transactions, and generate financial reports like budgets or spending summaries.

11. Car Rental System: Develop a program that simulates a car rental service, allowing users to browse available cars, make reservations, and calculate rental fees based on duration and car type.

12. Appointment Scheduler: Create a program that allows users to schedule appointments or meetings, check availability, and send notifications or reminders.

13. Restaurant Menu Management: Develop a program that allows restaurant owners or managers to create and manage their menus, update item availability, and track orders.

14. Book Library Management: Build a program that helps users organize and manage their book collection. Include features like searching, sorting, and tracking borrowed books.

15. Quiz Game: Build a quiz game program that presents questions to the user and checks their answers. 

16. Personal Diary with Encryption: Build a program that allows users to write and encrypt their personal diary entries. Users can access their diary using a password and store their entries securely on their computer.

17. Restaurant Reservation System: Build a program that allows users to make reservations at a restaurant. Implement features like reservation management, table availability, and confirmation emails.

18. Password Strength Checker: Implement a program that assesses the strength of a password based on factors like length, complexity, and usage of different character types.

19. Currency Converter: Develop a program that converts between different currencies based on user input. Users can enter an amount in one currency, select a target currency, and the program will provide the converted amount.

20. Vehicle Management System: Build a program that helps users track and manage vehicle information, such as maintenance records, fuel consumption, and service reminders. Users can generate reports and track vehicle expenses.

21. Secret Santa Generator: Develop a program that randomly assigns Secret Santa gift exchange partners among a group of participants. Users can input participant names, and the program will generate the assignments.

22. Contact Book: Develop a program that allows users to store and manage their contacts locally on their computer. Implement features like adding contacts, searching, and sorting by name or category.

23. Digital Wallet: Create a program that simulates a digital wallet where users can store virtual money, make transactions, and check their balance locally on their computer.

24. File Renamer: Develop a program that helps users rename multiple files in a directory based on specified patterns or criteria. Users can choose to replace text, add prefixes or suffixes, or reformat file names.

25. Password Strength Evaluator: Develop a program that evaluates the strength of user-provided passwords and provides feedback on their complexity, such as length, character types, and common patterns.

26. Text-based Calendar: Create a program that displays a calendar in the command line interface. Users can add events, view the calendar by month or year, and receive reminders for upcoming events.

27. Hotel Reservation System: Develop a program that allows users to make hotel reservations locally. Users can check room availability, book rooms, and generate reservation confirmations.

28. Movie Ticket Booking System: Create a program that simulates a movie ticket booking system. Users can select movie screenings, choose seats, and generate printable tickets locally.

29. Online Shopping System: Build a program that simulates an online shopping system. Users can browse products, add items to their cart, and check out using a payment gateway.

30. Online Banking System: Develop a program that simulates an online banking system. Users can log in to their account, view their balance, and make transactions.

31. Online Food Ordering System: Create a program that simulates an online food ordering system. Users can browse restaurants, view menus, and place orders for delivery or pickup.

32. Online Course Registration System: Build a program that simulates an online course registration system. Users can browse courses, register for classes, and view their schedule.
   """)       


st.divider()
if st.columns(3)[1].button("Selected Project ?", key = 'get_project'):
    switch_page('get_project')