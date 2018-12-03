from tabulate import tabulate
class Bank:
	accounts = {}
	def __init__(self, acc_no, bal):
		self.name = input("Enter name: ")
		self.bal = bal
		#self.pin = int(input("enter a pin: "))
		self.acc_no = acc_no
		self.accounts[self.acc_no] = [[self.bal],[]]

	def withdraw(self, amt, acc_no):
		if acc_no not in self.accounts.keys():
			print("Account does not exist.")
		else:
			temp = self.bal - amt
			if temp < 500:
				print("Maintain minimum balance.")
			else:
				self.bal -= amt
				self.accounts[self.acc_no].append([[self.bal],["-"+f"{amt}"]])

	def deposit(self, amt, acc_no):
		if acc_no not in self.accounts.keys():
			print("Account does not exist.")
		else:
			self.bal += amt
			self.accounts[self.acc_no].append([[self.bal],["+"+f"{amt}"]])

	def statement(self, acc_no):
		if acc_no not in self.accounts.keys():
			print("Account does not exist.")
		else:
			print(self.accounts.values())				
							

