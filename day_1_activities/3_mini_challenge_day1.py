# Project Prompt:

# You are hired to build a Student Lookup Tool for a school front office. The secretary must be able to:

    # Enter a student’s full name

    # Instantly see:

            # CPS ID

            # Homeroom

            # Grade Level

            # Primary Email

            # Students must:

            # Describe the search process

## be able to add new data
# Your program must allow the secretary to ADD a brand new student
# into the system while the program is running.

# Your job is to let the secretary type in a new student just like filling out a registration form.
# Once the form is complete, your program must turn that information into a dictionary and add it to the main list of students.
# If the student already exists (same CPS ID), your program must block the entry to prevent duplicates.

# The program should:
    # 1. Ask the user for the following information:
    #    - CPS ID
    #    - First Name
    #    - Last Name
    #    - Middle Name
    #    - Homeroom
    #    - Grade Level
    #    - Primary Email
    #    - Secondary Email

# 2. Combine the First and Last name into this format:
    #    "Last, First"  

# 3. Store all of the new information into ONE dictionary
    #    that matches the structure of the existing student data.

# 4. Add (append) that new dictionary into the main students list.

# 5. After adding the student, the program must:
    #    - Print a confirmation message
    #    - Print the total number of students in the system
    #    - Print the newly added student record

# 6. The program must NOT delete or overwrite any existing students.

# 7. If the CPS ID already exists in the system:
        #    - Do NOT add the student
        #    - Display an error message saying the CPS ID is already taken

students = [{
    "CPSID": 10000011,
    "Combo,Name": "Llamas, Zahid",
    "LName": "Llamas",
    "FName": "Zahid",
    "MName": "Gilbert",
    "HR": "B311",
    "GL": 10,
    "Email": ["Zahidllamas@example.com", "Zahid.L@example.net"]
}, {
    "CPSID": 10000012,
    "Combo,Name": "Martinez, Gael",
    "LName": "Martinez",
    "FName": "Gael",
    "MName": "Gilgeous",
    "HR": "B412",
    "GL": 10,
    "Email": ["Gaelmartinez@example.com", "gg.martinez@example.net"]
}, {
    "CPSID": 10000013,
    "Combo,Name": "Angel, Rosales",
    "LName": "Angel",
    "FName": "Rosales",
    "MName": "Franciso",
    "HR": "B213",
    "GL": 10,
    "Email": ["Arosales@example.com", "Arosales6229@example.net"]
}, {
    "CPSID": 10000014,
    "Combo,Name": "Hernandez, Noah",
    "LName": "Hernandez",
    "FName": "Noah",
    "MName": "Peter",
    "HR": "B214",
    "GL": 10,
    "Email": ["noahhernandez@example.com", "noah.hdz@example.net"]
}, {
    "CPSID": 10000015,
    "Combo,Name": "Lopez, Olivia",
    "LName": "Lopez",
    "FName": "Olivia",
    "MName": "Quinn",
    "HR": "B215",
    "GL": 10,
    "Email": ["olivialopez@example.com", "olivia.lop@example.net"]
}, {
    "CPSID": 10000016,
    "Combo,Name": "King, Paul",
    "LName": "King",
    "FName": "Paul",
    "MName": "Robert",
    "HR": "B216",
    "GL": 10,
    "Email": ["paulking@example.com", "p.king@example.net"]
}, {
    "CPSID": 10000017,
    "Combo,Name": "Clark, Quinn",
    "LName": "Clark",
    "FName": "Quinn",
    "MName": "Stella",
    "HR": "B217",
    "GL": 10,
    "Email": ["quinnclark@example.com", "quinn.cl@example.net"]
}, {
    "CPSID": 10000018,
    "Combo,Name": "Young, Rachel",
    "LName": "Young",
    "FName": "Rachel",
    "MName": "Tara",
    "HR": "B218",
    "GL": 10,
    "Email": ["rachelyoung@example.com", "r.young@example.net"]
}, {
    "CPSID": 10000019,
    "Combo,Name": "Walker, Steve",
    "LName": "Walker",
    "FName": "Steve",
    "MName": "Ulysses",
    "HR": "B219",
    "GL": 10,
    "Email": ["stevewalker@example.com", "steve.walk@example.net"]
}, {
    "CPSID": 10000020,
    "Combo,Name": "White, Tina",
    "LName": "White",
    "FName": "Tina",
    "MName": "Violet",
    "HR": "B220",
    "GL": 10,
    "Email": ["tinawhite@example.com", "tina.w@example.net"]
}, {
    "CPSID": 10000021,
    "Combo,Name": "Adams, Uriel",
    "LName": "Adams",
    "FName": "Uriel",
    "MName": "William",
    "HR": "B221",
    "GL": 10,
    "Email": ["urieladams@example.com", "uriel.ad@example.net"]
}, {
    "CPSID": 10000022,
    "Combo,Name": "Bennett, Victoria",
    "LName": "Bennett",
    "FName": "Victoria",
    "MName": "Xena",
    "HR": "B222",
    "GL": 10,
    "Email": ["victoriabennett@example.com", "vicky.b@example.net"]
}, {
    "CPSID": 10000023,
    "Combo,Name": "Carter, Wyatt",
    "LName": "Carter",
    "FName": "Wyatt",
    "MName": "Yale",
    "HR": "B223",
    "GL": 10,
    "Email": ["wyattcarter@example.com", "wyatt.c@example.net"]
}, {
    "CPSID": 10000024,
    "Combo,Name": "Dixon, Ximena",
    "LName": "Dixon",
    "FName": "Ximena",
    "MName": "Zara",
    "HR": "B224",
    "GL": 10,
    "Email": ["ximenadixon@example.com", "ximena.d@example.net"]
}, {
    "CPSID": 10000025,
    "Combo,Name": "Evans, Yosef",
    "LName": "Evans",
    "FName": "Yosef",
    "MName": "Aaron",
    "HR": "B225",
    "GL": 10,
    "Email": ["yosefevans@example.com", "yosef.e@example.net"]
}, {
    "CPSID": 10000026,
    "Combo,Name": "Flores, Zoe",
    "LName": "Flores",
    "FName": "Zoe",
    "MName": "Brian",
    "HR": "B226",
    "GL": 10,
    "Email": ["zoeflores@example.com", "zoe.f@example.net"]
}, {
    "CPSID": 10000027,
    "Combo,Name": "Green, Alan",
    "LName": "Green",
    "FName": "Alan",
    "MName": "Charlie",
    "HR": "B227",
    "GL": 10,
    "Email": ["alangreen@example.com", "alan.g@example.net"]
}, {
    "CPSID": 10000028,
    "Combo,Name": "Hill, Bella",
    "LName": "Hill",
    "FName": "Bella",
    "MName": "Diane",
    "HR": "B228",
    "GL": 10,
    "Email": ["bellahill@example.com", "bella.h@example.net"]
}, {
    "CPSID": 10000029,
    "Combo,Name": "Irwin, Carl",
    "LName": "Irwin",
    "FName": "Carl",
    "MName": "Edward",
    "HR": "B229",
    "GL": 10,
    "Email": ["carlirwin@example.com", "carl.i@example.net"]
}, {
    "CPSID": 10000030,
    "Combo,Name": "Jones, Donna",
    "LName": "Jones",
    "FName": "Donna",
    "MName": "Francine",
    "HR": "B230",
    "GL": 10,
    "Email": ["donnajones@example.com", "donna.j@example.net"]
}, {
    "CPSID": 10000031,
    "Combo,Name": "Knight, George",
    "LName": "Knight",
    "FName": "George",
    "MName": "Henry",
    "HR": "B231",
    "GL": 10,
    "Email": ["georgeknight@example.com", "g.knight@example.net"]
}, {
    "CPSID": 10000032,
    "Combo,Name": "Lowe, Hannah",
    "LName": "Lowe",
    "FName": "Hannah",
    "MName": "Isabel",
    "HR": "B232",
    "GL": 10,
    "Email": ["hannahlowe@example.com", "h.lowe@example.net"]
}, {
    "CPSID": 10000033,
    "Combo,Name": "Morris, Ian",
    "LName": "Morris",
    "FName": "Ian",
    "MName": "James",
    "HR": "B233",
    "GL": 10,
    "Email": ["ianmorris@example.com", "ian.m@example.net"]
}, {
    "CPSID": 10000034,
    "Combo,Name": "Nash, Julia",
    "LName": "Nash",
    "FName": "Julia",
    "MName": "Kate",
    "HR": "B234",
    "GL": 10,
    "Email": ["julianash@example.com", "j.nash@example.net"]
}, {
    "CPSID": 10000035,
    "Combo,Name": "Owens, Kevin",
    "LName": "Owens",
    "FName": "Kevin",
    "MName": "Leon",
    "HR": "B235",
    "GL": 10,
    "Email": ["kevinowens@example.com", "k.owens@example.net"]
}, {
    "CPSID": 10000036,
    "Combo,Name": "Perry, Lisa",
    "LName": "Perry",
    "FName": "Lisa",
    "MName": "Marie",
    "HR": "B236",
    "GL": 10,
    "Email": ["lisaperry@example.com", "l.perry@example.net"]
}, {
    "CPSID": 10000037,
    "Combo,Name": "Quinn, Mark",
    "LName": "Quinn",
    "FName": "Mark",
    "MName": "Nathan",
    "HR": "B237",
    "GL": 10,
    "Email": ["markquinn@example.com", "m.quinn@example.net"]
}, {
    "CPSID": 10000038,
    "Combo,Name": "Reed, Olivia",
    "LName": "Reed",
    "FName": "Olivia",
    "MName": "Paige",
    "HR": "B238",
    "GL": 10,
    "Email": ["oliviareed@example.com", "olivia.r@example.net"]
}, {
    "CPSID": 10000039,
    "Combo,Name": "Scott, Peter",
    "LName": "Scott",
    "FName": "Peter",
    "MName": "Quentin",
    "HR": "B239",
    "GL": 10,
    "Email": ["peterscott@example.com", "p.scott@example.net"]
}, {
    "CPSID": 10000040,
    "Combo,Name": "Turner, Quinn",
    "LName": "Turner",
    "FName": "Quinn",
    "MName": "Rachel",
    "HR": "B240",
    "GL": 10,
    "Email": ["quinnt@example.com", "q.turner@example.net"]
}, {
    "CPSID": 10000041,
    "Combo,Name": "Upton, Sam",
    "LName": "Upton",
    "FName": "Sam",
    "MName": "Thomas",
    "HR": "B241",
    "GL": 10,
    "Email": ["samupton@example.com", "s.upton@example.net"]
}, {
    "CPSID": 10000042,
    "Combo,Name": "Vega, Tina",
    "LName": "Vega",
    "FName": "Tina",
    "MName": "Uma",
    "HR": "B242",
    "GL": 10,
    "Email": ["tinavega@example.com", "t.vega@example.net"]
}, {
    "CPSID": 10000043,
    "Combo,Name": "Watson, Uri",
    "LName": "Watson",
    "FName": "Uri",
    "MName": "Victor",
    "HR": "B243",
    "GL": 10,
    "Email": ["uriwatson@example.com", "u.watson@example.net"]
}, {
    "CPSID": 10000044,
    "Combo,Name": "Bryant, Kobe",
    "LName": "Bryant",
    "FName": "Kobe",
    "MName": "Bean",
    "HR": "B244",
    "GL": 10,
    "Email": ["Kobeb@example.com", "KB.Bean@example.net"]
}, {
    "CPSID": 10000045,
    "Combo,Name": "Svenginston, Kaleb",
    "LName": "Sevingston",
    "FName": "Kaleb",
    "MName": "Derrick",
    "HR": "B345",
    "GL": 10,
    "Email": ["Kalebsev@example.com", "KD.Sev@example.net"]
}, {
    "CPSID": 10000046,
    "Combo,Name": "Sandoval, Juan",
    "LName": "Sandoval",
    "FName": "Juan",
    "MName": "Carlos",
    "HR": "B346",
    "GL": 10,
    "Email": ["JuanSandoval@example.com", "JC.Sandoval@example.net"]
}]

cps_id = input("Enter CPS ID: ")

for student in students:
    if student["cps_id"] == cps_id:
        print(" ERROR: CPS ID is already taken.")


