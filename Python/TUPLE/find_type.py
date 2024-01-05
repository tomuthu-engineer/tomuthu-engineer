# find the type of the collection using type() function

def find_type():
        user_input=input("Enter Five color:").split()
        converted_value=tuple(user_input)
        value_type=type(converted_value)
        return value_type
print(find_type())