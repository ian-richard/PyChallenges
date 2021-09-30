# Implement a function which convert the given boolean value into its string representation.

# Note: Only valid inputs will be given.

def boolean_to_string_og(b):
    return 'True' if b == True else 'False'
        

def boolean_to_string_convert(b):
    return str(b)

def boolean_to_string(b):
    return 'True' if b else 'False'
    
        
print(boolean_to_string(True) == "True")

print(boolean_to_string_convert(False) == "False")