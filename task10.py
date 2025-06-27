#  Matndan raqamlarni ajratish

# Berilgan matndan faqat sonlarni ajrating:

# ```python
# text = ["apple", "34", "banana", "100", "abc", "75"]
# ```

# > Natija: `['34', '100', '75']`

text = ["apple", "34", "banana", "100", "abc", "75"]

result = filter(str.isdigit,text)
print(list(result))