class BankAccount:
    def __init__(self,name,account_no,ifsc_code,balance=0):
        self.name=name 
        self.account_no=account_no
        self.ifsc_code=ifsc_code
        self.balance=balance
    
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            return f"Deposited ${amount}, NewBalance:${self.balance}"
        else:
            return "Invalid amount deposited"
        
    def withdrawl(self,amount):
        if 0<amount<self.balance:
            self.balance-=amount
            return f"Withdrwal ${amount}, NewBalnce: ${self.balance}"
        else:
            return "Insufficient funds or invalid withdraw amount"
    
    def balance_enquire(self):
        return f"Account holder: {self.name} \n Account No:{self.account_no} \n IFSC_code:{self.ifsc_code}\n Balance:${self.balance}"
    
bank=BankAccount("Kavitha","123456789","SBIN100",1000)
print(bank.balance_enquire())
print(bank.deposit(1000))
print(bank.withdrawl(500))