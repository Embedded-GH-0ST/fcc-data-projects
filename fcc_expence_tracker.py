def add_expense(expenses, amount, category):
    expenses.append({"amount": amount, "category": category})


def print_expenses(expenses):
    for expense in expenses:
        print(f"Amount: {expense['amount']}, Category: {expense['category']}")


def total_epenses(expenses):
    return sum(map(lambda expense: expense["amount"], expenses))


def filter_expenses_by_category(expenses, category):
    return lambda expense: expense["category"] == category, expen


expenses = []
