# http://www.geeksforgeeks.org/count-palindrome-sub-strings-string-set-2/

def palindrome(input_str, start_index, end_index):
	substr = input_str[start_index:end_index + 1]
	length = len(substr)
	if length == 1:
		return True
	if length == 2:
		return substr[0] == substr[1]
	if (start_index, end_index) not in dp:
		dp[(start_index, end_index)] = substr[0] == substr[length - 1] and palindrome(input_str, start_index + 1, end_index - 1)
	return dp[(start_index, end_index)]

input_str = str(raw_input())
n = len(input_str)
count, dp = 0, {}
for diff in range(1, n):
	start_index = 0
	end_index = start_index + diff
	while end_index < n:
		if palindrome(input_str, start_index, end_index):
			count += 1
		start_index += 1
		end_index += 1
print count
print dp