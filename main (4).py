implementaion a class called bank account that represents a bank account.the class should have private. 
attributes for account number.account holder name and accounts balance.include methods to. 
deposit money, withdraw money,and display the account balance ensure that the account balance . 
cannot be accessed directly from outside the class. write a program to create an instnce of the. 
bank account class abd deposit and withdrawal functionality. 


class bank account; 

def__init__(self, account _number, account _holder_name, initial _balance=0.0); 
self_account_ holder_name=account _holder_name 
self__account_balance=initial_balance 
def_deposit(self,amount): 
if amount>0: 
  self__account_balance+=amount 
print("deposit £{}. new balance:£{}, format(amount,self_account_balance") 
else: 
print("invalid deposit amount,please deposit a positive amount.") 
def withdraw (self,amount): 
  if amount>0and amount<=self.__amount_balance: 
    self.__account_balance_=amount
print("withdraw £{}.new balance:£{}". format (amount,self.__account_balance)) 
else: 
print (invalid withdraw (amount or insufficient balance.")) 
def display_balance(self)): 
   print("account balance for{}(account#{}):£{}".format) 
self.__account_holder_name,self__account_number, 
self.__ account _balance