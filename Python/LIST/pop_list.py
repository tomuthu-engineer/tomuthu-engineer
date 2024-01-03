# List pop() Method --> it removes the element at the specified position

colors = ['red','blue','green','yellow','orange']

def pop_list():
    user_input=int(input('which position you want delete '))
    colors.pop(user_input)
    return colors
print(pop_list())