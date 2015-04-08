import urllib

def read_text():
	quotes = open(r"C:\Users\Schuster\Documents\Programming Foundations with Python\movie.txt")
	contents_of_file = quotes.read()
	print(contents_of_file)
	quotes.close()
	check_profanity(contents_of_file)
	
def check_profanity(text_to_check):	
	connection = urllib.urlopen("http://www.wdyl.com/profanity?q=" + text_to_check)
	output = connection.read()
	connection.close()
	if "true" in output:
	    print "Profanity in the text!"
	elif "false" in output:
		print "This document has no profanity"
	else:
		print "Error, could not make connection"
	
read_text()