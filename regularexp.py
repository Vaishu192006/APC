'''#1.Write a Python program using regular expressions to extract all digits from a given string.
import re
s = "Hello123 Python456"
digits = re.findall(r'\d', s)
print("Digits:", digits)
#2.Accept a sentence and display all words beginning with the letter A or a.
import re
s = input("Enter a sentence: ")
words = re.findall(r'\b[Aa]\w*', s)
print("Words beginning with A or a:", words)
#3.Write a program to count the occurrences of vowels in a given string using regular expressions.
import re
s = input("Enter a string: ")
vowels = re.findall(r'[aeiouAEIOU]', s)
print("Total vowels:", len(vowels))

#4.Write a program to extract all uppercase letters from a given string.
import re
s = input("Enter a string: ")
letters = re.findall(r'[A-Z]', s)
print("Uppercase letters:", letters)

#5.Write a program to identify all spaces, tabs, and newline characters in a text.
import re
s = "Hello World\tPython\nProgramming"
chars = re.findall(r'[ \t\n]', s)
print("Spaces, tabs and newlines:", chars)
print("Total count:", len(chars))

#6.Write a program to replace multiple consecutive spaces with a single space.
import re
s = "Hello    World   Python"
result = re.sub(r' +', ' ', s)
print("Result:", result)

#7.Accept a sentence and display all words containing exactly five characters.
import re
s=input("Enter a string:")
words = re.findall(r'\b\w{5}\b', s)
print("Five-character words:", words)

#8.Write a program to identify all words ending with the letter s.
import re
s = input("Enter a sentence: ")
words = re.findall(r'\b\w*s\b', s, re.IGNORECASE)
print("Words ending with s:", words)
#9.Write a program to remove all special characters from a given string while retaining letters, digits, and spaces.
import re
s = input("Enter a string: ")
result = re.sub(r'[^A-Za-z0-9 ]', '', s)
print("Result:", result)
#10.Write a program to count the number of words in a sentence using regular expressions.
import re
s = input("Enter a sentence: ")
words = re.findall(r'\b\w+\b', s)
print("Number of words:", len(words))
#11.Write a program to validate a 10-digit Indian mobile number using a regular expression.
import re
num = input("Enter mobile number: ")
if re.fullmatch(r'[6-9]\d{9}', num):
    print("Valid mobile number")
else:
    print("Invalid mobile number")
#12.Accept an email address and check whether it follows a reasonable email format.
import re
email = input("Enter email: ")
if re.fullmatch(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', email):
    print("Valid email")
else:
    print("Invalid email")'''
#13.Write a program to extract dates in DD-MM-YYYY format from a given paragraph
import re
s = input("Enter a paragraph: ")
dates = re.findall(r'\b\d{2}-\d{2}-\d{4}\b', s)
print("Dates:", dates)
#14.Write a program to identify web addresses beginning with http:// or https://.
import re
s = input("Enter text: ")
urls = re.findall(r'https?://\S+', s)
print("Web addresses:", urls)
#15.Write a program to extract all hashtags from a social media post.
import re
s = input("Enter a post: ")
hashtags = re.findall(r'(?<!\w)#[A-Za-z0-9_]+', s)
print("Hashtags:", hashtags)
#16.Write a program to check whether a password contains at least eight characters, one uppercase letter,
#one lowercase letter, one digit, and one special character.
import re
password = input("Enter password: ")
pattern = r'(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[^A-Za-z0-9\s])\S{8,}'
if re.fullmatch(pattern, password):
    print("Valid password")
else:
    print("Invalid password")
#17.Write a program to identify consecutive repeated words in a sentence, ignoring case differences.
import re
s = input("Enter a sentence: ")
words = re.findall(r'\b(\w+)\s+\1\b', s, re.IGNORECASE)
print("Repeated words:", words)
#18.Write a program to extract six-digit Indian PIN codes from a paragraph.
import re
s = input("Enter a paragraph: ")
pins = re.findall(r'\b[1-9]\d{5}\b', s)
print("PIN codes:", pins)
#19.Write a program to check whether an input matches a common Indian vehicle registration format, such as MH12AB1234.
import re
num = input("Enter vehicle number: ")
pattern = r'[A-Z]{2}\d{1,2}[A-Z]{1,3}\d{4}'
if re.fullmatch(pattern, num):
    print("Valid vehicle number format")
else:
    print("Invalid vehicle number format")
#20.Write a program to extract file extensions from filenames in a given string.
import re
s = input("Enter filenames: ")
extensions = re.findall(r'\.([A-Za-z0-9]+)\b', s)
print("File extensions:", extensions)
#21.Write a program to remove HTML tags, extra whitespace, and unwanted punctuation from a text document.
import re
s = input("Enter text: ")
s = re.sub(r'<[^>]*>', '', s)
s = re.sub(r'[^\w\s.,]', '', s)
s = re.sub(r'\s+', ' ', s)
print("Clean text:", s.strip())
#22.Extract invoice numbers, dates, and monetary amounts from invoice text using regular expressions.
import re
s = input("Enter invoice text: ")
invoice = re.findall(r'Invoice No:\s*(\w+-?\w*)', s)
dates = re.findall(r'\b\d{2}-\d{2}-\d{4}\b', s)
amounts = re.findall(r'₹\s*[\d,]+(?:\.\d{2})?', s)
print("Invoice number:", invoice)
print("Dates:", dates)
print("Amounts:", amounts)
#23.Write a program to identify single-line comments in Python source code. Discuss why regular expressions alone may not correctly handle every string literal or multiline case.
import re
s = input("Enter Python code: ")
comments = re.findall(r'^\s*#.*$', s, re.MULTILINE)
print("Comments:", comments)
#24.Validate product codes following the pattern ABC-1234-XY, where letters and digits must appear in the specified positions.
import re
code = input("Enter product code: ")
if re.fullmatch(r'[A-Z]{3}-\d{4}-[A-Z]{2}', code):
    print("Valid product code")
else:
    print("Invalid product code")
#25.Given a paragraph containing student names, roll numbers, and marks, extract each field using regular expressions.
import re
s = input("Enter student details: ")
pattern = r'Name:\s*(\w+)\s*,\s*Roll:\s*(\d+)\s*,\s*Marks:\s*(\d+)'
result = re.findall(pattern, s)
for name, roll, marks in result:
    print("Name:", name)
    print("Roll Number:", roll)
    print("Marks:", marks)
#26.Extract DOI identifiers, publication years, email addresses, and URLs from a collection of research paper references.
import re
s = input("Enter research references: ")
doi = re.findall(r'\b10\.\d{4,9}/\S+', s)
years = re.findall(r'\b(?:19|20)\d{2}\b', s)
emails = re.findall(r'[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}', s)
urls = re.findall(r'https?://\S+', s)
print("DOI:", doi)
print("Years:", years)
print("Emails:", emails)
print("URLs:", urls)

