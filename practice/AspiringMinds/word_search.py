# Sample code to read input and write output:

'''
NAME = raw_input()            # Read input from STDIN
print 'Hello %s' % NAME       # Write output to STDOUT
'''

# Warning: Printing unwanted or ill-formatted 
# data to output will cause the test cases to fail

# Write your code here
def recurse(matrix, word, r, c, n):
    if len(word) == 0:
        return True
    if r < 0 or r >= n or c < 0 or c >= n or matrix[r][c] != word[0]:
        return False
    present = False
    matrix[r][c] = '_'
    for direction in [(0,1), (0,-1), (1,0), (-1,0)]:
        present = recurse(matrix, word[1:], r + direction[0], c + direction[1], n)
        if present:
            break
    matrix[r][c] = word[0]
    return present

def exist(word, matrix, n):
    for r in range(n):
        for c in range(n):
            if recurse(matrix, word, r, c, n):
                return 'Yes'
    return 'No'


n = int(raw_input())
matrix = [raw_input().strip().split() for _ in range(n)]
m = int(raw_input())
words = raw_input().strip().split()
ans = []
for word in words:
    ans.append(exist(word, matrix, n))
print(' '.join(ans))
