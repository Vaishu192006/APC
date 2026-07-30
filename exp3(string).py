# Program 1: Find length of string without using len()
s = input("Enter a string: ")
count = 0
for ch in s:
    count += 1
print("Length of string:", count)

# Program 2: Count vowels, consonants, digits, spaces, and special characters
s = input("Enter a string: ")
vowels = consonants = digits = spaces = special = 0
for ch in s:
    if ch.lower() in "aeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch.isdigit():
        digits += 1
    elif ch.isspace():
        spaces += 1
    else:
        special += 1
print("Vowels:", vowels, "Consonants:", consonants, "Digits:", digits, "Spaces:", spaces, "Special:", special)

# Program 3: Reverse a string without using built-in reverse
s = input("Enter a string: ")
rev = ""
for ch in s:
    rev = ch + rev
print("Reversed string:", rev)

# Program 4: Check if string is palindrome
s = input("Enter a string: ")
rev = ""
for ch in s:
    rev = ch + rev
if s == rev:
    print("Palindrome")
else:
    print("Not a palindrome")

# Program 5: Count uppercase and lowercase letters
s = input("Enter a string: ")
upper = lower = 0
for ch in s:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
print("Uppercase:", upper, "Lowercase:", lower)

# Program 6: Replace all occurrences of a character
s = input("Enter a string: ")
old = input("Character to replace: ")
new = input("New character: ")
result = ""
for ch in s:
    if ch == old:
        result += new
    else:
        result += ch
print("Modified string:", result)

# Program 7: Remove all spaces from string
s = input("Enter a string: ")
result = ""
for ch in s:
    if ch != " ":
        result += ch
print("String without spaces:", result)

# Program 8: Find frequency of a character
s = input("Enter a string: ")
ch = input("Enter character: ")
count = 0
for c in s:
    if c == ch:
        count += 1
print("Frequency of", ch, ":", count)

# Program 9: Print first and last character
s = input("Enter a string: ")
print("First character:", s[0])
print("Last character:", s[-1])

# Program 10: Display ASCII values of characters
s = input("Enter a string: ")
for ch in s:
    print(ch, ":", ord(ch))

# Program 11: Count words in a sentence
s = input("Enter a sentence: ")
words = s.split()
print("Word count:", len(words))

# Program 12: Find longest word in sentence
s = input("Enter a sentence: ")
words = s.split()
longest = max(words, key=len)
print("Longest word:", longest)

# Program 13: Find shortest word in sentence
s = input("Enter a sentence: ")
words = s.split()
shortest = min(words, key=len)
print("Shortest word:", shortest)

# Program 14: Convert first letter of each word to uppercase
s = input("Enter a sentence: ")
words = s.split()
result = ""
for w in words:
    result += w[0].upper() + w[1:].lower() + " "
print("Title case:", result.strip())

# Program 15: Print duplicate characters
s = input("Enter a string: ")
seen = set()
duplicates = set()
for ch in s:
    if ch in seen:
        duplicates.add(ch)
    else:
        seen.add(ch)
print("Duplicate characters:", "".join(duplicates))

