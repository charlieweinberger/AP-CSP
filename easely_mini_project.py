from datetime import datetime

CURRENT_MONTH = datetime.now().month
CURRENT_YEAR = datetime.now().year

DAYS_IN_YEAR = 365.26
MONTHS_IN_YEAR = 12

planet_data = {
    'Mercury': [58.6, 0.241],
    'Venus': [243, 0.615],
    'Mars': [1.03, 1.88],
    'Jupiter': [0.41, 11.86],
    'Saturn': [0.45, 29.46],
    'Uranus': [0.72, 84.01],
    'Neptune': [0.67, 164.79],
    'Pluto': [6.39, 248.59]
}

age = input("When is your birthday? (MM/DD/YYYY) ")
age = age.split("/")

birth_month = int(age[0][1]) if age[0][0] == '0' else int(age[0])
birth_day   = int(age[1][1]) if age[1][0] == '0' else int(age[1])
birth_year  = int(age[2])

earth_years = CURRENT_YEAR - birth_year + (CURRENT_MONTH - birth_month) / MONTHS_IN_YEAR
earth_days = birth_day + DAYS_IN_YEAR * earth_years

for planet, data in planet_data.items():
    days  = round(earth_days  / data[0], 2)
    years = round(earth_years / data[1], 2)
    print(f"Your age on {planet} is approximately {days} days, or {years} years.")

# add leap years
# add CURRENT_DAY = datetime.now().day to make more accurate