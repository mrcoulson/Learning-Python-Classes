from person import Person
from another import Spock

# Get user input.
strBirthdate = input("Enter your birthdate (format: Nov 28 1978): ")
strGivenName = input("Enter your given name: ")
strSurname = input("Enter your surname: ")

# Handle blank input.
if not strGivenName:
	strGivenName = "<empty input>"
if not strSurname:
	strSurname = "<empty input>"

# Create a Person object with the input above.
p = Person(strBirthdate, strGivenName, strSurname)

# Print the result using the properties and methods from the Person class.
print(p.givenName, p.surname, "is about", p.calculateAge(), "years old.")

# Print a Spock quote using the printQuote method from the Spock class.
s = Spock("Change is the essential process of all existence.")
print(s.printQuote())