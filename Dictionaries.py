# Dictionary: key-value pairs, Unordered, Mutable

my_dict =  {
    "name": "Max",
    "age": 28,
    "city": "New York"
}

mydict2 = dict(name="Mary", age=27, city="Boston")
print(mydict2)

value = my_dict["name"]
print(value)

value = my_dict["lastname"]
print(value)

my_dict["email"] = "max@xyz.com"
print(my_dict)

my_dict["email"] = "coolmax@xyz.com"
print(my_dict)


del my_dict["name"]
print(my_dict)


my_dict.pop("age")
print(my_dict)

my_dict.popitem()
print(my_dict)


if "name" in my_dict:
    (my_dict["name"])


try:
    print(my_dict["name"])
except:
    print("Error")



