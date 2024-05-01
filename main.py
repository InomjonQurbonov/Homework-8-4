def has_odd_number_of_divisors(n):
    divisors = 0
    for i in range(1, n + 1):
        if n % i == 0:
            divisors += 1
    return divisors % 2 == 1


def find_numbers_with_property(L, R):
    hisob = len([n for n in range(L, R + 1) if has_odd_number_of_divisors(n)])
    return hisob - 1


T = int(input())
for _ in range(T):
    L, R = map(int, input().split())
    print(find_numbers_with_property(L, R))
