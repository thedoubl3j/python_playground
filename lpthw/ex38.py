# Variable storing a list of things
ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. let's fix that.")

#variable storing ten things split method, splitting via whitespace. 
stuff = ten_things.split(' ')
# variable to store extra variables
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]
# The thing that does it all. While the length of variable stuff IS NOT 10, removes one element from more_stuff (next_one) and then appends it stuff. 
# Then counts to see how many elements are in stuff, if it is not 10, then it goes back through until it is 10. 
while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go:", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1]) #neat
print(stuff.pop())
print(' '.join(stuff)) #what in tarnation
print('#'.join(stuff[3:5])) #again, what in tarnation
