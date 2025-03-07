# Global variable
name = "Global Variable"

def my_function():
    # Local variable 
    name = "Local Variable"
    print("Inside Function:", name)  # Prints local variable

# Calling the function
my_function()

# Printing global variable
print("Outside function:", name)  # Prints global variable