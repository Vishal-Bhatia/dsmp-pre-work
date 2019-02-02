# --------------
# Code starts here
##Creating class lists
class_1 = ['Geoffrey Hinton', 'Andrew Ng', 'Sebastian Raschka', 'Yoshua Bengio']
class_2 = ['Hilary Mason', 'Carla Gentry', 'Corinna Cortes']

##Concatenating the two lists and printing the combined list out
new_class = class_1 + class_2
print(new_class)

##Adding missing student to the existing list, and printing the updated list
new_class.append('Peter Warden')
print(new_class)

##Removing incorrect entry, and printing the updated list
new_class.remove('Carla Gentry')
print(new_class)
# Code ends here


# --------------
# Code starts here
##Creating a dictionary of the marks obtained by Geoffrey Hinton, and printing it
courses = {'Math':65, 'English':70, 'History':80, 'French':70, 'Science':60}
print(courses)

##Summing the marks obtained, and printing it
total = sum(courses.values())
print(total)

##Calculating percentage scored by Geoffrey Hinton, and printing it
percentage = total*100/500
print(percentage)
# Code ends here


# --------------
# Code starts here
##Creating the list of scores in maths by students
mathematics = {'Geoffrey Hinton':78, 'Andrew Ng':95, 'Sebastian Raschka':65, 'Yoshua Benjio':50, 'Hilary Mason':70, 'Corinna Cortes':66, 'Peter Warden':75}
print(mathematics)

##Using the max function to obtain the topper
topper = max(mathematics, key = mathematics.get)
print (topper)
# Code ends here


# --------------
# Given string
topper = 'andrew ng'

# Code starts here
##Splitting using the split() function
topper_split = topper.split(" ", 2)

##Identifying the first and last names, and concatenating them such that the last name is shown first
first_name = topper_split[0]
last_name = topper_split[1]
full_name = last_name + ' ' + first_name

##Upper-casing the full name, and printing it
certificate_name = full_name.upper()
print(certificate_name)
# Code ends here


