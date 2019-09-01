# http://www.geeksforgeeks.org/maximum-sum-subarray-sum-less-equal-given-sum/

line1 = str(raw_input())
s = int(raw_input())
a = [int(x) for x in line1.split(", ")]
n = len(a)
max = -1
dp = [None]*n
for x in range(n, 0, -1):
	if max == s:
		break
	i = x - 1
	v = a[i]
	if v > s:
		continue
	dp[i] = [v]
	if v > max and v <= s:
		max = v
	if i+1 < n and dp[i+1] != None:
		for y in dp[i+1]:
			u = v + y
			if u > s:
				continue
			dp[i].append(u)
			if u > max and u <= s:
				max = u
print max
