import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

def deff(str):
    for i in str:
        if not is_prime(int(i)):
            return 'No'
    s = sum([int(i) for i in str])
    num1, num2 = str, str[::-1]
    if not is_prime(s) or not is_prime(int(num1)) or not is_prime(int(num2)):
        return 'No'
    return 'Yes'
if __name__ == '__main__':
    for _ in range(int(input())):
        print(deff(input()))
