birth_year = 1992

info_dict = {
    "name": "Hasnat", # key: value
    "age": 27,
    "location": "MIRPUR DOHS",
    "bith_year": birth_year
}

info_dict["name"] = "Abdullah"

print(info_dict["name"])
print(info_dict["age"])
print(info_dict)
print(info_dict.items())

for key,value in info_dict.items():
    print(f"{key}->{value}")

info_dict.pop("name")
print(info_dict)