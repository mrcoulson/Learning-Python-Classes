from person import Person
from another import Spock

# Get user input.
birthdate = input("Enter your birthdate (format: Nov 28 1978): ")
given_name = input("Enter your given name: ")
surname = input("Enter your surname: ")

# Handle blank input.
if not given_name:
	given_name = "<empty input>"
if not surname:
	surname = "<empty input>"

# Create a Person object with the input above.
p = Person(birthdate, given_name, surname)

# Print the result using the properties and methods from the Person class.
print("{} {} is about {} years old.".format(p.given_name, p.surname, p.calculate_age()))

# Print a Spock quote using the printQuote method from the Spock class.
s = Spock("Change is the essential process of all existence.")
print(s.print_quote())