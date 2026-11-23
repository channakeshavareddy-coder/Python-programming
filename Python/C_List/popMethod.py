list = [10, 20, 30, 40]
print("Original list", list)
print("----------------------->>")
removed_value = list.pop()
print("Removed value is: ",removed_value)
print("current list: ", list)
print("----------------------->>")
#With pop(index), when you want to remove a specific element, you specify its index.
print("Original list: ", list)
print("----------------------->>")
removed_element = list.pop(1)
#index 1 whatever the value  at index 1 is,# that will be removed and return.
print("Removed list: ", removed_element)
print("Current list: ", list)