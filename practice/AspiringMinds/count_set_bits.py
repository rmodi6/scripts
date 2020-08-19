# Sample code to read input and write output:

'''
NAME = input()                # Read input from STDIN
print("Hello " + NAME)        # Write output to STDOUT
'''

# Warning: Printing unwanted or ill-formatted 
# data to output will cause the test cases to fail

# Write your code here

num = int(input())
print(sum(map(int, bin(num)[2:])))
