# Anirudha Simha
# anirud3
# Caesar Cipher Shifter
# Enter one word at a time

shiftAmount = input('Enter an amount to shift by:\n')
text = input("Enter text to shift:\n")
output = ""
for letter in text.lower():
    if (ord(letter)+int(shiftAmount)) > ord('z'):
        output+=chr(ord(letter)+int(shiftAmount)-26)
    else:
        output+=chr(ord(letter)+int(shiftAmount))
print(output)