from datetime import datetime, date, timedelta
import sys

class Person:
	
	def __init__(self, birthdate, givenName, surname):
		self.birthdate = birthdate
		self.givenName = givenName
		self.surname = surname

	def calculateAge(self):
		if self.birthdate:
			try:
				d = datetime.strptime(self.birthdate, "%b %d %Y")
				age = (datetime.today() - d) // timedelta(days=365.2425)
			except:
				age = sys.exc_info()[0]
		else:
			age = "<empty input>"
		return age