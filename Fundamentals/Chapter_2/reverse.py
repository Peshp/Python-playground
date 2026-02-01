def reverse_string(sentence):
    reverrse = ""
    for i, val in enumerate(sentence.split()):
        reverrse += "".join(char for char in val[::-1])
    return reverrse

sentence = "Python is awesome"
print(reverse_string(sentence))

# Given a sentence, reverse each individual 
# word within the string while maintaining the original word order.


def reverse_string2(sentence):
    words = sentence.split()
    reverse = [word[::-1] for word in words]
    return " ".join(reverse)

print(reverse_string2("Python is awesome"))