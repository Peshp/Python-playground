import re

name = ["apple", "education", "ice", "ocean", "python", "umbrella"]
matched = []

pattern = r"^[aeiouAEIOU][a-zA-Z]{4}$"

for element in name:
    m = re.match(pattern, element)
    if m:
        matched.append(element)

print(matched)

# Given a list of strings, use a single list comprehension to extract strings 
# that meet two criteria: they must be 5 characters AND they must start with a vowel (a, e, i, o, u).

