# lambda` bilan ro'yxatni qisqartirish

# Berilgan ro’yxatdagi faqat string va uzunligi 5 dan katta bo‘lganlarni ajrating:

# ```python
# data = [123, "apple", "banana", "cat", 456, "mango", "elephant"]
# ```

data = [123, "apple", "banana", "cat", 456, "mango", "elephant"]

words = filter(lambda a: isinstance(item,str) and len(a)>5,)

print(list(words))