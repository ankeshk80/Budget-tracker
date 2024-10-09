import json

class BudgetTracker:
    def __init__(self):
        self.balance = 0.0
        self.expenses = []
        self.income = []
        self.load_data()

    def load_data(self):
        try:
            with open('budget_data.json', 'r') as file:
                data = json.load(file)
                self.balance = data.get('balance', 0.0)
                self.expenses = data.get('expenses', [])
                self.income = data.get('income', [])
        except FileNotFoundError:
            self.save_data()  # Create file if it doesn't exist

    def save_data(self):
        data = {
            'balance': self.balance,
            'expenses': self.expenses,
            'income': self.income
        }
        with open('budget_data.json', 'w') as file:
            json.dump(data, file)

    def add_income(self, amount, description):
        self.income.append({'amount': amount, 'description': description})
        self.balance += amount
        self.save_data()

    def add_expense(self, amount, description):
        self.expenses.append({'amount': amount, 'description': description})
        self.balance -= amount
        self.save_data()

    def get_balance(self):
        return self.balance

    def view_income(self):
        return self.income

    def view_expenses(self):
        return self.expenses

def main():
    tracker = BudgetTracker()
    while True:
        print("\nBudget Tracker")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Balance")
        print("4. View Income")
        print("5. View Expenses")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            amount = float(input("Enter income amount: "))
            description = input("Enter income description: ")
            tracker.add_income(amount, description)
            print("Income added.")
        elif choice == '2':
            amount = float(input("Enter expense amount: "))
            description = input("Enter expense description: ")
            tracker.add_expense(amount, description)
            print("Expense added.")
        elif choice == '3':
            print(f"Current Balance: ${tracker.get_balance():.2f}")
        elif choice == '4':
            print("Income:")
            for item in tracker.view_income():
                print(f"{item['description']}: ${item['amount']:.2f}")
        elif choice == '5':
            print("Expenses:")
            for item in tracker.view_expenses():
                print(f"{item['description']}: ${item['amount']:.2f}")
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
