# Narxlarni \$ belgisiz olish

# Quyidagi narxlar ro’yxatidan `$` belgisiz faqat raqamlarni ajrating (lambda bilan).

# ```python
# prices = ["$120", "$340", "$50", "$90"]
# ```

prices = ["$120", "$340", "$50", "$90"]

result = map(lambda pric: pric.replace("$"," "),prices)
print(list(result))