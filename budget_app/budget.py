class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0
        self.spent = 0

    def deposit(self, amount, description = ""):
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount

    def withdraw(self, amount, description = ""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": 
description})
            self.balance -= amount
            self.spent += amount
            return True
        else:
            return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + category.name)
            category.deposit(amount, "Transfer from " + self.name)
            return True
        else:
            return False

    def check_funds(self, amount):
        if amount > self.balance:
            return False
        else:
            return True

    def __str__(self):
        title = self.name.center(30, "*")
        items = ""
        for item in self.ledger:
            items += item["description"][:23].ljust(23) + "{:.2f}".format(item["amount"]).rjust(7) + "\n"
        total = "Total: {:.2f}".format(self.balance)
        return title + "\n" + items + total
    
def create_spend_chart(categories):
    title = "Percentage spent by category\n"
    names = []
    spent = []
    spent_percent = []
    for category in categories:
        names.append(category.name)
        spent.append(category.spent)
    total = sum(spent)
    for amount in spent:
        spent_percent.append(int(amount / total * 100))
    chart = ""
    for percent in range(100, -1, -10):
        chart += str(percent).rjust(3) + "| "
        for amount in spent_percent:
            if amount >= percent:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"
    chart += "    " + "-" * (len(names) * 3 + 1) + "\n"
    for i in range(len(max(names, key=len))):
        chart += "     "
        for name in names:
            if len(name) > i:
                chart += name[i] + "  "
            else:
                chart += "   "
        if i < len(max(names, key=len)) - 1:
            chart += "\n"
    return title + chart

