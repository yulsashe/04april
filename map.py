def far(c):
    return (c*9/5)+32

numbers = [0,10,20,30,40]
far_numbers = map (far, numbers)
print (list(numbers))
print (list(far_numbers)) # [0,10,20,30,40]

def far2 (x):
    return x/5
numbers = [0,10,20,30,40]
far2_numbers = map (far2, numbers)
print (list(far2_numbers))