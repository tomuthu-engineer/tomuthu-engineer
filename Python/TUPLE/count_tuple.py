# Tuple count() Method --> it returns the number of times a specfied value appears in this tuple

def value_count(number):
    this_tuple =(1,2,3,4,7,5,4,3,5,4,7,8,9,6,3,1,4,5,23,1,4,7,3,1,7,8,3,14,8)
    value_count=this_tuple.count(number)
    return value_count
print(value_count(5))
    