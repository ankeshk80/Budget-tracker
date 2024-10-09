from flask import Flask, render_template, request, redirect, url_for
import json

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Placeholder balance, income, and expenses data
    balance = 5000
    income = 15000
    expenses = 10000

    return render_template('index.html', balance=balance, income=income, expenses=expenses)

if __name__ == '__main__':
    app.run(debug=True)

app = Flask(__name__)

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

tracker = BudgetTracker()

@app.route('/')
def index():
    return render_template('index.html', balance=tracker.get_balance(), income=tracker.view_income(), expenses=tracker.view_expenses())

@app.route('/add_income', methods=['POST'])
def add_income():
    amount = float(request.form['amount'])
    description = request.form['description']
    tracker.add_income(amount, description)
    return redirect(url_for('index'))

@app.route('/add_expense', methods=['POST'])
def add_expense():
    amount = float(request.form['amount'])
    description = request.form['description']
    tracker.add_expense(amount, description)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
