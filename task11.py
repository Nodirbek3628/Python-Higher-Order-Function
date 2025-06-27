# Juft sonlarning kvadratlari

# Faqat juft sonlarni tanlab, ularning kvadratlarini `filter()` + `map()` bilan hisoblang.

# ```python
# nums = list(range(1, 21))

def num_square(a):
    return a ** 2

nums = list(range(1, 21))

juft_num = filter(lambda num: num % 2 == 0,nums)
result = map(num_square,juft_num)

print(list(result))