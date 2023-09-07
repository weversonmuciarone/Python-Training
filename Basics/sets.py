
# Sets
#     Similar a listas
#     Evita items duplicados
#     nao utiliza index
#     {} Curly Brackets means Sets
#     | single pipe means union which I have two diff lists and it has removed the dupes
#     - means difference hence it will only show distinct values
#     ^ means symmetric difference which will only show distict number from both values, it will remove the values with they're present in both lists
#     & means And which will only show whats duplicated in both lists
'''
list1 = [10, 20, 30, 40, 50]
list2 = [10, 20, 60, 70]

num1 = set(list1)
num2 = set(list2)

print(num1 | num2) # Union
print(num1 - num2) # Difference
print(num1 ^ num2) # Symmetric Difference
print(num1 & num2) # And

s1 = {10, 20, 30, 40, 50} # The use of curly brackets tells python that this is a set hence there is no need to convert using set()
s1.add(70) # sets does not duplicate hence if I try to add an existing numb it won't duplicate
s1.update([80, 90, 100]) # Update will allow to add multiple items
s1.remove(10) # Removes a value if exists or throw an error if the value you're trying to remove does not exist
s1.discard(20) # Removes a value same as above but if the value does not exist it won't give an error, will ignore
print(s1)
'''

# Sets scom strings
#     Similar a listas
#     Evita items duplicados
#     nao utiliza index

set1 = {'a', 'b', 'c'}
set2 ={'a', 'd', 'e'}
set3 = {'c', 'd', 'f'}

set4 = set1.intersection(set2) # Intersection will display the value that is present in both
print(set4)