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
    "Ak": "7665551234",
    "MS": "7435555678",
    "Vk": "9575559012"
}
contacts["shub"] = "9845897610"
contacts["MS"] = "7865478970"
print("Lookup Ak:", contacts.get("Ak", "Contact not found"))
print("Lookup Dk:", contacts.get("Dk", "Contact not found"))
print("\nContact List:")
for name, phone in contacts.items():
    print(f"Contact: {name} | Phone: {phone}")


