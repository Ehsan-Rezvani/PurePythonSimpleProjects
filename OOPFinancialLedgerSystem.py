class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for item in self.ledger:
            desc = item["description"][:23].ljust(23)
            amt = f"{item['amount']:>7.2f}"
            items += f"{desc}{amt}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total

def create_spend_chart(categories):
    spendings = []
    for cat in categories:
        spent = sum(item["amount"] for item in cat.ledger if item["amount"] < 0)
        spendings.append(abs(spent))
    
    total_spent = sum(spendings)
    percentages = [(s / total_spent * 100) // 10 * 10 for s in spendings]

    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        chart += f"{str(i).rjust(3)}| "
        for p in percentages:
            chart += "o  " if p >= i else "   "
        chart += "\n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    max_len = max(len(cat.name) for cat in categories)
    names = [cat.name.ljust(max_len) for cat in categories]
    
    for i in range(max_len):
        chart += "     "
        for name in names:
            chart += name[i] + "  "
        if i < max_len - 1:
            chart += "\n"

    return chart
