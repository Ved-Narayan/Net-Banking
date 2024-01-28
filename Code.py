import pickle
import os
import pathlib
class Account :
    accNo = 0
    name = ""
    password=""
    deposit=0
    type = ""
    def createAccount(self):
        self.accNo= int(input("Enter the account no : "))
        self.password=input("Create a password for your account: ")
        self.name = input("Enter the account holder name : ")
        self.type = input("Ente the type of account [C/S] : ")
        self.deposit = int(input("Enter The Initial amount(>=500 for Saving and >=1000 for current:"))
        print("\n\t Your Account has been Created Successfully\n")
def intro():
    print("\t\t\t\t**********************")
    print("\t\t\t\t      NET BANKING")
    print("\t\t\t\t**********************")
def writeAccount():
    account = Account()
    account.createAccount()
    writeAccountsFile(account)
def displaySp(num,pas):
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        infile.close()
        found = False
        for item in mylist :
            if item.accNo == num :
                 if item.password==pas:
                    print("\n\tYour account Balance is = ",item.deposit)
                    found = True
    else :
        print("\n\tNo records to Search\n")
    if not found :
        print("\n\tNo existing record with this number\n")
def depositAndWithdraw(num1,pas,num2):
    found=0
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in mylist :
            if item.accNo == num1 :
                found=1                
                if item.password==pas:
                    if num2 == 1 :
                        amount = int(input("\tEnter the amount to deposit : "))
                        item.deposit += amount
                        print("\n\tYour account is updted\n")
                    elif num2 == 2 :
                        amount = int(input("\tEnter the amount to withdraw : "))
                        if amount <= item.deposit :
                            item.deposit -=amount
                            print("\n\tYour amount has been withdrawed succesfully \n")
                        else :
                            print("\n\tInsufficient Funds in your Account\n")
                else:
                    print("\n\tInvalid Account Number or Password.\n")
        if found==0:
            print("\n\tNo Account found with the given Account Number!\n")
    else :
        print("\n\tNo records to Search\n")
    outfile = open('newaccounts.data','wb')
    pickle.dump(mylist, outfile)
    outfile.close()
    os.rename('newaccounts.data', 'accounts.data') 
def deleteAccount(num,pas):
    found=0
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        infile.close()
        newlist = []
        for item in oldlist :
            if item.accNo == num :
                 if item.password==pas:
                        found=1
        if(found==0):
            print("\tInvalid Account Number or Password.")
        else:
            for item in oldlist :
                if item.accNo != num :
                    newlist.append(item)
            print("\n\tAccount deleted successfully\n")
        os.remove('accounts.data')
        outfile = open('newaccounts.data','wb')
        pickle.dump(newlist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data') 
def modifyAccount(num,pas):
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in oldlist :
            if item.accNo == num :
                 if item.password==pas:
                    item.name = input("\tEnter the new account holder name : ")
                    item.type = input("\tEnter the new account Type : ")
                    item.deposit = int(input("\tEnter the Amount : "))     
        outfile = open('newaccounts.data','wb')
        pickle.dump(oldlist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')
        print("\n\tAccount details modified successfully\n\n")
def writeAccountsFile(account) : 
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open("accounts.data",'rb')
        oldlist = pickle.load(infile)
        oldlist.append(account)
        infile.close()
        os.remove('accounts.data')
    else :
        oldlist = [account]
    outfile = open('newaccounts.data','wb')
    pickle.dump(oldlist, outfile)
    outfile.close()
    os.rename('newaccounts.data', 'accounts.data')
def changepassword(num,pas):
    file=pathlib.Path("accounts.data")
    if file.exists():
        infile=open('accounts.data','rb')
        mylist=pickle.load(infile)
        infile.close()
        for item in mylist:
            if item.accNo==num:
                if item.password==pas:
                    item.password=input("\tEnter the new password: ")
                    print("\n\tPassword changed successfully :)\n")
                else:
                    print("\n\tIncorrect Account Number or Password!!\n")
        outfile=open('accounts.data','wb')
        pickle.dump(mylist,outfile)
        outfile.close()
ch=" "
num=0
pas=""
intro()
while 1:
    print("\tMAIN MENU")
    print("\t1. NEW ACCOUNT")
    print("\t2. DEPOSIT AMOUNT")
    print("\t3. WITHDRAW AMOUNT")
    print("\t4. BALANCE ENQUIRY")
    print("\t5. CLOSE AN ACCOUNT")
    print("\t6. MODIFY AN ACCOUNT")
    print("\t7. CHANGE PASSWORD")
    print("\t8. EXIT")
    ch = input("\tSelect Your Option (1-8) ")
    if ch == '1':
        print()
        writeAccount()
    elif ch =='2':
        num = int(input("\n\tEnter The account No. : "))
        pas=input("\tEnter the password : ")
        depositAndWithdraw(num,pas, 1)
    elif ch == '3':
        num = int(input("\n\tEnter The account No. : "))
        pas=input("\tEnter the password : ") 
        depositAndWithdraw(num,pas, 2)
    elif ch == '4':
        num = int(input("\n\tEnter The account No. : "))
        pas=input("\tEnter the password : ")
        displaySp(num,pas)
    elif ch == '5':
        num =int(input("\n\tEnter The account No. : "))
        pas=input("\tEnter the password : ")
        deleteAccount(num,pas)
    elif ch == '6':
        num = int(input("\n\tEnter The account No. : "))
        pas=input("\tEnter the password : ") 
        modifyAccount(num,pas)
    elif ch == '7':
        num=int(input("\n\tEnter The account No. : "))
        pas=input("\tEnter the current password : ")
        changepassword(num,pas)
    elif ch == '8':
        print("\n\tThanks for using Net Banking system")
        break
    else :
        print("Invalid choice")"
