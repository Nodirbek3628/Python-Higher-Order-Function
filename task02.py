# Har bir sonni kvadratga oshiring

# `map()` yordamida quyidagi ro'yxatdagi har bir sonni kvadratga oshiring.

# ```python
# nums = [1, 2, 3, 4, 5]


def thigh_leveel(a):
    return a ** 2
    

nums = [1, 2, 3, 4, 5]
result = map(thigh_leveel,nums)    # result = map(lamda num : num**2, nums)   lamda yuli bilan 
print(list(result))