# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

sampledict = {
    "name": "kelly",
    "age":25,
    "salary": 8000,
    "city": "new york"


}

new_key = "location"
old_key = "city"
sampledict[new_key] = sampledict.pop(old_key)
print(sampledict)