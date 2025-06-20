# Asks user to input a parragraph
# Asks user to input 3 letters
# Code should output how many times the 3 inputed letter appear in the parragraph
# Code should output how many words are there in the parragraph
# Code should output what's the first and last letter of the parragraph
# Code should output the same parragraph reversed
# Code should output if the word "Python" appears in the parragraph

text = "Hello World this is Andres' first portfolio using GitHub"

letter1 = "a"
letter2 = "b"
letter3 = "c"

letter1_count = text.lower.count(letter1)
letter2_count = text.lower.count(letter2)
letter3_count = text.lower.count(letter3)

print(letter1_count, letter2_count, letter3_count)