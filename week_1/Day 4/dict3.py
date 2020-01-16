my_info = {
    "name" : "Roxane",
    "dob" : "10/10/2028",
    "school": "Hostos",
    "GPA" : "4.0"
}
name = my_info["name"]
print(name)

if "job" in my_info:
   #print("oups! not in the dictionary")
   pass
for keys in my_info:
    print(keys)
    pass
for value in my_info.values():
    print(value)