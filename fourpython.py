#dictionary
my_dict = {"name": "Alice", "age": 30, "city": "New York", "hobbies": ["reading", "traveling", "cooking"]}
print("Dictionary:", my_dict)

print("Name:", my_dict["name"])
print("Age:", my_dict["age"])   

my_dict["name"] = "Bob"
my_dict["suraname"] = "Smith"
print("Updated Dictionary:", my_dict)

#nested dictionary
nested_dict = {
    "person1": {"name": "Alice", "age": 30},
    "person2": {"name": "Bob", "age": 25}
}
print("Nested Dictionary:", nested_dict)
print("Person1's name:", nested_dict["person1"]["name"])
print("Person2's age:", nested_dict["person2"]["age"])


#dictionary methods
print("Keys:", my_dict.keys())
print("Values:", my_dict.values())
print("Items:", my_dict.items())
my_dict.pop("age")
print("Dictionary after popping age:", my_dict)
my_dict.clear()
print("Dictionary after clearing:", my_dict)

print("Person1's age:", nested_dict.get("person1", {}).get("age", "Not found"))


#set
my_set = {1, 2, 3, 4, 5, "hello", 4, "hello"}
print("Set:", my_set)
my_set.add(6)
print("Set after adding 6:", my_set)
my_set.remove(3)
print("Set after removing 3:", my_set)
my_set.discard(10)  # No error if element not found
print("Set after discarding 10:", my_set)
my_set.clear()
print("Set after clearing:", my_set)
