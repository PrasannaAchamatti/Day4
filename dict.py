my_dict={"id":"74","name":"srush","age":21,"place":"munyal"}
print(my_dict.get("id"))
print(my_dict.get("name"))
print(my_dict.get("age"))
print(my_dict.get("name","age"))

my_dict.update({"place":"Belagam"})
print(my_dict.get("place"))
print(my_dict.pop("id"))
print(my_dict.popitem())
my_dict.update({"Branch":"CSE"})
print(my_dict)
print(my_dict['name'])
print(my_dict['Branch'])
my_dict['Branch']="ai"
print(my_dict)
print(list(my_dict.keys()),list(my_dict.values()))
del my_dict["name"]
print(my_dict)

for key, value in my_dict.items():
    print(key,":",value)
print("age:",my_dict["age"])
print("Branch:",my_dict["Branch"])



















contacts = {
    "Alice": "7665551234",
    "Bob": "7435555678",
    "Charlie": "9575559012"
}
contacts["Diana"] = "9845897610"
contacts["Bob"] = "7865478970"
print("Lookup Alice:", contacts.get("Alice", "Contact not found"))
print("Lookup Eve:", contacts.get("Eve", "Contact not found"))
print("\nContact List:")
for name, phone in contacts.items():
    print(f"Contact: {name} | Phone: {phone}")


