# Barclays Programming challenge 1 description:
# Given a number and a pattern, map the numbers to the pattern and print the output of the mathematical expression.
# The pattern consists of lowercase english characters where each character maps to the corresponding digit
# in the number in the same location. The pattern also consists an operator in between which is either '+' or '-'
# For example, if the number is 486215 and the pattern is a-bcdef then the corresponding mathematical expression
# would be 4-86215 = −86211. Print the output -86211

# Input:
# Your program should read lines from standard input. Each line the number and the pattern separated by whitespace

# Output:
# For each line of input, print to standard output the result of the mathematical expression

import sys
for line in sys.stdin:
    number, pattern = line.split(' ')
    number_str = str(number)
    index_of_operator = 0
    for p in pattern:
        if p == '+' or p == '-':
            break
        index_of_operator += 1
    operator = pattern[index_of_operator]
    operand1 = number_str[:index_of_operator]
    operand2 = number_str[index_of_operator:]
    if operator == '+':
        print(int(operand1) + int(operand2), end="")
    else:
        print(int(operand1) - int(operand2), end="")
