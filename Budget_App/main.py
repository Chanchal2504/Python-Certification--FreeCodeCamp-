class Category:
    def __init__(self,name):
        self.ledger=[]
        self.name=name

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self,amount,descr=""):
        if self.check_funds(amount):
            self.ledger.append({"amount":-amount,"description":descr})
            return True
        else:
            return False

    def get_balance(self):
        balance=0.0
        for entry in self.ledger:
            balance=balance+entry["amount"]
        return balance

    def transfer(self,amount,category):
        if self.check_funds(amount):
            if self.withdraw(amount, f"Transfer to {category.name}"):
                category.deposit(amount,f"Transfer from {self.name}")
                return True
            else:
                return False
        else:
            return False

    def check_funds(self,amount):
        if self.get_balance()>=amount:
            return True
        else:
            return False
    def __str__(self):
        output = f"{self.name:*^30}\n"
        for entry in self.ledger:
            description = entry["description"][:23].ljust(23)
            amount = f"{entry['amount']:.2f}".rjust(7)
            output += f"{description}{amount}\n"
        
        output += f"Total: {self.get_balance():.2f}"
        return output


def create_spend_chart(categories):
    Total=0
    withdraws=[]
    for item in categories:
        spent=0
        for ele in item.ledger:
            if ele["amount"]<0:
                spent=spent+abs(ele["amount"])
                Total=Total+abs(ele["amount"])
        withdraws.append(spent)
    
    for i in range(len(withdraws)):
        if withdraws[i]>0:
            withdraws[i]=(((withdraws[i]/Total)*100)//10)*10
        
            
    output="Percentage spent by category\n"
    for i in range(100,-1,-10):
        output+=f"{str(i).rjust(3)}| "
        for value in withdraws:
            if value>=i:
                output=output+"o  "
            else:
                output+="   "
        output+="\n"
    output+="    " + "-" * (3 * len(categories) + 1) + "\n"
    max_len = max(len(cat.name) for cat in categories)
    names = [cat.name.ljust(max_len) for cat in categories]
    
    for i in range(max_len):
        output += "     "
        for name in names:
            output += name[i] + "  "
        if i < max_len - 1:
            output += "\n"
    
    return output 

