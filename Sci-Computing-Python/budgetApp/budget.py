
class Category:
    # List
    ledger = []
    
    # initializer (Contructor)
    def __init__(self, catergoryType):
        self.catergoryType = catergoryType



    def deposit(amount, desc=""):
        ledger.append({"amount":amount, "description":desc})



    def withdraw(amount, desc):

        if check_funds(amount):
            ledger.append({"amount":-amount, "description":desc})
            return True
        else:
            return False



    def get_balance():
        balance = 0
        for entry in ledger:
            balance += entry["amount"]
        return balance



    def transfer(amount, budgetType):
        remark = "Transfer to " + budgetType.categoryType
        response = self.withdraw(amount, desc)
        if response:
            remark = "Transfer from " + self.catergoryType
            budgetType.deposit(amount, desc)

        return response


    
    def check_funds(amount):
        totalBalance = self.get_balance()
        if totalBalance < amount:
            return False
        else:
            return True
        
    def printObj():
        
        



#def create_spend_chart(categories):
    
        