#  Top 3 eng uzun so‘z

# Matndagi eng uzun 3 ta so‘zni toping:

# ```python
# sentence = "Functional programming in Python is very powerful and elegant"
# ```

# > Foydalaning: `sorted()`, `lambda`, `split()`, `[:3]`

sentence = "Functional programming in Python is very powerful and elegant"

words = sentence.split()
sort_word = sorted(words,key=lambda word:(len(word)),reverse=True)
final_word = sort_word[:3]


print(list(final_word))