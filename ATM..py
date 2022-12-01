pin_number=1234
acc_type='Savings'
total_amount=10000
for i in range(3):
    user_pin=int(input('Enter the pin number: '))
    if user_pin==pin_number:
        user_account=input('Enter the account type (Savings/Current): ')
        if user_account!=acc_type:
            print('Invalid account type: ')
            continue
        else:
            print('''
            select
            1.Withdrawal 
            2.Crediting
            3.Checking balance
            ''')
            option=int(input('Select the option given above: '))
            if option==1:
                amount=int(input('Enter the amount to be debited: '))
                if amount>total_amount:
                    print('Insufficient balance')
                    break
                else:
                    print(amount,'is debited from your account')
                    total_amount-=amount
                    print('Balance amount in account is ', total_amount)
                    break
            elif option==2:
                amount_credited=int(input('Enter the amount to be credited:'))
                total_amount+=amount_credited
                print("Total amount in your account is: ",total_amount)
                break
            else:
                print('Total balance :', total_amount)
                break

    else:
        print('Invalid pin number')
        continue
else:
    print('''
    Invalid details.
    Your account has been stopped.
    Please visit the bank
    ''')
