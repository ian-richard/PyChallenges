def sum (x=0, y=[]):
    y.append(x)
    if (len(y) % 2 == 0):
         return ("Even")
    else:
        return ("Odd")

print(sum(), "1") 
print(sum(1), "2") ##odd or even?