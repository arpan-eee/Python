class Bank:
    def __init__(self,name) -> None:
        self.name = name
        self.users = {}
        self.__balance = 0
        self.__loan_status = True
        self.__loan_given = 0
        self.__is_bankrupt = False

    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
        else :
            print("Invalid Amount")

    def withdraw(self,amount):
        if amount > 0:
            self.__balance -= amount
        else :
            print("Invalid Amount")

    def loan_given(self,amount):
        self.__loan_given += amount
        self.__balance -= amount

    @property
    def balance(self):
        return self.__balance
    
    @property
    def loan_given_amount(self):
        return self.__loan_given
   
    @property
    def status(self):
        return self.__is_bankrupt
    
    @property
    def loan_status(self):
        return self.__loan_status
    
    def loan_status_update(self,status):
        self.__loan_status = status

    def add_user(self,user):
        user_number = f'{len(self.__users)+1}'
        self.__users[user_number] = user
        user.ac_number(user_number)

    def transfer(self,ac_1,ac_2,amount):
        if ac_1 <= len(self.__users) and ac_2 <= len(self.__users):
            if self.__users[ac_1].balance > amount :
                self.__users[ac_1].withdraw(amount)
                self.__users[ac_2].deposit(amount)
            else:
                print("Insufficient Balance")
        else :
            print("Account does not exist")


        
class User:
    def __init__(self,name,email,address,ac_type) -> None:
        self.name = name
        self.__email = email
        self.__address = address
        self.__ac_type = ac_type
        self.__loan = 0
        self.__own_balance = 0
        # self.__balance = self.__loan + self.__own_balance
        self.__ac_number = None
        self.__transaction = {}
        self.loan_count = 0

    def deposit(self,amount,bank):
        if amount<=0:
            print("Invalid Amount")
        else:
            self.__own_balance += amount
            bank.deposit(amount)

        t_no = f'{len(self.__transaction)+1}'
        self.__transaction[t_no] = amount

    def withdraw(self,amount,bank):
        if amount<0:
            print("Unavailable")
        elif amount > self.__balance:
            print("Withdrawal amount exceeded")
        elif amount > bank.balance and bank.status == False:
            print("The bank is bankrupt")
            print(type(bank.status))
        else:
            self.__balance -= amount
            bank.withdraw(amount)

        t_no = f'{len(self.__transaction)+1}'
        self.__transaction[t_no] = -amount

    @property
    def balance(self):
        return self.__loan + self.__own_balance
    
    @property
    def tn_history(self):
        return self.__transaction
    
    def take_loan(self,amount,bank):
        if self.loan_count < 2:
            if bank.balance >= amount and bank.status == False and bank.loan_status == True:
                self.__loan += amount
                bank.loan_given(amount)
                self.loan_count+=1
            else:
                print("The bank is bankrupt")
        else:
            print("Can't take loan more than twice")

    def ac_number(self,number):
        self.__ac_number = number



        
class Admin(User):
    def __init__(self, name, email, address, ac_type) -> None:
        super().__init__(name, email, address, ac_type)

    def delete_account(self,id,bank):
        del bank.users[id]
    
    def show_users(self,bank):
        for user in bank.users.values():
            print(user.name)

    def bank_balance(self,bank):
        print(bank.balance)

    def loan_amount(self,bank):
        print(bank.loan_given_amount)
    
    def loan_status_update(self,bank,status):
        bank.loan_status_update(status)

    

ab = Bank("AB")
arpan = User("Arpan", "a@g.com", "Ng", "savings")
ab.add_user(arpan)
arpan.deposit(1000,ab)
arpan.take_loan(800,ab)
arpan.take_loan(500,ab)

print(ab.balance)
print(arpan.balance)

