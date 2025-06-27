# Talabalarni baho bo‘yicha tartiblang

# Baholar bo‘yicha saralash (kichikdan katta):

# ```python
# students = [
#   {"name": "Aziz", "grade": 89},
#   {"name": "Kamola", "grade": 95},
#   {"name": "Javlon", "grade": 76}
# ]

def growth(studen):
    return studen["grade"]

students = [
    {"name": "Aziz", "grade": 89},
    {"name": "Kamola", "grade": 95},
    {"name": "Javlon", "grade": 76}
]

result = sorted(students,key=growth)
print(list(result))