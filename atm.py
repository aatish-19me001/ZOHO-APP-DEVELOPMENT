Username="ADMIN"
Password=1234
Balance=100000
username="giri"
password=1717
balance=10000
usernamee="boo"
passwordd=9876
def _admin(Balance):
    while True:
        print("1=see balance")
        print("2=load money")
        d=int(input("Enter your choice :"))
        if(d==1):
            print(Balance)
            return _admin(Balance)
        elif(d==2):
            e=int(input("Enter the no. of 2000 :"))
            f=int(input("Enter the no. of 500 :"))
            g=int(input("Enter the no. of 200 :"))
            h=int(input("Enter the no. of 100 :"))
            i=((e*2000)+(f*500)+(g*200)+(h*100))
            print("amount added successfully")
            print("amount added =",i)
            Balance+=i
        else:
            print("EXIT")
            return atm(Balance)

def admin(Balance):
    while True:
        b=input("Enter the username :")
        c=int(input("Enter the password :"))
        if((b==Username) and (c==Password)):
            print("Welcome back Admin")
            _admin(Balance)
        else:
            print("username or password incorrect")

def withdrawal(balance):
    while True:
        k=int(input("Enter the withdrawal amount :"))
        if (k<=Balance):
            if (k<=balance):
                if (k%100==0):
                    print("Your cash",k,"is ready,kindly collect it")
                    balance=balance-k
                    print("your current balance is",balance)
                    print("Thank you for coming")
                    return _user(balance)
                else:
                    print("Enter valid amount")
                    return _user(balance)
            else:
                print("Sorry")
                print("Low balance")
                return _user(balance)
        else:
            print("Sorry")
            print("Not enough cash,contact the admin")
            return _user(balance)

def transfer(balance):
    while True:
        b2=input("Enter the username :")
        c2=int(input("Enter the password :"))
        if((b2==usernamee) and (c2==passwordd)):
            print("you are transferring money to",usernamee+"'s account")
            n=int(input("Enter the amount to be transferred :"))
            if (n<=balance):
                print("Your cash",n,"is transferred successfully")
                balance=balance-n
                print("your current balance is",balance)
                print("Thank you for coming")
                return _user(balance)
            else:
                print("Sorry")
                print("Low balance")
                return _user(balance)

def change(passworrd):
    while True:
        passworrd=1717
        l=int(input("Enter your current password :"))
        if (l == passworrd):
            l1=int(input("Enter new password :"))
            l2=int(input("Re-enter your new password :"))
            if (l1==l2):
                password=l1
                print("Password change successful")
                print("your current password is",password)
                print("please don't forget your password")
                print("Thank you")
                passworrd=password
                break
            elif (l==l1):
                print("your password is older")
                print("Kindly enter a different password")
                return _user(balance)
            else:
                print("Your passwords aren't same")
                return _user(balance)
        else:
            print("Your password is incorrect")
            print("Kindly contact the admin")
            return _user(balance)

def _user(balance):
    while True:
        print("1=Withdrawal")
        print("2=Check balance")
        print("3=Change password")
        print("4=Transfer money")
        j=int(input("Enter your choice :"))
        if(j==1):
            print("Withdrawal")
            withdrawal(balance)
        elif(j==2):
            print("Checking your balance")
            print("Your current balance is",balance)
            return _user(balance)
        elif(j==3):
            print("Change password")
            change(password)                       
        elif(j==4):
            print("Transfer money")
            transfer(balance)
        else:
            print("EXIT")
            return atm(Balance)

def user(balance):
    while True:
        b1=input("Enter the username :")
        c1=int(input("Enter the password :"))
        if((b1==username) and (c1==password)):
            print("Welcome back",username)
            _user(balance)     
        else:
            print("username or password incorrect")

            
def atm(Balance):
    while True:
        print("ATM")
        print("1=ADMIN")
        print("2=USER")
        a=int(input("Enter your choice :"))
        if(a==1):
            print("ADMIN")
            admin(Balance)
        elif(a==2):
            print("USER")
            user(balance)
        else:
            print("EXIT")
            break
atm(Balance)
