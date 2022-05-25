import secrets
from string import digits
from string import punctuation
from string import ascii_letters


password = ""
dictionary = digits + punctuation + ascii_letters
dictionary2 = digits + " ~`!@#$%^&*()_-+}={[]|\:;<,>.?/" + ascii_letters
length = 20

for i in range(length):
    password += "".join(secrets.choice(dictionary2))


print(password)