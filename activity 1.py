string=input("please enter your own word: ")
char=input("please enter a character to count: ")
i=0
count=0
while i<len(string):
    if string[i]==char:
        count = count + 1
    i+=1
print(" the total number of times the character appears in the string is: ", count)
