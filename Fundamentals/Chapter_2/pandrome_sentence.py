def palindrome(input):
    chars = "".join(char.lower() for char in input if char.isalnum())
    str = "".join(chars)
    return str == chars[::-1]

print(palindrome("A man, a plan, a canal: Panama"))

# Write a function to check if a full sentence is a palindrome. 
# You must ignore case, spaces, and all punctuation marks.

def is_palindrome_sentence(sentence):
    clean_chars = [char.lower() for char in sentence if char.isalnum()]
    clean_str = "".join(clean_chars)  
    return clean_str == clean_str[::-1]

print(is_palindrome_sentence("Madam, I’m Adam"))