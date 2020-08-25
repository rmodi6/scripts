# When a passenger buys a ticket the ticket contains an account number. When the ticket is scanned for entry to the transit system, the account number needs to be validated.
# 
# Our validation mechanism is quite simple: the account number is eight hexadecimal digits, and the first two digits is a checksum which is calculated from the sum of the last six digits.
# 
# You will be provided a list of account numbers as input, such as BADFOODS.
# 
# You should provide a line of output per line of input that states if the account number is VALID or INVALID.

import fileinput

def process(line: str) -> str:
    # Return 'VALID' or 'INVALID'
    if len(line) != 8:
        return 'INVALID'
    try:
        num = int(line[2:], 16)
        checksum = sum([int(i) for i in str(num)])
        return 'VALID' if hex(checksum) == hex(int(line[:2], 16)) else 'INVALID'
    except Exception:
        return 'INVALID'

for line in fileinput.input():
    print(process(line.rstrip()))