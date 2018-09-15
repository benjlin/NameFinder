import re

wordsToIgnore = ["Some", "It", "This", "There"]

mainLoopActive = True;

while mainLoopActive:
	menu = "0 to exit, raw text to anylise"
	userInput = input(menu)
	
	if(userInput == "0"):
		mainLoopActive = False
	else:
		pattern = re.compile('([A-Z][a-z]+)')
		capitalWords = re.findall(pattern, userInput)
		
		for word in wordsToIgnore:
			for capitalWord in capitalWords:
				if(capitalWord.lower() == word.lower()):
					capitalWords.remove(capitalWord)
		
		print()
		print("Found words are:")
		print(capitalWords)
	print()
print("exited")
