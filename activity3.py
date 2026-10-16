num=(input("enter a number"))
if len(num)>=4:
    mid=len(num)//2
    a=int(num[mid-1])
    b=int(num[mid])
    print("the product of the middle two digits is: ", a*b)
else:
    print("the number entered is not a four digit number")  