import random
import mysql.connector
con= mysql.connector.connect(
    host= 'localhost',
    username= 'root',
    password= 'password',
    port=3306
)
mycursor= con.cursor()
mycursor.execute("Create DATABASE if not exists Bank_management")
mycursor.execute("use Bank_management")
mycursor.execute("create table if not exists account_info(acc_no int, name varchar(30), amount float)")

def options():
    print("Welcome to Chandigarh Branch")
    print("1, Create account")
    print("2, Deposit money")
    print("3, Withdraw money")
    print("4, Delete account")
    print("5, View Account info")
    print("6, Exit")

def again():
    print("\nDo you want to continue")
    z=int(input("enter 1 for main and 2 for exit"))
    if(z==1):
        options()
        repeat()
    else:
        print("Thankyou for using Chandigarh Branch")

def create_account():
    name=input("Enter your name:")
    acc_no=random.randint(1000,9999)
    amount=float(input("Enter initial deposit amount (Min Rs500): "))
    if amount>=500:
        query=f"INSERT INTO account_info(name,acc_no,amount) VALUES(%s,%s,%s)"
        values=(name,acc_no,amount)
        mycursor.execute(query,values)
        con.commit()
        print("Account created successfully")
        print("Your account number is",{acc_no})
    else:
        print("Minimum deposit should be Rs500.")
    for row in mycursor.fetchall():
        print(f"Name: {row[1]}, Account No: {row[0]}, Balance: Rs{row[2]}")
    again()

def deposit():
    acc_no=int(input("Enter your account number: "))
    amount=float(input("Enter amount to deposit: "))
    mycursor.execute("UPDATE account_info SET amount = amount + %s WHERE acc_no = %s", (amount, acc_no))
    con.commit()
    print("Amount credited successfully")
    again()
    

def withdraw():
    acc_no=int(input("Enter your account number: "))
    amount=float(input("Enter withdrawl amount (Min:Rs200): "))
    if amount>=200:
        mycursor.execute("UPDATE account_info SET amount=amount-%s WHERE acc_no=%s",(amount,acc_no))
        con.commit()
        print("withdrawl successfull")
    else:
        print("Insufficient balance or minimum withdrawl is Rs200")
    again()
        

def delete_account():
    acc_no=int(input("Enter your account number: "))
    mycursor.execute("DELETE from account_info WHERE acc_no=%s",(acc_no,))
    con.commit()
    print("Account deleted successfully")
    again()
    
def display_account():
    acc_no=int(input("Enter your account number: "))
    mycursor.execute("SELECT * from account_info WHERE acc_no=%s",(acc_no,))
    record=mycursor.fetchone()
    if record:
        print(f"Name: {record[1]}, Account No: {record[0]}, Balance: Rs{record[2]}")
        
    else:
        print("No account found") 
    again()

def repeat():  
    print("Do you want to perform my other operations: ")
    choice=int(input("Enter your choice: "))
    if choice==1:
        print("Account already created!")
    elif choice==2:
        deposit()
    elif choice==3:
        withdraw()
    elif choice==4:
        delete_account()
    elif choice==5:
        display_account()
    elif choice==6:
        print("Thankyou for using Chandigarh Bank!")
    else:
        print("Invalid choice. Please try again")
        again()

print("Welcome to Chandigarh Bank")
print("Are you an existing user? or a new user?")
print("Press 1 for existing user")
print("Press 2 for new user")
a=int(input("ENTER Number"))
if a==1:
    print("What do you want to do?")
    options()
    repeat()
elif a==2:
    create_account()
else:
        print("Invalid choice. Please try again")