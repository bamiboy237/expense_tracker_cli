from datetime import datetime
import json
from pathlib import Path
import calendar
import argparse 

# Expense class that contains properties of each created expense
class Expense:
    def __init__(self, description, amount):
        self.description = description
        self.amount = float(amount)
        self.date = datetime.now().strftime("%Y-%m-%d")

# Expense tracker to handle updating, deleting and viewing of expenses 
class ExpenseTracker:
    def __init__(self, path):
        self.expenses = {}
        self.current_id = 1
        self.path = path
        self.load_expenses()

    def load_expenses(self):
        # Load expenses from the JSON file
        if self.path.exists():
            with open(self.path, 'r') as file:
                expenses_data = json.load(file)
                self.expenses = {int(k): v for k, v in expenses_data.items()}  # Convert keys back to int
                self.current_id = max(self.expenses.keys()) + 1 if self.expenses else 1  # Update current_id

    def save_expenses(self):
        # Save current expenses to the JSON file
        with open(self.path, 'w') as file:
            json.dump(self.expenses, file)

    def add_expense(self, description, amount):
        # Create a new expense and add it to the expense dictionary
        expense = Expense(description, amount)
        self.expenses[self.current_id] = {
            'Expense': expense.description,
            'Amount': expense.amount,
            'Date': expense.date  
        }
        self.current_id += 1  # Increment the current ID for the next task
        self.save_expenses()  # Save expenses after adding
        return f'Expense added successfully (ID: {self.current_id - 1})'

    def delete_expense(self, id):
        # Delete an expense by its ID if it exists
        if id in self.expenses:
            expense_description = self.expenses[id]['Expense']  # Store expense name for the return message
            del self.expenses[id]
            self.save_expenses()  # Save expenses after deletion
            return f"'{expense_description}' expense successfully deleted"
        else:
            return "I don't think you had such an expense."

    def update_expense(self, id, updated_description, amount=None):
        if id in self.expenses:
            if amount is not None:
                self.expenses[id]['Amount'] = amount
            self.expenses[id]['Expense'] = updated_description
            self.save_expenses()      
        else:
            return "Sorry, this expense does not exist."

    def list_expenses(self):
        # List all expenses
        print("ID  Date       Description  Amount")  # Output header
        # Iterate through the records and print them
        for id, details in self.expenses.items():
            print(f"{id}   {details['Date']}  {details['Expense']:10}  ${details['Amount']}")

    def expense_summary(self, month=None):
        total_expense = 0
        for expense in self.expenses.values():
            expense_date = datetime.strptime(expense['Date'], "%Y-%m-%d")
            if month is None or expense_date.month == month:
                total_expense += expense['Amount']
        if month:
            print(f"Your expenses for the month of {calendar.month_name[month]} total up to: ${total_expense}")
        else:
            print(f"Your expenses total up to: ${total_expense}")

# Initialize the path for the JSON file
path = Path('expenses.json')

# Initialize an instance of the ExpenseTracker class
expense_tracker = ExpenseTracker(path)

def main():
    parser = argparse.ArgumentParser(description='Expense Tracker')
    subparsers = parser.add_subparsers(dest='command')

    # Add command
    add_parser = subparsers.add_parser('add', help='Add an expense')
    add_parser.add_argument('--description', required=True, help='Description of the expense')
    add_parser.add_argument('--amount', type=float, required=True, help='Amount of the expense')

    # List command
    list_parser = subparsers.add_parser('list', help='List all expenses')

    # Summary command
    summary_parser = subparsers.add_parser('summary', help='Get total expenses')
    summary_parser.add_argument('--month', type=int, help='Month to summarize (1-12)')

    # Delete command
    delete_parser = subparsers.add_parser('delete', help='Delete an expense')
    delete_parser.add_argument('--id', type=int, required=True, help='ID of the expense to delete')

    args = parser.parse_args()

    if args.command == "add":
        print(expense_tracker.add_expense(args.description, args.amount))
    elif args.command == "list":
        expense_tracker.list_expenses()
    elif args.command == "delete":
        print(expense_tracker.delete_expense(args.id))
    elif args.command == "summary":
        expense_tracker.expense_summary(args.month)
    else:
        print("Invalid command.")

if __name__ == '__main__':
    main()
