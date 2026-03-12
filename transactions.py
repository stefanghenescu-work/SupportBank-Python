import csv

FILENAME = 'Transactions2014.csv'

class Transaction:
    def __init__(self, date, fromAccount, toAccount, narrative, amount):
        self.date = date
        self.fromAccount = fromAccount
        self.toAccount = toAccount
        self.narrative = narrative
        self.amount = float(amount)

class Account:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.transactions = []

    def addTransaction(self, transaction):
        self.transactions.append(transaction)

        if transaction.fromAccount == self.name:
            self.balance -= transaction.amount
        elif transaction.toAccount == self.name:
            self.balance += transaction.amount

def readCSV():
    with open(FILENAME, mode = 'r') as file:
        csvFile = csv.DictReader(file)
        return list(csvFile)
    
def listAll(accounts):
    for name, account in accounts.items():
        print(f"Account for {name} {'is owed' if account.balance > 0 else 'owes'} {abs(account.balance):.2f}")
        
def listAccount(accounts, name):
    if name not in accounts:
        print("Account not found!")
        return
    
    print("Transactions for " + name + "'s account")
    
    account = accounts[name]

    transactionIndex = 1
    for transaction in account.transactions:
        print(str(transactionIndex) + ": " + transaction.date + " " + transaction.narrative)
        transactionIndex = transactionIndex + 1



if __name__ == "__main__":
    accounts = {}
    
    # read data from csv
    transactionsFile = readCSV()

    # extract information from the data
    for row in transactionsFile:
        fromPerson = row['From']
        toPerson = row['To']
        
        # if not created, add new account
        if fromPerson not in accounts:
            accounts[fromPerson] = Account(fromPerson)
        
        if toPerson not in accounts:
            accounts[toPerson] = Account(toPerson)

        # Create transaction
        transaction = Transaction(
            date=row['Date'],
            fromAccount=row['From'],
            toAccount=row['To'],
            narrative=row['Narrative'],
            amount=row['Amount']
        )

        # Add transaction to the accounts
        accounts[fromPerson].addTransaction(transaction)
        accounts[toPerson].addTransaction(transaction)

    while True:
        command = input()
        if command == "List all":
            listAll(accounts)
        elif command.startswith("List "):
            accName = command[5:].strip()
            listAccount(accounts, accName)
        else:
            print("Unknown command.")

