# Anirudha Simha
# Caesar Cipher Shifter
# Enter one word at a time
import sys

def shift():
	shiftAmount = input('Enter an amount to shift by (shift amount must be between 0 and 25):\n')

	text = input("Enter text to shift:\n")
	output = ""
	for letter in text.lower():
		if (ord(letter)+int(shiftAmount)) > ord('z'):
			output+=chr(ord(letter)+int(shiftAmount)-26)
		else:
			output+=chr(ord(letter)+int(shiftAmount))
	print(output)
	runAgain = input("Run again? y or n\n")
	while runAgain != "y" and runAgain != "n":
		runAgain = input("Run again? y or n\n")
	return runAgain

done = False
while not done:
	rerun = shift()
	
	if rerun == "y":
		shift()
	else:
		done = True
sys.exit()