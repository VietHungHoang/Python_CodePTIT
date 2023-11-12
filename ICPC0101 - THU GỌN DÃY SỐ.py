if __name__ == '__main__':
	n = int(input())
	a = list(map(int, input().split()))
	i = 1
	while i < len(a) and len(a) > 1:
		if (a[i] + a[i - 1]) % 2 == 0:
			a.pop(i)
			a.pop(i - 1)
			if i > 1: i -= 1 # Move left 1 cell to check the next pair. If i <= 1, cannot move left
		else: i += 1
	print(len(a))