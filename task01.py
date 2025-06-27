# Foydali sonlarni ajratish

# Berilgan ro'yxatdan musbat sonlarni `filter()` yordamida ajrating.

# ```python
# numbers = [4, -2, 0, 7, -9, 3, -1, 5]

#function yaratish yuli bilan 

def positev_num(m):
    return m > 0

numbers = [4, -2, 0, 7, -9, 3, -1, 5]
result = filter(positev_num,numbers)

# print(list(result))

# Lambada yo'li bilan.

numbers = [4, -2, 0, 7, -9, 3, -1, 5]

result = filter(lambda number: number > 0, numbers )

print(list(result))


    