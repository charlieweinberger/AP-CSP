import requests
import datetime

data = requests.get("https://sheetdb.io/api/v1/q1i98nk7tufs9").json()
new_data = sorted(data, key = lambda x: int(x['Importance']))[::-1]

print('\noriginal data: ')

for assignment in new_data:
    print(f'{assignment}')

# FIRST, WRITE A COMMENT DESCRIBING YOUR ALGORITHM. HOW WILL YOUR ALGORITHM WORK? WHAT IS THE HEURISTIC YOU ARE USING? WHAT HAPPENS WHEN YOU HAVE TOO MUCH HOMEWORK AND NOT ENOUGH MINUTES? WHAT HAPPENS WHEN YOU HAVE ENOUGH MINUTES TO COMPLETE AN ASSIGNMENT HALFWAY, BUT NOT COMPLETELY? WALK ME THROUGH AN EXAMPLE WITH A FEW ASSIGNMENTS.  

"""

My algorithm takes in a list of assignments and ranks them based on their priority, and gives you the assignments with the highest priority that you have time for in a day. If you have too many assignments, the algorithm will tell you to do the assignments after a certain number of days (default is 3 days), because you will probably have more time by then. The algorithm assumes you must finish every assignment in one sitting.

"""

# NEXT, WRITE YOUR ALGORITHM OUT IN PSEUDOCODE.

"""

Loop through days ahead

    Get today's date
    set current date to today's date plus days ahead
    Ask the user how much time they have to do homework on the current date

    Loop through assignments

        If there is time to do the current assignemnt
            
            Add current assignment to list of assignments to do on the current date
            add current assignment time to total time spent
            Remove current assignment from list of assignments

    If there are no more assignments to do
        end the algorithm
    otherwise
        print every assignment to do on the current date

If there are still assignments left after looping through all days ahead
    print every remaining assignment

"""

# FINALLY, IMPLEMENT YOUR ALGORITHM! IF YOU FINISH, THINK ABOUT HOW TO OPTIMIZE YOUR ALGORITHM! MAYBE ADD A "I DONT WANT TO" OPTION TO PUSH YOUR HOMEWORK TO THE NEXT DAY OR A "STAY UP LATE" TO FINISH A PRIORITY ASSIGNMENT.

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

assignment_planner(new_data, 4)