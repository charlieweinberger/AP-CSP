# WEEKLY ORGANIZER
 
import requests
import datetime

data = requests.get("https://sheetdb.io/api/URLINKHERE").json()

today = [datetime.datetime.now().strftime("%x")]
today.append(int(input("How many minutes do you have to do homework today?")))

tomorrow = [(datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%x")]
tomorrow.append(int(input("How many minutes do you have to do homework tomorrow?")))

dayafter = [(datetime.datetime.now() + datetime.timedelta(days=2)).strftime("%x")]
dayafter.append(int(input("How many minutes do you have to do homework the day after?")))

# FIRST, WRITE A COMMENT DESCRIBING YOUR ALGORITHM. HOW WILL YOUR ALGORITHM WORK? WHAT IS THE HEURISTIC YOU ARE USING? WHAT HAPPENS WHEN YOU HAVE TOO MUCH HOMEWORK AND NOT ENOUGH MINUTES? WHAT HAPPENS WHEN YOU HAVE ENOUGH MINUTES TO COMPLETE AN ASSIGNMENT HALFWAY, BUT NOT COMPLETELY? WALK ME THROUGH AN EXAMPLE WITH A FEW ASSIGNMENTS.  

# NEXT, WRITE YOUR ALGORITHM OUT IN PSEUDOCODE.

# FINALLY, IMPLEMENT YOUR ALGORITHM! IF YOU FINISH, THINK ABOUT HOW TO OPTIMIZE YOUR ALGORITHM! MAYBE ADD A "I DONT WANT TO" OPTION TO PUSH YOUR HOMEWORK TO THE NEXT DAY OR A "STAY UP LATE" TO FINISH A PRIORITY ASSIGNMENT.