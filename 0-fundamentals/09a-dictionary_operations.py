# merging dictionaries
defaults_tags = {
    "Environment": "Production",
    "Owner": "Finance",
    "CostCenter": "1000"
}

custom_tags = {
    "CostCenter": "12354"
}

# while merging, order matters
merged_tags = defaults_tags | custom_tags
print (merged_tags)
merged_tags2 = custom_tags | defaults_tags
print (merged_tags2)

# update dictionary
defaults_tags.update(custom_tags)
print (defaults_tags)

# create new dictionary based on a set of keys
new_dict = dict.fromkeys(['one', 'two', 'one'], 0)
print (new_dict)

# clear dictionary
new_dict.clear()
print(new_dict)

# adding and updating items
tags = {
    "Environment": "Production",
    "Owner": "Finance",
    "CostCenter": "1000"
}

tags ["CostCenter"] = "2137"
tags ["Projects"] = "Testing"
print (tags)