
print('Welcome to ziss bank. ')
pin = int(input('enter your four digit pin: '))
chances = 0
balance = 10000
sec_pin = 3678
cur_bal = 2000

if pin == sec_pin:
    print("""
        Please choose:
                    1. Services.
                    2. Balance enquiry.
                    3. Cash withdrawl.

        """)
    user = int(input('enter your choice: '))
    if user == 1:
        print(""" Please call our customer service centre to know about our legal services. 
                        """)
    elif user == 2:
        new_bal = balance - cur_bal
        print('Your balance is: ', cur_bal)
    elif user == 3:
        x = 'Available amounts are 100, 200, 500, 2000'
        print(x)
        user_amount = int(input('Enter the amount: '))
        if user_amount in [100, 200, 500, 2000]:
            print('please collect your cash ')

            print('Do you want the transaction recipt? yes/no')
            receipt = str(input('enter: '))
            if receipt.lower() == 'yes':
                    new_balance = balance - user_amount
                    print('Receipt: ')
                    print('last transaction: ', user_amount)
                    print('Your balance is:', new_balance)

        else:
                print('please enter the valid  available amounts : ', x)

else:
    print("wrong pin.")
    print("please remove your card.")

//SHASHANK



