# lambda` bilan ro'yxatni qisqartirish

# Berilgan ro’yxatdagi faqat string va uzunligi 5 dan katta bo‘lganlarni ajrating:

# ```python
# data = [123, "apple", "banana", "cat", 456, "mango", "elephant"]
# ```

data = [123, "apple", "banana", "cat", 456, "mango", "elephant"]

ab_jsj = filter(str.upper,data)
print(list(ab_jsj))