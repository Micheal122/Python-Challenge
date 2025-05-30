#list all the height of weight of e5 people
heightandweight = ["James", 73, 1.82, "Peter", 78, 1.80, "Jay", "Beth", 65, 1.53, "Mags", 66, 1.50, "Joy", 62, 1.34]

#write the file
with open ("example.txt", "wt") as person:
    for item in heightandweight:
        person.write(str(item) + "\n")
    person.close()

#print the height and weight
print(heightandweight)