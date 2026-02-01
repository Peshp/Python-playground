import re

name = ["apple", "education", "ice", "ocean", "python", "umbrella"]

def filtering(name):
    pattern = r"^[aeiouAEIOU][a-zA-Z]{4}$"
    matched = []

    for element in name:
        m = re.match(pattern, element)
        if m:
            matched.append(element)

    return matched

print(filtering(name))

# Given a list of strings, use a single list comprehension to extract strings 
# that meet two criteria: they must be 5 characters AND they must start with a vowel (a, e, i, o, u).


def filtering2(anme):
    matched = []

    for element in name:
        if element[0] in "a o e i u" and len(element) == 5:
            matched.append(element)

    return matched

print(filtering2(name))
