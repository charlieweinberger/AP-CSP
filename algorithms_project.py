import requests
import datetime

data = requests.get("https://sheetdb.io/api/v1/q1i98nk7tufs9").json()
new_data = sorted(data, key = lambda x: int(x['Importance']))[::-1]

print('\noriginal data: ')

for assignment in new_data:
    print(f'{assignment}')

# FIRST, WRITE A COMMENT DESCRIBING YOUR ALGORITHM. HOW WILL YOUR ALGORITHM WORK? WHAT IS THE HEURISTIC YOU ARE USING? WHAT HAPPENS WHEN YOU HAVE TOO MUCH HOMEWORK AND NOT ENOUGH MINUTES? WHAT HAPPENS WHEN YOU HAVE ENOUGH MINUTES TO COMPLETE AN ASSIGNMENT HALFWAY, BUT NOT COMPLETELY? WALK ME THROUGH AN EXAMPLE WITH A FEW ASSIGNMENTS.  

# NEXT, WRITE YOUR ALGORITHM OUT IN PSEUDOCODE.

# FINALLY, IMPLEMENT YOUR ALGORITHM! IF YOU FINISH, THINK ABOUT HOW TO OPTIMIZE YOUR ALGORITHM! MAYBE ADD A "I DONT WANT TO" OPTION TO PUSH YOUR HOMEWORK TO THE NEXT DAY OR A "STAY UP LATE" TO FINISH A PRIORITY ASSIGNMENT.

# today

def assignment_planner(input_data, days_ahead):

    for day in range(days_ahead + 1):

        todays_date = datetime.datetime.now().strftime("%x")
        date = (datetime.datetime.now() + datetime.timedelta(days=day)).strftime("%x")
        available_time = int(input(f"\nToday's date: {todays_date}\nHow many minutes do you have to do homework on {date}? "))
        taken_time = 0
        assignments_to_to = []

        for i in range(len(input_data)):

            i -= len(assignments_to_to)
            assignment = input_data[i]

            if taken_time + int(assignment['Time Needed']) <= available_time:
                
                assignments_to_to.append(assignment)
                taken_time += int(assignment['Time Needed'])
                input_data.remove(assignment)

        if len(input_data) == 0:
            print(f'You have no assignments to do on {date}')
            return
        else:
        
            print(f'\nAssignments to do on {date}: ')
            for assignment in assignments_to_to:
                print(f'{assignment["Class"]} - {assignment["Assignment"]} - {assignment["Due Date"]}')
    
    if len(input_data) != 0:
        after_date = (datetime.datetime.now() + datetime.timedelta(days = days_ahead)).strftime("%x")
        print(f'\nOther assignments to do after {after_date}:')
        for assignment in input_data:
            print(f'{assignment["Class"]} - {assignment["Assignment"]} - {assignment["Due Date"]}')
    
    print('')

assignment_planner(new_data, 2)