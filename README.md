# Expense Tracker CLI

## Overview
The Expense Tracker is a simple command-line application that allows users to manage their expenses effectively. Users can add, list, delete, and summarize their expenses, making it easy to keep track of their financial activities.

## Features
- **Add Expenses**: Record new expenses with descriptions and amounts.
- **List Expenses**: View all recorded expenses in a clear format.
- **Delete Expenses**: Remove expenses by their unique ID.
- **Summary**: Get a total of all expenses or filter by month.

## Requirements
- Python 3.x
- `argparse` (included in Python standard library)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/bamibopy237/expense_tracker_cli.git
   cd expense-tracker
## Usage
To use the Expense Tracker, run the main script from the command line. Here are the available commands:
1. Add an Expense - python expense_tracker.py add --description "Your Description" --amount 100.0
2. List all expenses - python expense_tracker.py list
3. Delete an expense - python expense_tracker.py delete --id 1
4. Get total expense - python expense_tracker.py summary
5. Get Total Expenses for a Specific Month - python expense_tracker.py summary --month 8

## Data Storage
Expenses are stored in a JSON file named expenses.json in the same directory as the script. This file will be created automatically upon adding the first expense.

## Contributing
Contributions are welcome! If you'd like to contribute, please fork the repository and submit a pull request.

