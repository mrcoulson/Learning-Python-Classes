class Spock:
	
	def __init__(self, words):
		self.words = words

	def printQuote(self):
		quote = self.words
		# Reverse the quote just so we have a reason to have used this method.
		quote = quote + " " + quote[::-1]
		return quote