# List insert() Method -->  it insert specified value at the specified position

colour = ['blue','red','green']

def insert_colour():
    user_index=int(input('Enter position '))
    user_color=input('Enter your color ')
    colour.insert(user_index,user_color)
    return colour
print(insert_colour())