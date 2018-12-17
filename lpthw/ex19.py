#creating the function cheese and crackers and passing in the 2 variables that are found in the ()
def cheese_and_crackers(cheese_count, box_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {box_of_crackers} boxes of crackers!")
    print("man that's enough for a party!")
    print("Get a blanket")
#printing the output of the simply giving the fucntion numbers
print("We can just give the function numbers directly")
cheese_and_crackers(20, 30)

#printing the output of storing numbers in variables and then passing those vars into the function
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#printing simple addition problems as the numbers that are passed into the function
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

#combining the two examples above (variables and math) and passing both in at once. Vars were created on line 13 and 14
print("And we can combine the two, variables and math.")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
