if __name__ == '__main__':
	for _ in range(int(input())):
		s = input()
		res = 10 ** 20
		num = 0
		for i in range(len(s)):
			if s[i].isdigit(): num = num * 10 + ord(s[i]) - 48
			elif i > 0 and s[i].isalpha() and s[i - 1].isdigit():
				res = min(res, num)
				num = 0
		print(res)