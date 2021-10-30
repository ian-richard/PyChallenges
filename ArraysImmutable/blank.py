def sum (x=0, y=[]):
    y.append(x)
    if (len(y) % 2 == 0):
         print ("Even")
    else:
        print ("Odd")

print(sum(), "1") 
print(sum(1), "2") ##odd or even?