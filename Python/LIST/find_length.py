# find the length of the list

colors = input("Enter colors Names ").split()

def find_length(): #accepts strings only
    result = len(colors)
    return result
print(f"length of colors {find_length()} ")