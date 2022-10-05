
import math

class Category:
    # List
    ledger = []
    
    # initializer (Contructor)
    def __init__(self, cType):
        self.Category = cType



    def deposit(self, amount, desc=""):
        self.ledger.append({"amount":amount, "description":desc})



    def withdraw(self, amount, desc=''):
        if self.check_funds(amount):
            self.ledger.append({"amount":-amount, "description":desc})
            return True
        else:
            return False



    def get_balance(self):
        balance = 0
        for entry in self.ledger:
            balance += entry["amount"]
        return balance



    def transfer(self, amount, budget):
        remark = "Transfer to " + budget.Category
        response = self.withdraw(amount, remark)
        if response:
            remark = "Transfer from " + self.Category
            budget.deposit(amount, remark)

        return response


    
    def check_funds(self, amount):
        totalBalance = self.get_balance()
        if totalBalance < amount:
            return False
        else:
            return True
        


    def __str__(self):
        formatSize = math.ceil((30 - len(self.Category))/2)

        # get maximum length of amount digits
        digitMaxLen = 0
        for entry in self.ledger:
            if len(str(entry["amount"])) > digitMaxLen:
                digitMaxLen = len('{:.2f}'.format(entry["amount"]))

        print("*"*formatSize + self.Category + "*"*formatSize)

        for entry in self.ledger:
            print(f"{entry['description'][0:23] :<23} {'{:.2f}'.format(entry['amount']) :>{digitMaxLen}}")

        totalBalance = self.get_balance()
        return (f"{'Total:':<7}{'{:.2f}'.format(totalBalance)}")



#def create_spend_chart(categories):
    
