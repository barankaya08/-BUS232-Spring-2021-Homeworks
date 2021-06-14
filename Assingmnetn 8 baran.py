import datetime
user = input("How may I assist you today? \nPress 1 to load an account.\nPress 2 to open a new account.\n")
if user==1:
    fhandler = open("LoadAccount", mode= 'r')
    fhandler.readlines()
    account_name = input("Enter the account name: ")
    user2 = int(input("Press 1 to deposit money to account.\nPress 2 to witdraw money from account"))
    if user2==1:

        amount=(input("How much do you want to deposit?"))
        print("The amount has been added in your account.")
        fhandler.write(amount)
        fhandler.close()

    elif user2==2:
        amount_withdraw=(input("How much do you want to withdraw?"))
        print("The amount has been withdawn from your account.")
        fhandler.write(amount_withdraw)
        fhandler.close()


else:
    new_account_name = input("Enter the new account name:")
    new_account_name += ".txt"
    fhandler = open(new_account_name,"w")
    lines = []
    lines.append("AccountName\tAccountNumber\tDate\tDescriptionOfTheEntry\tPostingReference\tDebit\tCredit\tDebitBalance\tCreditBalance\n")
    for x in range(3):
        print("Row"+str(x+1))
        AccountName = new_account_name[:-4]
        AccountNumber = "06123"
        Date = datetime.date.today()
        DescriptionOfTheEntry = input("Enter Description:")
        PostingReference = input("Enter Posting Reference:")
        Debit = input("Enter Debit:")
        Credit = input("Enter Credit:")
        DebitBalance = input("Enter Debit Balance:")
        CreditBalance = input("Enter Credit Balance:")
        lines.append(str(AccountName)+"\t"+str(AccountNumber)+"\t"+str(Date)+"\t"+str(DescriptionOfTheEntry)+"\t"+str(PostingReference)+"\t"+str(Debit)+"\t"+str(Credit)+"\t"+str(DebitBalance)+"\t"+str(CreditBalance)+"\n")
    fhandler.writelines(lines)
    print("New account is created successfully!")
    fhandler.close()
