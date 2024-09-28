#enter the pin value
pin_dig = 5475
pin1 ='5475'
#initial balance value
balance = 1000
deposit = 100
enquiry = "Yes"
enquiry_no = "No"
saving = balance
current = saving
credit = 10000
try:
    print("Welcome to BHUVANESH  ATM")
    
    i = 1
    while i <= 3:
        pin =int(input("Enter your four digit pin number : "))
#=========Entering pin value:===============        
        if pin == pin_dig:
            print("Welcome BHUVANESH BANK  User Customer")
            print("Select options:")
            print("1: Withdrawal  2: Deposit  3:  Balance Enquiry  4: Pin Change  5: Exit")
            option =int(input("Choose your option to display : "))
#===============Enter option 1 withdrawal===============
            if option == 1:

                withdrawal = int(input("Enter your withdrawal amount :"))
                
                if withdrawal<=balance:
                    print("Withdrawal Successfully. Please collect your Money")
                    print("Do you want check balance : 6 : Yes  7 : No")
                    check =int(input("Selection of the checking :"))
                    if check ==6:
                        check = (balance - withdrawal)
                        print('The checking balance of account is ',check)  
                        break
                    elif check == 7:
                        print('Transction completed')
                        break
                else:
                    print("Insufficent amount!!!...")
                    break
            
               
#=========Enter option 2 deposit:============
            elif option == 2:

                deposit = int(input("Enter the deposit amount: "))
                
                if deposit >= 100:
                    new_deposit = (balance + deposit)
                    print("Deposit Successfully...")
                    print("Your Total Account ", new_deposit)
                    break
                else:
                    print("Deposit unsuccessful!!!... Try Again.!!!.. ")
                    break
            
#========Enter option 3 enquiry:================
            elif option == 3:

                print("Choose  Yes  or No ")
                enquiry =input("Enter the enquiry choose :")
                if enquiry == "Yes":
                     print("Selection Choose :")
                     print("8 : Saving  9 : Current 10 : Credit")
                     choose = int(input("Enter the enquiry choose :"))
                     if choose == 8:                        
                        print("Your Saving's account balance is",balance)
                        break                                       
                     if choose == 9:
                        print("Your Current's account balance is",saving)
                        break
                     if choose ==10:
                        print("Your Credit's account balance is",credit)
                        break
                if enquiry == "No":
                    print("Transcation cancelled")
                    break
                else:
                      print("Balance enquiry failed")
                      break

#=============Enter option 4 Pin change:========
            elif option ==4:
                pin_dig = int(input("Enter your old pin number :"))

                if pin == pin_dig:                       
                    new_pin = int(input("Enter your new pin number :"))
                    re_new_pin = int(input("Re-enter your new pin number: "))
                    if new_pin == re_new_pin:
                        pin1 = pin1.replace('new_pin','pin1')
                        print("Your new pin has been changed sucessfully...",new_pin)
                        break
                    else:
                        print("Pin doesn't match....Try again!!!")
                        break
                   
                else:
                    print("Your pin number is wrong!!!!")
                    break
#===========Enter option 5 Exit :============
            elif option == 5:
                print("Your card exited!!!")
                break

#=====================================================
        else:
            print("Sorry,Invalid pin number!!!...")
            break
        i =i+1
    else:
        print("Entered invalid pin more than three times.So,Your Card has been bloced!!!...")
        

except ValueError:
     print("Please enter in numbers only")
print("Thank You!!!...")
 
 
