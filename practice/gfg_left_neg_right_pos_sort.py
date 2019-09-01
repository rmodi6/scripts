# http://www.geeksforgeeks.org/move-negative-numbers-beginning-positive-end-constant-extra-space/

line = str(raw_input())
array = [int(x) for x in line.split(', ')]
i, j = 0, len(array)-1
while i < j:
	while array[i] < 0 and i < len(array)-1:
		i += 1
	while array[j] >= 0 and j > 0:
		j -= 1
	if i >= j:
		break
	array[i], array[j] = array[j], array[i]
print array