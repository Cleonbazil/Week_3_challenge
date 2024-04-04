def input_info(account_type):

    """Recieves the input for the savnings_account and the cd_account functions
    and verifies their validity.

    Args:
        balance (float): The initial account balance.
        interest (float): The APR interest rate for the account.
        maturity (int): The length of months to determine the amount of interest.
        count (int) : Tallies the number of opportinities the user has for incorrect input
    Returns:
        float: The verified inputs for the accounts balance, interest rate and maturity period.
    """


    # Vefying input that the input is a number greater than zero
    count = 1
    while count <= 3:
        try:
            balance = float(input(f"Please enter the {account_type} account's balance: "))
            if type(balance) is float and balance > 0:
                count = 4
            elif type(balance) is float and balance <= 0 and count == 1:
                print('Please enter a positive amount')
                count+=1
            elif type(balance) is float and balance <= 0 and count == 2: 
                print('Please enter a positive amount you have 1 more try')
                count+=1
            else:
                print('Please review your information and start over')
                exit()
    #Vefying input that the input is a number
        except ValueError:
            if count < 2 :
                print(f'Please enter a number you have {3-count} more tries')
                count+=1
            elif count == 2:
                print('Please enter a number you have 1 more try')
                count+=1
            else:
                print('Please review your information and start over')
                exit()

    
     #Vefying input that the input is a number greater than zero
    count = 1
    while count <= 3:
        try:        
            interest = float(input("Please enter the account's interest rate: "))
            if type(interest) is float and interest > 0:
                  count = 4
            
            elif type(interest) is float and interest <= 0 and count == 1:
                print('Please enter a positive amount')
                count+=1
            elif type(interest) is float and interest <= 0 and count == 2: 
                print('Please enter a positive amount you have 1 more try')
                count+=1
            else:
                print('Please review your information and start over')
                exit()    
    #Vefying input that the input is a number        
        except ValueError:
            if 3-count > 1:
                print(f'Please enter a number you have {3-count} more tries')
                count+=1
            elif count == 2:
                print('Please enter a number you have 1 more try')
                count+=1
            else:
                print('Please review your information and start over')
                exit

    #Vefying input that the input is a number greater than zero            
    count = 1    
    while count <=3:
        try:        
            maturity = float(input("Please enter the number of months to reach maturity: "))
            if type(maturity) is float and maturity > 0:
                count = 4
            elif type(maturity) is float and maturity <= 0 and count == 1:
                print('Please enter a positive amount')
                count+=1
            elif type(maturity) is float and maturity <= 0 and count == 2: 
                print('Please enter a positive amount you have 1 more try')
                count+=1
            else:
                print('Please review your information and start over')
                exit()
                
    #Vefying input that the input is a number  
        except ValueError:
            if 3-count > 1:
                print(f'Please enter a number you have {3-count} more tries')
                count+=1
            elif count == 2:
                print('Please enter a number you have 1 more try')
                count+=1
            else:
                print('Please review your information and start over')
                exit()
    
    return balance,interest,maturity
