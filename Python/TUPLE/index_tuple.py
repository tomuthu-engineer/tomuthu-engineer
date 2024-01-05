# Tuple index() --> it finds the first occurrence of the specified value

this_tuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

def find_index(number):
    find_value=this_tuple.index(number)
    return find_value
print(find_index(7))