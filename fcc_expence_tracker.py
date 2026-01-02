# add expense
def add_expense(expenses, amount, category):
    expenses.append({"amount": amount, "category": category})


# print expenses
def print_expenses(expenses):
    for expense in expenses:
        print(f"Amount: {expense['amount']}, Category: {expense['category']}")


# total expenses
def total_epenses(expenses):
    return sum(map(lambda expense: expense["amount"], expenses))


# filter expenses by category
def filter_expenses_by_category(expenses, category):
    return lambda expense: expense["category"] == category, expen


expenses = []
