def validate_code(code):
    import re
    return bool(re.match(r"^[123]\d*$",str(code)))

def validate_code_og(code):
     return str(code).startswith(('1','2','3'))



print(validate_code(123) == True)
print(validate_code(248) == True)
print(validate_code(8) == False)
print(validate_code(321) == True)
print(validate_code(9453) == False)

# Basic regex tasks. Write a function that takes in a numeric code of any length. 
# The function should check if the code begins with 1, 2, or 3 and return true if so. Return false otherwise.

# You can assume the input will always be a number.
