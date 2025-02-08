
def factorial(n):
    if(n<0 or n==1):
        return 1
    else:
        return n * factorial(n-1)
  
x = int(input(" Enter the number to find the factorial : "))
y = factorial(x)
a = input( " Enter a :")
print(f" The fact of {x} is {y} and {a}")