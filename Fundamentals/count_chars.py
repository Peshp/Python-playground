text = input()
letters = ''.join(text.split())
counts = {}

for letter in letters:
    if letter not in counts:
        counts[letter] = 0
    counts[letter] += 1

print(counts)