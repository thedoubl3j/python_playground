import random

###script to select random meal from a list and then remove it from the selection so that it cannot be picked again
#what do we need
'''
- need meal list
- the thing to select the meal
- thing to remove the selected item from the list

what to do
list already exists, how do we get stuff out of it. 
- a list has elements starting 0 -> n, (1, 2, 3, 4)
- pull random element from list
TODO : next thing is to put the random selection into a function and remove that selection from the list
'''

dinner = ['chicken', 'steak', 'pasta', 'veggie']
print(dinner)
first_entry = list.pop(dinner, 0)
print(first_entry)
random_selection = random.choice(dinner)
print(random_selection)