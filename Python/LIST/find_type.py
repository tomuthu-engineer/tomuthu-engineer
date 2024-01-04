# find the type of the list using type() function

user_input = input("Enter Any number ").split()

def find_type():
    result=type(user_input)
    return result

print(find_type())
print(user_input)