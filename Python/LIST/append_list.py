# list append() method --> it adds an element at the end of the list

list1= ['red','yellow','green']

def color(): 
    user_input=input('Enter One color:')
    list1.append(user_input)
    return list1

print(color())