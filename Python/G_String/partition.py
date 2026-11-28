var = "I Love Python"
new_var = var.partition('Love')
print(new_var)

new__var = var.partition('Java')
print(new__var)
# If the specified separator is not present,
# partition() returns the entire string as the first element.
# and two empty strings as the second and third elements.