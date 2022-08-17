age = input("When is your birthday? (MM/DD/YYYY) ")
age = age.split("/")

birth_month = int(age[0][1]) if age[0][0] == '0' else int(age[0])
birth_day = int(age[1][1]) if age[1][0] == '0' else int(age[1])
birth_year = int(age[2])

earth_years = 2022 - birth_year + ((8 - birth_month) * 10 / 12) / 10
earth_days = birth_day + 365.26 * earth_years

print(earth_years)
print(earth_days)

planet_data = {
    'Mercury': [58.6, 87.97],
    'Venus': [],
    'Earth': [],
    'Mars': [],
    'Jupiter': [],
    'Saturn': [],
    'Uranus': [],
    'Neptune': []
}

mercury_days = round(earth_days / 58.6, 2)
mercury_years = round(earth_years * 365.26 / 87.97, 2)

print(mercury_days)
print(mercury_years)