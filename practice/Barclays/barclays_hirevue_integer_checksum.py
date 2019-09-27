# Barclays Programming challenge 2 description:
# Write a program that computes an integer's checksum. To compute the checksum, break the integer into its constituent digits 
# and, working from right to left, doubling every second digit. If the product results in a number with two digits, 
# treat those two digits independently. Then, sum all the digits for the final checksum. 
# For example, 1496 has a checksum of 21. We compute this by first breaking 1496 into constituents and 
# doubling the ever second digit => 6, 18, 4, 2. 
# Then, the individual digits are summed as 6 + (1 + 8) + 4 + 2 = 21.

# Input:
# Your program should read lines from standard input. Each line contains one integer.

# Output:
# For each line of input, print to standard output the integer's checksum, one checksum per line.

import sys
for line in sys.stdin:
    digits = str(line.strip())
    sum_list = []
    i = 0
    for digit in digits[::-1]:
      if i == 0:
        sum_list.append(int(digit))
      else:
        double_digit = int(digit) * 2
        sum_list += [int(d) for d in str(double_digit)]
      i = 1 - i
    print(sum(sum_list), end="")