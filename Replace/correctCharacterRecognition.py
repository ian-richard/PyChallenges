# Description:

# Character recognition software is widely used to digitise printed texts. Thus the texts can be edited, searched and stored on a computer.

# When documents (especially pretty old ones written with a typewriter), are digitised character recognition softwares often make mistakes.

# Your task is correct the errors in the digitised text. You only have to handle the following mistakes:

#     S is misinterpreted as 5
#     O is misinterpreted as 0
#     I is misinterpreted as 1

# The test cases contain numbers only by mistake.

def correct(string):
    return string.replace('1','I').replace('0','O').replace('5','S')

# def correct(string):
#     return string.translate(str.maketrans("501", "SOI"))
# https://www.w3schools.com/python/ref_string_maketrans.asp

print(correct("1F-RUDYARD K1PL1NG") == "IF-RUDYARD KIPLING")
print(correct("R0BERT MERLE - THE DAY 0F THE D0LPH1N") =="ROBERT MERLE - THE DAY OF THE DOLPHIN")
