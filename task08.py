# Yoshi bo'yicha sortlash

# Quyidagi lug’atdagi odamlarni yosh bo’yicha o’sish tartibida saralang.

# ```python
# people = [
#   {"name": "Ali", "age": 25},
#   {"name": "Sami", "age": 19},
#   {"name": "Lola", "age": 31}
# ]

def growing_age(user):
    return user["age"]

people = [
  {"name": "Ali", "age": 25},
  {"name": "Sami", "age": 19},
  {"name": "Lola", "age": 31}
]

result = sorted(people,key=growing_age)
print(list(result))

