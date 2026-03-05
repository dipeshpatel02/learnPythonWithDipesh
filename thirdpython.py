#List and tuple
mylist = [1, 2, 3, 4, 5]
mytuple = (1, 2, 3, 4, 5)
print("List:", mylist)
print("Tuple:", mytuple)
print("Length of list:", len(mylist))
print("Length of tuple:", len(mytuple))
print("First element of list:", mylist[0])
print("First element of tuple:", mytuple[0])


student = ["name", 3, 40.10]
print("Student list:", student)

student[1] = 4
print("Updated student list:", student)

#slicing
print("Sliced list (0-2):", mylist[0:2])
print("Sliced tuple (0-2):", mytuple[0:2])


#list and tuple methods
mylist.append(6)
print("List after appending 6:", mylist)
mylist.remove(3)
print("List after removing 3:", mylist)
mylist.sort()
print("Sorted list:", mylist)
mylist.sort(reverse=True)
print("List after sorting in reverse:", mylist)
mylist.reverse()
print("List after reversing:", mylist)
mylist.remove(6)
print("List after removing 6:", mylist)
mylist.pop()
print("List after popping last element:", mylist)


#write a program take three name and sort them in alphabetical order
name1 = input("Enter first name: ")
name2 = input("Enter second name: ")
name3 = input("Enter third name: ")
names = [name1, name2, name3]
names.sort()
print("Names in alphabetical order:", names)


#write a program to check list is pallindrome or not
mylist2 = [1, 2, 3, 2, 1]
mylist3 = mylist2.copy()
mylist3.reverse()
if mylist2 == mylist3:
    print("The list is a palindrome.")
else:
    print("The list is not a palindrome.")

#write a program to count a grade from a tuple of marks
marks_tuple = (85, 90, 78, 92, 88)
count = marks_tuple.count(90)
print("Number of students with grade 90:", count)

