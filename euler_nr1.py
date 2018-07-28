for x in range(1, 1001):
    if x % 3 and x % 5:
        continue
    print(x)

"print('\n'.join(str(n) for n in range(1, 1001) if n % 5 == 0 or n % 3 == 0))"