def registr(x):
    return x.upper(x)

numbers = ['hello','world','python','programming']
registr_numbers = map (len, numbers)
print (list(registr_numbers)) # []