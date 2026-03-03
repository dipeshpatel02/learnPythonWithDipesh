name = "Dipesh"
age = 22
price = 100.5
boolean_value = True
a=None
print("My name is", name)
print("I am", age, "years old") 
print("The price is", price)
print("Boolean value is", boolean_value)
print("The value of a is", a)

print(type(name))  # Output: <class 'str'>
print(type(age))   # Output: <class 'int'>  
print(type(price)) # Output: <class 'float'>
print(type(boolean_value))  # Output: <class 'bool'>
print(type(a))  # Output: <class 'NoneType'>


#Sum of two numbers
num1 = 10
num2 = 20
sum = num1 + num2
print("The sum of", num1, "and", num2, "is", sum)

#subtraction of two numbers
difference = num1 - num2
print("The difference between", num1, "and", num2, "is", difference)
#Multiplication of two numbers
product = num1 * num2   
print("The product of", num1, "and", num2, "is", product)
#Division of two numbers        
quotient = num1 / num2
print("The quotient of", num1, "and", num2, "is", quotient)
#Modulus of two numbers
modulus = num1 % num2
print("The modulus of", num1, "and", num2, "is", modulus)
#Exponentiation of two numbers
exponentiation = num1 ** num2
print("The exponentiation of", num1, "and", num2, "is", exponentiation)

#operators
a = 10
b = 5
print("is a equal to b ", a == b) 
print("is a not equal to b ", a != b)
print("is a greater than b ", a > b)
print("is a less than b ", a < b)


#assignment operators
x = 10
x += 5  # Equivalent to x = x + 5
print("After += operator, x =", x)
x -= 3  # Equivalent to x = x - 3
print("After -= operator, x =", x)
x *= 2  # Equivalent to x = x * 2
print("After *= operator, x =", x)
x /= 4  # Equivalent to x = x / 4
print("After /= operator, x =", x)
x %= 3  # Equivalent to x = x % 3
print("After %= operator, x =", x)

#logical operators
p = True
q = False
print("p and q is", p and q)  # Output: False
print("p or q is", p or q)   # Output: True
print("not p is", not p)     # Output: False


#type conversion
num_float = 3.14
num_int = 3
sum = num_float + num_int
print("The value is", sum)
print("The type value is", type(sum))

#type casting
num_str = "100"
num_int = int(num_str)
print("The integer value is", num_int)
print("The type of num_int is", type(num_int))


#input function
name = input("Enter your name: ")
print("Hello, " + name + "! Welcome to Python programming.")
print("The type of name is", type(name))
number = input("Enter a number: ")
print("You entered the number:", number)
print("The type of number is", type(number))

#input function with type conversion
num1 = int(input("Enter the first number: "))
print("The first number is", num1)
print("The type of num1 is", type(num1))


#area of square
side = float(input("Enter the length of the side of the square: "))
area_square = side ** 2
print("The area of the square is:", area_square)
