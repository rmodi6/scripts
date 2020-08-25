# Count the odd number of entries in the input
# Sample code to read input and write output:

'''
NAME = input()                # Read input from STDIN
print("Hello " + NAME)        # Write output to STDOUT
'''

# Warning: Printing unwanted or ill-formatted 
# data to output will cause the test cases to fail

# Write your code here
n = int(input())
days = [int(x) for x in input().strip().split()]
arr = [0] * 32
for day in days:
    arr[day] += 1
ans = 0
for a in arr:
    ans += (a % 2)
print(ans)
