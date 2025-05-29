#list every country available
countryPop = { "Japan": 127000000,"Germany": 81000000,"Iran": 77000000,"UK": 64000000,"Canada": 33000000,"Australia": 23000000,"USA": 317000000,"Bulgaria": 7000000,"Sweden": 10000000}

print("list of these countries")
for country in countryPop:
    print(country.title())

#input the first country
country1=input("Enter the first country").lower()

#input the second country
country2=input("Enter the second country").lower()

#Print the total answer
if country1 in countryPop and country2 in countryPop:
    total=countryPop[country]+countryPop[country2]
    print("The total population is " ,(total))
else:
    print("This country is not in this list")
