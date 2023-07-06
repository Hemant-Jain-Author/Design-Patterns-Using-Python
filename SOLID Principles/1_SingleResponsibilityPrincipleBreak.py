""" DRY - Don't repeat yourself. 
Expect changes - Software always changes. 
Solid principle

Class should have only one reason to change.
"""

""" CRUD operations. - Create Read Update Delete  """ 

class Student:
	def __init__(self, name):
		self.name = name

	def get_name(self):
		return self.name

class BTechStudents(Student):
	def __init__(self, name):
		self.name = name	


class MTechStudents(Student):
	def __init__(self, name):
		self.name = name


class CoursesManager:
	def register_students(student, course):
		print("Register student to course.")
		pass

	def get_payment(sudent, course, payment):
		payment.make_payment()
		print("Payment received.")


class IPayment:
	def make_payment():
		pass

class CashPayment(IPayment):
	def make_payment():
		print("Make cash payment.")

	def count_cash():
		print("Counting cash.")

class CardPayment(IPayment):
	def make_payment():
		print("Make card payment")


class NetBankingPayment(IPayment):
	def make_payment():
		print("Make net-banking payment.")