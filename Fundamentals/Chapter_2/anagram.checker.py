

def Is_anagram(word1, word2):
    x1 = sorted(word1.lower().replace(" ", ""))
    x2 = sorted(word2.lower().replace(" ", ""))

    return x1 == x2

print(Is_anagram("listen", "silent"))

# Write a function that determines if two strings are 
# anagrams (contain the exact same characters in a different order).
