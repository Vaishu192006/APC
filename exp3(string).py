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
# Program 16: Display frequency of each character
s = input("Enter a string: ")
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
for k, v in freq.items():
    print(k, ":", v)

# Program 17: Check if two strings are anagrams
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
if sorted(s1) == sorted(s2):
    print("Anagrams")
else:
    print("Not anagrams")

# Program 18: Remove duplicate characters
s = input("Enter a string: ")
result = ""
seen = set()
for ch in s:
    if ch not in seen:
        result += ch
        seen.add(ch)
print("Without duplicates:", result)

# Program 19: Check if substring exists
s = input("Enter main string: ")
sub = input("Enter substring: ")
if sub in s:
    print("Substring exists")
else:
    print("Substring not found")

# Program 20: Count occurrences of a word
s = input("Enter a sentence: ")
word = input("Enter word: ")
words = s.split()
count = 0
for w in words:
    if w == word:
        count += 1
print("Occurrences of", word, ":", count)

# Program 21: Validate password
import string
pwd = input("Enter password: ")
if (len(pwd) >= 8 and
    any(ch.isupper() for ch in pwd) and
    any(ch.islower() for ch in pwd) and
    any(ch.isdigit() for ch in pwd) and
    any(ch in string.punctuation for ch in pwd)):
    print("Valid password")
else:
    print("Invalid password")

# Program 22: Run-length encoding
s = input("Enter a string: ")
i = 0
result = ""
while i < len(s):
    count = 1
    while i + 1 < len(s) and s[i] == s[i+1]:
        count += 1
        i += 1
    result += s[i] + str(count)
    i += 1
print("Encoded string:", result)

# Program 23: Compress string if shorter
s = input("Enter a string: ")
i = 0
compressed = ""
while i < len(s):
    count = 1
    while i + 1 < len(s) and s[i] == s[i+1]:
        count += 1
        i += 1
    compressed += s[i] + str(count)
    i += 1
print("Compressed string:", compressed if len(compressed) < len(s) else s)

# Program 24: Find most frequent character
s = input("Enter a string: ")
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
most = max(freq, key=freq.get)
print("Most frequent character:", most)

# Program 25: Find second most frequent character
s = input("Enter a string: ")
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
if len(sorted_freq) > 1:
    print("Second most frequent character:", sorted_freq[1][0])
else:
    print("No second most frequent character")

