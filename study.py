### Section: String to Integer Conversion and Addition
# data_string = '12'
# number = 10
# new_number = int(data_string)
# together = number + new_number
# print(together)

### Section: Logical Operators (and, or, not)
# x = 10
# y = 20

# print(x > 3 and y < 30) #both conditions are true
# print(x > 3 or y < 10) #only one needs to be true
# print(not (x == 11)) #negation of the first condition

### Section: Simple Login System with Limited Attempts
# name = "admin"
# password = "4321"

# count = 0
# while count < 3:
#     input_name = input("Enter your name: ")
#     input_password = input("Enter your password: ")

#     if input_name == name and input_password == password:
#         print("Welcome!")
#         break
#     else:
#         if input_name != name:
#             print("Invalid name")
#         else:
#             print("Invalid password")
    
#     count += 1

# if count == 3:
#     print("Account locked.")

### Section: Loop Control with continue and break
# Use continue to skip 5
# Use break if the number is 8

# for i in range(10):
#     if i == 5:
#         continue
#     print(i)

# print("------")

# for i in range(10):
#     if i == 8:
#         break
#     print(i)

### Section: Merging Two Lists Without Duplicates
# def marge_arrays(array1, array2):
#     return sorted(set(array1 + array2))

# list1 = [1, 3, 5, 7]
# list2 = [2, 4, 6, 8]
# merge = marge_arrays(list1, list2)
# print(merge)

### Section: strip() removes LEADING and trailing spaces clean space, tabs, new lines

# text = "  warning  "
# clean = text.strip()
# print(clean)
# text2 = "<<<warning!!!>>>"
# clean2 = text2.strip("<!>") #specific characters
# print(clean2)

### Section: split() splits a string into a list based on separator (space by default) 

# sentence = "python is awesome python is cute"
# parts = sentence.split("python") #[2] will cut the string at this location, and remove from result
# print(parts)

### Section: f-string lets you embed python expressions directly inside of a string, using curly brackets.
# name = "Jean"
# age = 28
# print(f"my name is {name}, and i am {age} years old.")
# expression {age + 2}
#works with functions {text(function)}
#format numbers {price:.2f} #2 decimal places
##works with dates##
# import datetime
# today = datetime.date.today()
# print(f"Today is {today:%B %d, %Y}")

### Section: Capitalize str
# name = "aloha"
# cap = name.capitalize()
# print(cap)

### Section: Title cap both words
# name = "aloha jean"
# cap = name.title()
# print(cap)


### Section:
### Section:
### Section:
