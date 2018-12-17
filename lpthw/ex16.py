#importing argument variable (argv), the variable holds the arguments you pass to python when you run the script, ex here is filename on line 6.
from sys import argv
#unpacks argv and gets assigned to script and filename
script, filename = argv
#using filename here for argv, taking in whatever the user types in
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL + C (^C).")
print("If you want to do that, hit RETURN.")
#I am assuming we are waiting for input here?
input("?")
#opening the file that is stored in the filename variable and then storing the result in target. "w" means we want to also write to that file
print("Opening the file now...")
target = open(filename, 'w')
#truncating target
print("Truncating the file now. Goodbye!")
target.truncate()

print("Now I am going to ask you for three lines.")
#asking for input storing the input in the line variables
line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("I'm going to write these to the file.")
#write the lines stored in each variable and then write a page break
target.write(line1)
target.write("/n")
target.write(line2)
target.write("/n")
target.write(line3)
target.write("/n")

print("And finally, we close it.")
target.close()
