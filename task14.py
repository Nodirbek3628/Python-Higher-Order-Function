# list.sort bilan joyida o'zgartirish

# Quyidagi ro’yxatni uzunlik bo‘yicha joyida sort qiling:

# ```python
# words = ["sun", "mountain", "a", "apple"]
# ```

# > `list.sort(key=lambda ...)` ishlatilishi kerak.

# ---

words = ["sun", "mountain", "a", "apple"]

words.sort(key=lambda word: len(word))

print(words)