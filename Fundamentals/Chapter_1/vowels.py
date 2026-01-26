text = input()
chars = list(text)
vowels = ['a', 'o', 'u', 'e', 'i']

for letter in chars:
    for vowel in vowels:
        if letter == vowel:
            chars.remove(letter)

newWord = "".join(chars)
print(newWord)
