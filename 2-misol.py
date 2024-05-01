def count_chiroyli_numbers(L, R):
    def is_chiroyli(n):
        n_str = str(n)
        return n_str[0] == n_str[-1]

    count = 0
    for num in range(L, R + 1):
        if is_chiroyli(num):
            count += 1
    return count


L, R = map(int, input().split())
print(count_chiroyli_numbers(L, R))