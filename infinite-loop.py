# Motive: to learn how to harness the power of infinite loops

# Task: Take input from user and keep asking for more inputs till the user deny to answer.


# Infinite Loop

while True:
    name = input("Enter your name: ")
    should_continue = input("Dou you want to continue? (Y/N)")
    if (should_continue == "N"):
        break
print("You opt to exit the program")
