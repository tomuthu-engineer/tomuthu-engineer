# List index() Method --> it returns position at the first occurrence of the specified value

numbers = [1,2,3,5,4,6,23,1,8,2,9,7,6,3,4,5,6,3,2,1,4]

def find_index():
    a=numbers.index(9)
    return a
print(find_index())