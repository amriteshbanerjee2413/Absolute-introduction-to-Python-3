
#Lists
y = [1, 2, 3]
y.pop()
print(y)
y.append("Hello")
print(y)
y.pop(0)
print(y)

#Dictonaries
items_for_supermarket = dict()
items_for_supermarket['Eggs'] = 10
items_for_supermarket['Bread'] = 5
items_for_supermarket['Milk'] = 29
items_for_supermarket['Sugar'] = 2
print(items_for_supermarket)

#Tuples
if (0, 1, 2) < (3, 4, 5):
    print("True")
else:
    print("False")
    
if ('ZZZZ', 'ZzZ') > ('Chris', 'Jean'):
    print("True")
else:
    print("False")
