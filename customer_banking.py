# Import the create_cd_account and create_savings_account functions
from create_accounts.savings_account import create_savings_account
from create_accounts.cd_account import create_cd_account
from create_accounts.input_info import input_info

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance, savings_interest, savings_maturity = input_info('Savings')



    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, savings_interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print('\n\n')
    print("------------------------------------------")
    print("                  AI Bank                 ")
    print("------------------------------------------")
    print("Account type: --------------| Savings ")
    print(f"Original balance: ----------| {savings_balance} ")
    print(f"Interest rate: -------------| {savings_interest}%")
    print(f"Maturity period: -----------| {savings_maturity} ")
    print(f"Earned interest: -----------| {savings_interest_earned} ")
    print(f"Updated balance: -----------| {updated_savings_balance} ")
    print('\n\n')

# Prompt the user to set the CD balance,in interest rate, and months for the CD account.
    cd_balance, cd_interest, cd_maturity = input_info('CD')

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)


    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print('\n\n')
    print("------------------------------------------")
    print("                  AI Bank                 ")
    print("------------------------------------------")
    print("Account type: --------------| CD ")
    print(f"Original balance: ----------| {cd_balance} ")
    print(f"Interest rate: -------------| {cd_interest}%")
    print(f"Maturity period: -----------| {cd_maturity} ")
    print(f"Earned interest: -----------| {cd_interest_earned} ")
    print(f"Updated balance: -----------| {updated_cd_balance} ")
    print('\n\n')
    

if __name__ == "__main__":
    # Call the main function.
    main()