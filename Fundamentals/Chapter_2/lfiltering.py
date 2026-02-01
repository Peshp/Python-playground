import re

name = ["apple", "education", "ice", "ocean", "python", "umbrella"]

pattern = r"^[aeiouAEIOU][a-zA-Z]{4}$"

# Iterate through the names to check the pattern
for element in name:
    m = re.match(pattern, element)
    if m:
        print(f"Matched word: {m.group()}")

