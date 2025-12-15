# this is what we will use for the video intro to dictionaries
#dictonary = a collection of (keyvalue) pairs
# ordered and changeable . No duplicates

capitals = {"USA": "Washington D.C",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}
# print(dir(capitals))
# print(help(capitals))

# print(capitals.get("USA"))

# if capitals.get("Russia"):
#     print("that capital exists")
# else:
#     print("That capital doesn't exist")

# capitals.update({"Germany": "Berlin"})
# capitals.update({"USA": "Detroit"})
# capitals.pop("China")
# capitals.popitem()
# capitals.clear()
keys = capitals.keys()

# for key in capitals.keys():
#     print(keys)

# values = capitals.values()
# for value in capitals.values():
#     print(value)

for key, value in capitals.item():
    print(f"{key}: {value}")
