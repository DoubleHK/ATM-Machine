# The registered pin numbers are stored under pinData
pinData = open("pin.txt", "r")
cardData = open("cardNumber100.txt", "r")
pin = pinData.readlines()
card = cardData.readlines()
pinList = [pin.rstrip('\n') for pin in open('pin.txt')]
cardList = [card.rstrip('\n') for card in open('cardNumber100.txt')]
atmData = ["Withdraw Cash", "Recharge Your Mobile", "Pay Income Tax", "Deposit Cash", "Transfer Cash"]
savingsAccount = 1000
currentAccount = 500
tries = 0
# Getting input from user for card and pin number
print("Welcome to the ATM")
# Using while to limit the number of incorrect card number entries
while tries < 3:
    cardNumber = input("Please enter your 16-digit card number:")
# Using if condition to check of the length of the card number is 16
    if len(cardNumber) == 16:
        if cardNumber in cardList:
            print("Card Number is correct")   # If card length is 16, then card number is correct
            while tries < 3:
                pinNumber = input("Please enter your 4-digit pin number:")
                if len(pinNumber) == 4:
                    if pinNumber in pinList:
                        print("Pin Number is correct")
                        print("\nList of Functions:" "\nPress 1 for Cash Withdraw",
                              "\nPress 2 for Recharge Your Mobile", "\nPress 3 for Balance Enquiry",
                              "\nPress 4 for Income Tax Payment", "\nPress 5 for Cash Deposit",
                              "\nPress 6 for Funds Transfer", "\nPress 7 to end")
                        # Getting input from user to perform the necessary functions
                        atmFunction = input("\nEnter the Function to proceed:")
                        # Based on the input, the following if conditional will be executed accordingly
                        if atmFunction == "1":
                            typeAccount = input("\nEnter Savings or Current Account:")
                            withdrawAmount = input("Enter the amount to withdraw:")
                            if typeAccount == "Savings" and int(withdrawAmount) < int(savingsAccount):
                                savingsAccount -= int(withdrawAmount)
                                print("Transaction Successful")
                                print("Available Balance:", savingsAccount)
                            elif typeAccount == "Current" and int(withdrawAmount) < int(currentAccount):
                                currentAccount -= int(withdrawAmount)
                                print("Transaction Successful")
                                print("Available Balance:", currentAccount)
                            else:
                                print("Insufficient Balance in Savings account")
                                transferAccount = input("Would you like to try current account (Yes or No):")
                                if transferAccount == "Yes":
                                    currentAccount -= int(withdrawAmount)
                                    print("Transaction Successful")
                                    print("Available Balance:", currentAccount)
                                    break
                                else:
                                    print("Thank you for banking with us")
                        elif atmFunction == "2":
                            mobileNumber = input("Enter your 10-digit mobile number:")
                            rechargeAmount = input("Enter the recharge amount:")
                            if len(mobileNumber) == 10:
                                print(mobileNumber)
                                confirm = input("Confirm if this is the correct mobile number (Yes or No):")
                                if confirm == "Yes":
                                    savingsAccount -= int(rechargeAmount)
                                    print("Recharge Successful", "\nAvailable Balance:", savingsAccount)
                                else:
                                    print("Enter correct mobile number")
                                    break
                            else:
                                print("Enter correct mobile number")
                        elif atmFunction == "3":
                            typeAccount = input("Which account balance is required (Savings or Current):")
                            if typeAccount == "Savings":
                                print(savingsAccount)
                                break
                            else:
                                print(currentAccount)
                        elif atmFunction == "7":
                            print("Thank you, Please visit again")
                            exit()
                        else:
                            print("\nPlease enter correct function name")
                    else:
                        print("You have entered an incorrect pin number, please try again")
                else:
                    print("The pin number you have entered is not 4-digit, please try again")
            # print("Too many entries, account has been locked, please contact nearest branch")
        else:
            print("You have entered an incorrect card number, please try again")
    else:
        print("The card number you have entered is not 16-digit, please try again")
print("\n\033[h;91mToo many attempts, your account has been locked, please contact your nearest branch\n")
exit()

