a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))
d = int(input("Enter fourth number:"))

if(a>=b, a>=c, a>=d):
    print(a,"is greater")

elif(b>=a, b>=c, b>=d):
    print(b,"is greater")

elif(c>=a, c>=b, c>=d):
    print(c,"is greater")

else:
    print(d,"is greater")