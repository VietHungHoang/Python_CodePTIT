if __name__ == '__main__':
    while True:
        arr = list(map(int, input().split()))
        if arr.count(0) == 4: break
        cnt = 0
        while arr.count(arr[0]) != 4:
            tmp = arr.copy()
            for i in range(4): arr[i] = abs(tmp[i] - tmp[(i + 1) % 4])
            cnt += 1
        print(cnt)
