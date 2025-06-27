# Eng uzoq ismni toping

# `max()` va `lambda` yordamida eng uzun ismni toping:

# ```python
# names = ["Ali", "Valijon", "Sami", "Diyorbek"]
# ```

names = ["Ali", "Valijon", "Sami", "Diyorbek"]

result = max(names,key=lambda name: len(name))

print(result)
