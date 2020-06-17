# Module Regular Expressions(RE)
import re

email_pattern = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|net)"

print("Enter email :")
user_input_1 = input()

if(re.search(email_pattern, user_input_1)):
	print("valid email")
else:
	print("invalid input")

# ========================================

# remove hyphen from phone number

pattern = "(\d\d\d)-(\d\d\d)-(\d\d\d\d)"

# r => raw input string
new_pattern = r"\1\2\3"

print("Enter number (xxx-xxx-xxxx) :")
user_input = input()

new_user_input = re.sub(pattern, new_pattern, user_input)
print(new_user_input)

# ===========================================

# Regular expressions are compiled into pattern objects

#case sensitive
p = re.compile('[a-e]')

print(p.findall("Aye, said Mr. Gibenson Stark")) 
# ['e', 'a', 'd', 'b', 'e', 'a']

# ===========================================

# split()
#  re.split(pattern, string, maxsplit=0, flags=0)

# sub() - substring
# repl - replace string
# re.sub(pattern, repl, string, count=0, flags=0)
print(re.sub('ub', '_test_repace_' , 'Subject has Uber booked already', flags = re.IGNORECASE)) 
# S_test_repace_ject has _test_repace_er booked already

# ===========================================

# subn()

# It returns a tuple with count of total of replacement
# and the new string rather than just the string.

# re.subn(pattern, repl, string, count=0, flags=0)

print(re.subn('ub', '~*' , 'Subject has Uber booked already'))
# ('S~*ject has Uber booked already', 1)

# escape()
# re.escape(string)
print(re.escape("This is Awseome even 1 AM")) 
# This\ is\ Awseome\ even\ 1\ AM
