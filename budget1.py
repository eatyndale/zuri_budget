class Budget:
    
    def __init__ (self):
        pass
    def Add (self):        
        total_budget = int (input ('Please enter deposit amount: \n'))
        print ('Your balance is being updated')
        category_balance['total_balance'] += total_budget
        print ('Your balance has been successfully updated')
        print ("Your new balance is", category_balance['total_balance'])
    def Deposit (self, category):    
        while True:
            category = input ('Please enter Category\n')
            deposit_amount = int (input (f'Please enter amount to add to {category} Budget: \n'))
            if deposit_amount <= category_balance ['total_balance']:
                category_balance[category] = deposit_amount
                print (f'Depositing {deposit_amount} in {category} Budget')
                category_balance['total_balance'] -= deposit_amount
                print('Deposit successful')
                print ("Remaining balance is", category_balance['total_balance'])
                break 
            else:
                print('Deposit amount is higher than Total Balance. Please deposit a lower amount')
                continue
    def Withdraw (self, category):
        while True:
            withdrawal_category = input ('Please enter category you want to withdraw from: \n')
            withdrawal_amount = int (input (f'Please enter amount to withdraw from {withdrawal_category} Budget: \n'))
            break
        if withdrawal_amount <= category_balance['total_balance']:
            category_balance[category] = withdrawal_amount
            print (f'You are withdrawing {withdrawal_amount} from {withdrawal_category} Budget')
            category_balance['total_balance'] += withdrawal_amount
            print ('Withdrawal successful')
            print ("Remaining balance is", category_balance['total_balance'])
        else:
            print ('Withdrawal amount is higher than Total Balance. Please withdraw a lower amount')
    def Balance (self, category):
        check_category = input ('Please select category')
        print(f" Your {category}'s balance is {category_balance[category]}")
    def Transfer (self, category):
        while True:
            try:
                transfer_from = input ('What category are you transfering from?\n')
                transfer_to = input ('What category are you transferring to?\n')
                break
                if transfer_from in category and transfer_to in category:
                    transfer_amount = int(input ('Please enter transfer amount\n'))
                    category_balance[transfer_to] += transfer_amount
                    print ('Your Budget Balance is being Updated')
                    print (f"Your {transfer_to}'s balance is now {category_balance[transfer_to]}")
                    category_balance[transfer_from] -= transfer_amount
                    print (f"Your {transfer_from.title()}'s balance is now {category_balance[transfer_from.title()]}")
                else:
                    print ("Category not found. Please enter valid category")
            except:
                continue
category = ['Food', 'Utility', 'Entertainment']
options = ['Add', 'Deposit', 'Withdraw', 'Balance,' 'Transfer']
category_balance =  {'total_balance' : 5000, 'Food' : 2000, 'Utility' : 2000, 'Entertainment' : 1000}
category = Budget()
category.Add()
category.Deposit('Food')
category.Withdraw('Food')
category.Balance('Food')
category.Transfer('Food')