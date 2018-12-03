from bank import Bank
from tabulate import tabulate
print("Welcome")
acc_no = 400
while True:
	choice = int(input("Select \n1.Create account \n2.Deposit \n3.withdraw \n4.Statement"))

	if choice == 1:
		bal = int(input('Enter initial balance: '))
		acc_no += 1
		b = Bank(acc_no, bal)
		print(acc_no)

	elif choice == 2:
		acc_no = int(input("Enter the account number: "))
		amt = int(input("Enter the amount to be withdrawn: "))
		b.withdraw(amt, acc_no)  

	elif choice == 3:
		acc_no = int(input("Enter the account number: "))
		amt = int(input("Enter the amount to be deposited: "))
		b.deposit(amt, acc_no) 

	elif choice == 4:
		acc_no = int(input("Enter the account number: "))
		b.statement(acc_no)

	else:
		exit()	