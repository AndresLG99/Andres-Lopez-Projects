# Asks user to input a text
# Asks user to input 3 letters
# Code should output how many times the 3 inputed letters appear in the text
# Code should output how many words are there in the text
# Code should output what's the first and last letter of the text
# Code should output the same text reversed (words)
# Code should output if the word "Python" appears in the text

text = input("Enter a text: ")
text_lowered = text.lower()

letter1 = input("Enter a letter: ").lower()
letter2 = input("Enter a second letter: ").lower()
letter3 = input("Enter a third letter: ").lower()

print("TASK 1")
letter1_count = text_lowered.count(letter1)
letter2_count = text_lowered.count(letter2)
letter3_count = text_lowered.count(letter3)
print(f"Letter '{letter1}' was found {letter1_count} time(s)")
print(f"Letter '{letter2}' was found {letter2_count} time(s)")
print(f"Letter '{letter3}' was found {letter3_count} time(s)")
print()
print("-" * 50)

print("TASK 2")
separated_text = text.split(" ")
print(f"The text has {len(separated_text)} words")
print()
print("-" * 50)

print("TASK 3")
print(f"The first letter in the text is {text[0]}")
print(f"The last letter in the text is {text[-1]}")
print()
print("-" * 50)

print("TASK 4")
separated_text.reverse()
print(" ".join(separated_text))
print()
print("-" * 50)

print("TASK 5")
word = "Python"
print(f"The word '{word}' appears in the text: {word.lower() in text_lowered}")
print()
print("-" * 50)