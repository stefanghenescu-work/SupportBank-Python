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
        self.owe = 0
        self.othersOwed = 0
        self.transactions = []

    def addTransaction(self, transaction):
        self.transactions.append(transaction)

        accountName = self.name
        transactionValue = transaction.amount

        if transaction.fromAccount == accountName:
            self.owe = self.owe + transactionValue
        elif transaction.toAccount == accountName:
            self.othersOwed = self.othersOwed + transactionValue

def readCSV():
    with open(FILENAME, mode = 'r') as file:
        csvFile = csv.DictReader(file)
        return csvFile
    

if __name__ == "__main__":
    transactionsFile = readCSV()
    
