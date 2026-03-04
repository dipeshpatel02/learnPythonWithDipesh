str = "Hello,' World!"
print(str)
str1 = 'Python is" great!'
print(str1)
str2 = """This is a multi-line string.
It can span multiple lines."""
print(str2)

str3 = "This is a string with a newline character.\nSee, it goes to the next line."
print(str3)

str4 = "This is a string with a tab character.\tSee, it adds a tab space."
print(str4)

#string concatenation
str5 = "Hello, " + "World!"
print(str5)

#string functions
str6 = "Python programming is fun!"
print("Length of str6:", len(str6))
print("Uppercase str6:", str6.upper())
print("Lowercase str6:", str6.lower())
print("Is 'fun' in str6?", "fun" in str6)
print("Ends with 'fun!'?", str6.endswith("fun!"))
print("Replace 'fun' with 'awesome':", str6.replace("fun", "awesome"))
print("Capitalize str6:", str6.capitalize())
print("Find 'programming' in str6:", str6.find("programming"))
print("Count of 'o' in str6:", str6.count("o"))

#indexing and slicing
str7 = "Hello, World!"
print("First character of str7:", str7[0])
# str7[0] = "h"  # This will raise an error because strings are immutable
print("Last character of str7:", str7[-1])
print("Substring of str7 (0-5):", str7[0:5])
print("substring of str7 (7-last):", str7[7:])



#Take user input and print length of the input string
user_input = input("Enter a string: ")
print("Length of the input string:", len(user_input))

#Take user input and check occurance of a $ in the string
user_input2 = input("Enter another string: ")
print("The number of $ in the input string is:", user_input2.count("$"))

#indentation = 4 spaces is similar to block of code in other programming languages
#Conditional statements
num = 21
if num > 17:
    print("Can able to vote.")
    print("Can able to drive.")
else:
    print("Cannot able to vote.")


trafic_light = "red"
if trafic_light == "red":
    print("Stop")
elif trafic_light == "yellow":
    print("Get ready")
else:   
    print("Go")


#grade calculation
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B") 
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: F")


#nested if statements
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
    if age >= 21:
        print("You are also eligible to drink alcohol.")
    else:
        print("You are not eligible to drink alcohol.")

#Write a program to check if a number is even or odd
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is even.")    
else:    
    print("The number is odd.")

#Write a program to find greatest of three numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: ")) 
if num1 >= num2 and num1 >= num3:
    print("The greatest number is:", num1)
elif num2 >= num1 and num2 >= num3:
    print("The greatest number is:", num2)  
else:   
    print("The greatest number is:", num3)