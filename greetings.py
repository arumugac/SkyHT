# Example of a local scope - variable is outside the Main program
def greeting(name):
    print('Hello', name)

# Main program
input_name1 = input('Enter your name:\n')
greeting(input_name1)
input_name2 = input('Enter another name:\n')
greeting(input_name2)



# Example of global scope - variable is in the Main program

# def greeting():
#     print('Hello', name)
#
# # Main program
# name = input('Enter your name:\n')
# greeting()
# print('Thanks', name)
