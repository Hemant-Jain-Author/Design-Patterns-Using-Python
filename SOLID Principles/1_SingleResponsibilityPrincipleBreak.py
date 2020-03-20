""" DRY - Don't repeat yourself. 
Expect changes - Software always changes. 
Solid principle

Class should have only one reason to change.
"""

""" CRUD operations. - Create Read Update Delete  """ 

class Student:
	def __init__(self, name):
		self.name = name

	def getName(self):
		return self.name

class BTechStudents(Student):
	def __init__(self, name)
		self.name = name	


class MTechStudents(Student):
	def __init__(self, name)
		self.name = name


class CoursesManager:
	def registerStudents(student, course)
		print("Register student to course.")
		pass

	def getPayment(sudent, course, payment)
		payment.makePayment()
		print("Payment received.")


class IPayment:
	def makePayment():
		pass

class CashPayment(IPayment):
	def makePayment():
		print("Make cash payment.")

	def countCash():
		print("Counting cash.")

class CardPayment(IPayment):
	def makePayment():
		print("Make card payment")


class NetBankingPayment(IPayment):
	def makePayment():
		print("Make net-banking payment.")


