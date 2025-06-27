# Tanlovlar ro'yxatidan eng ko'p ovoz olganini topish

# Har bir tanlovda necha ovoz borligini bilgan holda eng ko'p ovoz olgan variantni aniqlang.

# ```python
# votes = [
#   {"option": "A", "votes": 123},
#   {"option": "B", "votes": 145},
#   {"option": "C", "votes": 97}
# ]
# ```

# > `max(..., key=lambda x: x["votes"])`

def votes_age(user):
    return user["votes"]

votes = [
  {"option": "A", "votes": 123},
  {"option": "B", "votes": 145},
  {"option": "C", "votes": 97}
]

max_votes = max(votes,key=votes_age )

print([max_votes])