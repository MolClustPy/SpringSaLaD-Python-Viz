original_list = [1, 2, 3, 4]
position = 2
element = 'a'

# Creating a new list with the element inserted
new_list = original_list[:position] + [element] + original_list[position:]

print("Original List:", original_list)
print("New List:", new_list)
