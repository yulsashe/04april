def lg(x):
    return len(x)

numbers = ['apple','banana','orange','kiwi']
lg_numbers = map (len, numbers)
print (list(lg_numbers)) # []