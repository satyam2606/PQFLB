x,y=input("Enter two numbers with space between them").split()
x,y=int(x),int(y)
x,y=y,x  #swapping rule 1
print("x = {0} and y = {1}".format(x,y))
# swapping rule 2 by addition
#swapping rule 3 by multiplication
#swapping rule 4 for integers only :
x=x^y
y=x^y
x=x^y
print("x = {0} and y = {1}".format(x,y))
