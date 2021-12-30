class Category:
    def __init__(self, name):
        self.name = name
        self.balance = 0.0
        self.depositAmnt = 0.0
        self.withdrawAmnt = 0.0
        self.ledger = []

    def addLedger(self, amount, description):
        obj = {'amount': amount, 'description': description}
        return obj

    def check_funds(self, amount):
        if self.balance < amount:
            return False
        return True

    def deposit(self, amount, description=""):
        self.balance += amount
        self.depositAmnt += amount
        self.ledger.append(self.addLedger(amount, description))

    def withdraw(self, amount, description=""):
        if self.check_funds(amount) is False:
            return False
        self.withdrawAmnt += amount
        self.balance -= amount
        amount = -1 * amount
        self.ledger.append(self.addLedger(amount, description))
        return True

    def get_balance(self):
        return self.balance

    def transfer(self, amount, obj):
        if self.check_funds(amount) is False:
            return False
        self.withdraw(amount, "Transfer to {0}".format(obj.name))
        obj.deposit(amount, "Transfer from {0}".format(self.name))
        return True

    def __str__(self):
        info = ''
        info += self.name.center(30, '*') + '\n'
        for entry in self.ledger:
            #amnt = str(entry['amount'])
            #if amnt.find('.') == -1:
            #  amnt += '.00'
            #amnt = amnt.rjust(7)
            amnt = "{:.2f}".format(entry['amount']).rjust(7)
            desc = entry['description'][0:23].ljust(23)
            res = desc + amnt
            info += res + '\n'
        info += "Total: " + str(self.get_balance())
        return info


def create_spend_chart(categories):
    #Calculating values
    totalExpenses = sum(c.withdrawAmnt for c in categories)
    maxLength = max(len(c.name) for c in categories)
    colWidth = 12 + maxLength
    columns = [[]]
    chart = ""
    # First column for Indexes
    for i in range(colWidth):
        if i < 11:
            columns[0].append(str(10 * (10 - i)).rjust(3) + "| ")
        elif i == 11:
            columns[0].append('-'.rjust(5))
        else:
            columns[0].append(' '.rjust(5))

    # Columns for percentage bars
    for c in categories:
        newCol = []
        for i in range(11):
            if int(10 * (c.withdrawAmnt / totalExpenses)) >= 10 - i:
                newCol.append("o".ljust(3))
            else:
                newCol.append(" ".ljust(3))
        newCol.append("---")
        for i in range(maxLength):
            if len(c.name) > i:
                newCol.append(c.name[i] + "  ")
            else:
                newCol.append(" ".ljust(3))
        columns.append(newCol)

    # Fill out Chart
    chart += "Percentage spent by category"
    for i in range(colWidth):
        line = ""
        for c in columns:
            line += c[i]
        chart += '\n' + line

    return chart
