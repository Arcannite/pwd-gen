upper = [chr(i) for i in range(65, 65+26)]
lower = [chr(i) for i in range(97, 97+26)]
num = [str(i) for i in range(10)]
sym = [chr(i) for i in range(33,48)] + [chr(i) for i in range(58,65)] + [chr(i) for i in range(91,97)] + [chr(i) for i in range(123,127)]  

import secrets



INCLUDE_UPPER_LETTERS = True

INCLUDE_LOWER_LETTERS = True

INCLUDE_NUMBERS = True

INCLUDE_SYMBOLS = True



charPool = []

if INCLUDE_UPPER_LETTERS: charPool.extend(upper)
if INCLUDE_LOWER_LETTERS: charPool.extend(lower)
if INCLUDE_NUMBERS: charPool.extend(num)
if INCLUDE_SYMBOLS: charPool.extend(sym)


pwdLength = 16

pwd = ''

for i in range(pwdLength):
    pwd += secrets.choice("".join(charPool))

print(pwd)
