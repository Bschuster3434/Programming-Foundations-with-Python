def read_text():
	quotes = open(r"C:\Users\Schuster\Documents\Programming Foundations with Python\movie.txt")
	contents_of_file = quotes.read()
	print(contents_of_file)
	quotes.close()
read_text()