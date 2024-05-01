def min_questions_to_guess_number(N):
    import math
    return math.ceil(math.log2(N))


N = int(input())
print(min_questions_to_guess_number(N))