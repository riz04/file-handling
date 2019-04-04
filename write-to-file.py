# This file contains code to learn how to write data to a file using python
# This is also known as storing data in flat files
# The type of files can be .csv, .json or even .txt
# Other ways to store data is to store data inside a database


# For now we are focusing on storing data in files

# To read from/write to a file in Python first we have to open it using the in-built open() function
# Never forget to close the file, else it will stay in the memory(RAM)

# Let's make a file to store the name and mobile number of users (A phonebook app)

# Step I: Create a file (using open() function to open a file, if it's not there, a new file will be created)
# Step II: We'll using the 'a+' mode because we have to use the same file to store data of multiple users
# Step III: Write the Name & Mobile number of the user to the file
# Step IV: Save the file
# Step V: Read the data from the file and simply print it to the console

# Opening a file, if it's not there, a new file witht the given name will be created
newfile = open("phonebook.csv", "a+")

# writing in a file

newfile.write("\nriz, 88888888")
newfile.write("\nram, 89898888")

# When you opwn file in append mode, it reads the whole file and goes to the last (so that you can add new data instead of overitting the old data), hence we need to use fileobject.seek() if we want to print the contents of the file
newfile.seek(0)

# fileobject.readline() function is used to read the file line by line
# fileobject.readlines() function is used to get all the lines of a file in the form of a list
all_lines = newfile.readlines()

# print line by line
for line in all_lines:
    print(line)

# finally close the file
