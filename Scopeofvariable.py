# Global variable
x = 10

def my_function():
    # Local variable
    y = 5
    print("Inside the function:")
    print("Global variable x:", x)  # Accessing global variable
    print("Local variable y:", y)    # Accessing local variable

my_function()  # Call the function

# Accessing global variable outside the function
print("Outside the function:")
print("Global variable x:", x)
print("Local variable y:", y)
#Trying to access local variable y outside the function will cause an error
# Uncommenting the line below will result in a NameError
# print("Local variable y:", y)  # This will raise an error
