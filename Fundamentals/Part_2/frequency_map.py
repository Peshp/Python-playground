text = "Python Programming"

def get_count(t):
    letters = "".join(char for char in text if char.isalpha())
    letter_count = dict()

    for i in range(len(letters)):
        letter_count[letters[i].lower()] = letter_count.get(letters[i], 0) + 1
    return letter_count

print(get_count(text))

# Create a function that takes a string and returns a count of how many times each character appears. 
# Ignore spaces and make it case-insensitive.

from collections import Counter

def get_count2(t):
     cleaned = t.lower().replace(" ", "")
    
     return Counter(cleaned)

print(get_count2(text))