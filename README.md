# Expense Tracker

Expense Tracker is a menu-based application designed to help you keep track of expenses among multiple participants. This interactive program allows you to add participants, record expenses, view participant details, show expenses, and export data to a CSV file.

## Menu Options

### 1. Add participant(s)

Enter one or more unique names of individuals who will participate in the transactions.

### 2. Add expense

Record expenses by providing the following details:
- **Paid by:** Name of the person who paid the money.
- **Amount:** The amount paid by the person.
- **Distributed amongst:** All the participants involved in this payment.
  - You can input the number of participants first and then enter the name of each person.
  - Alternatively, you can enter one string and tokenize it.

### 3. Show all participants

Display a list of all participants currently involved in the transactions.

### 4. Show expenses

Display a table showing each person's expenses with the following columns for each participant:
- Participant's Name
- Amount "Owes" or "Gets Back"

### 5. Exit/Export

Exit the application and write back the data to a CSV file named "expenses.csv". The arrangement of data in the CSV file is up to you.

## Usage

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/daken04/Expense-Tracker
    cd Expense-Tracker
    ```

2. Run the application:

    ```bash
    python expense_tracker.py
    ```

3. Follow the on-screen menu to interact with the Expense Tracker.

## Data Persistence

Data is automatically written to "expenses.csv" upon exiting the application. You can open this CSV file to view or analyze your expense data.

