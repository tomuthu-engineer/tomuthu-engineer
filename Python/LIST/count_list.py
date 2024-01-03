# List count() method --> It returns the no of elements with specified value

count_list = [1,2,3,4,1,2,3,4,5,4,4,3,7,4,6,9,8]

def count():
    user_input = int(input("Enter any number "))
    counter = count_list.count(user_input)
    return counter
print(count())

