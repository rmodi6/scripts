# http://www.geeksforgeeks.org/longest-subarray-sum-elements-atmost-k/

line = str(raw_input())
k = int(raw_input())
array = [int(x) for x in line.split(', ')]
subarray = []
sum, maxlen = 0, 0
for x in array[1:]:
	subarray.append(x)
	sum += x
	if len(subarray) > maxlen and sum <= k:
		maxlen = len(subarray)
	while sum > k and len(subarray) > 0:
		sum -= subarray.pop(0)
print maxlen