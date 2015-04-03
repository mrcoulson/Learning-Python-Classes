from datetime import datetime, date, timedelta
import sys

class Person(object):
	
	def __init__(self, birthdate, given_name, surname):
		self.birthdate = birthdate
		self.given_name = given_name
		self.surname = surname

	def calculate_age(self):
		if self.birthdate:
			try:
				d = datetime.strptime(self.birthdate, "%b %d %Y")
				age = (datetime.today() - d) // timedelta(days=365.2425)
			except:
				age = sys.exc_info()[0]
		else:
			age = "<empty input>"
		return age