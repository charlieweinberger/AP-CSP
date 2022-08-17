age = input("When is your birthday? (MM/DD/YYYY) ")
age = age.split("/")

birth_month = int(age[0][1]) if age[0][0] == '0' else int(age[0])
birth_day = int(age[1][1]) if age[1][0] == '0' else int(age[1])
birth_year = int(age[2])

earth_years = 2022 - birth_year + ((8 - birth_month) * 10 / 12) / 10
earth_days = birth_day + 365.26 * earth_years

planet_data = {
    'Mercury': [58.6, 0.241],
    'Venus': [243, 0.615],
    'Earth': [0.99, 1],
    'Mars': [1.03, 1.88],
    'Jupiter': [0.41, 11.86],
    'Saturn': [0.45, 29.46],
    'Uranus': [0.72, 84.01],
    'Neptune': [0.67, 164.79],
    'Pluto': [6.39, 248.59]
}

for planet, data in planet_data.items():
    days  = round(earth_days  / data[0], 2)
    years = round(earth_years / data[1], 2)
    print(f"Your age on {planet} is {days} days, or {years} years.")