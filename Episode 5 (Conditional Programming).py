#First part
age = 40
if age > 40:
  print('You should retire soon')
elif age == 30:
  print('You are at your prime')
elif age == 40:
  print('40s are a great time to relax for a while')
else:
  print('You are young!!!')



#Second part
print('Hi, welcome to the sandwich shop. Please select a sandwich to continue.')
sandwichtype = input('"c" for Cheese sandwiches or "v" for a Veggie Special "nv" for a non-vegetarian sandwich. \nWhich Option? ')
print()

if sandwichtype.lower() == "c":
  #select cheese type
  print('Please select a cheese.')
  cheesetype = input('"C" for cheddar or "M" for Manchego: ')
  print()

  if cheesetype.lower() == "c":
    print('Here is your cheddar cheese sandwich, thank you!')
  else:
    print('Here is your Manchego cheese sandwich, thanks!')
  
elif sandwichtype.lower() == "v":
  print('Here is your veggie special sandwich')

elif sandwichtype.lower() == "nv":
    print('What meat would you like? ')
    meattype = input('Enter "c" for chicken, "b" for beef, "l" for lamb or "f" for fish ')
    if meattype.lower() == "c":
        print('Here is your chicken sandwich')
    elif meattype.lower() == "b":
        print('Here is your beef sandwich')
    elif meattype.lower() == "l":
        print("Here is your lamb sandwich")
    else:
        print('Here is your fish sandwich')

else:
  print('We do not have what you are looking for!')
