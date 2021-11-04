import operator

OPS = {
    "AND": operator.and_,
    "OR" : operator.or_,
    "XOR": operator.xor
}

def logical_calc_OPS(array, op):
    return reduce(OPS[op], array)

def logical_calc(array, op):
    res = array[0]
    for x in array[1:]:
        if op == "AND":
            res &= x
        elif op == "OR":
            res |= x
        else:
            res ^= x
        
    return res 

print(logical_calc([True, True, False, False], "AND") == False)
print(logical_calc([True, True, False, False], "OR") == True)
print(logical_calc([True, True, False, False], "XOR") == False)

'''
Your Task

Given an array of Boolean values and a logical operator, return a Boolean result based on sequentially applying the operator to the values in the array.
Examples

    booleans = [True, True, False], operator = "AND"

    True AND True -> True
    True AND False -> False
    return False

    booleans = [True, True, False], operator = "OR"

    True OR True -> True
    True OR False -> True
    return True

    booleans = [True, True, False], operator = "XOR"

    True XOR True -> False
    False XOR False -> False
    return False

Input

    an array of Boolean values (1 <= array_length <= 50)
    a string specifying a logical operator: "AND", "OR", "XOR"

Output

A Boolean value (True or False).
'''
