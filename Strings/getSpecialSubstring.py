
# https://studyx.ai/homework/102975285-1-intelligent-substring-there-are-two-types-of-characters-in-a-particular-language
# https://www.geeksforgeeks.org/find-length-of-longest-substring-with-at-most-k-normal-characters/

def getSpecialSubstring(s, k, charValue): 
	n = len(s)
	if (k == 0):
		return 0
	count = 0
	left, right = 0, 0
	ans = 0
	while (right < n):
		while (right < n and count <= k):
			pos = ord(s[right]) - ord('a') 
			if (charValue[pos] == '0'):
				if (count + 1 > k):
					break
				else:
					count += 1
			right += 1
			if (count <= k):
				ans = max(ans, right - left)
		while (left < right): 
			pos = ord(s[left]) - ord('a')
			left += 1
			if (charValue[pos] == '0'):
				count -= 1
			if (count < k):
				break
	return ans

print(getSpecialSubstring("normal", 1, "00000000000000000000000000"))
print(getSpecialSubstring("giraffe", 2, "01111001111111111011111111"))
