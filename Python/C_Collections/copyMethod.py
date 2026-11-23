# .copy is used to create copy of an existing list.
list = [10, "Channakeshavareddy G N", True, 22]
print(list)
print("----------------->")
new_list = list.copy()
print(new_list)

# If you modify the copied list, the original list remains unchanged:
print("----------------->")
new_list[1] = "Channa"
print(list)
print(new_list)