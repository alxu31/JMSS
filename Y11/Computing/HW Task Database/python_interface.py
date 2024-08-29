import sqlite3

#! Functioning teacher user, pass: mare, k5RkwSyfcu
#! Functioning student user, pass: alicej, pass1234
#? Teacher logged in required for queries 6 and 7
#? For query 6, a good task to use is "2"

# Prints basic menu depending on teacher or student
def print_menu(perms) -> None:
    # Display task 6 & 7 if permissions
    if perms:
        print("""
Homework Task Database   
------------------------------------------------------------
1. Quit
2. Subject Info
3. All Tasks
4. Task Average
5. Student Average
6. Scaled Grades
7. Email, User, Pass
-------------------------------------------------------------
    """)
    else:
        print("""
Homework Task Database       
-------------------------------------------------------------
1. Quit
2. Subject Info
3. All Tasks
4. Task Average
5. Student Average
-------------------------------------------------------------
    """)
        
# Prints information given by database depending on how many columns
def print_db(bLen, num, info) -> None:
    # Prints each row of info
    for tup in info:
        # Prints every item in the row
        for i in range(bLen//num):
            print(str(tup[i-1]).center(num, " "), end="")
        print()

# Prompts user for login info
def get_login() -> tuple:
    username = input("Username: ")
    password = input("Password: ")
    return username, password

# Checks validity of login info based off of dict from db
def check_login(u, p, all) -> bool:
    try:
        if all[u] == p:
            return True
    except(KeyError):
        pass
    return False

# Queries database using sql as a parameter
def query(sql) -> list:
    DB = "hw_task.db"
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    
    cursor.execute(sql)
    records = cursor.fetchall()
    conn.close()
    return records

# Queries database depending on command
def get_info(cmd) -> list:
    # Queries 2,3,4,5&7
    options = {
2:f"""SELECT Subject.Name, Teacher.Name
FROM Teacher, Subject
WHERE Teacher.teacherID = Subject.teacherID
ORDER BY Subject.subjectID;
""",
3:f"""
SELECT Task.title, subject.Name, Task.dueDate
FROM Task, Subject
WHERE Task.subjectID = subject.SubjectID
ORDER BY CONCAT(
	SUBSTR(Task.dueDate, 7, 4),
	SUBSTR(Task.dueDate, 4, 2),
	SUBSTR(Task.dueDate, 1, 2));
""",
4:f"""SELECT ROUND(AVG(Allocation.grade),2), Subject.Name, Task.title
FROM Allocation, Task, Subject
WHERE Allocation.taskID = Task.taskID
AND Task.subjectID = Subject.subjectID
GROUP BY Allocation.taskID;
""",
5:f"""
SELECT Student.Name, ROUND(AVG(Allocation.grade),2), Student.studentID
FROM Allocation, Student
WHERE Allocation.studentID = Student.studentID
GROUP BY Allocation.studentID
ORDER BY ROUND(AVG(Allocation.grade),2) DESC;
""",
7:f"""WITH const AS (SELECT "@jmss.vic.edu.au" AS suffix)
SELECT Student.loginUser AS "user", Student.loginPass, CONCAT(Student.loginUser, const.suffix), Student.studentID
FROM Student, const;
"""
    }
    # Query 6 requires second prompt for specific task
    if cmd == 6:
        task = int(input("Which task: "))
        sixSql = f"""SELECT Allocation.grade, ROUND(SQRT(Allocation.grade)*10, 2), Student.Name
FROM Allocation, Student
WHERE Allocation.taskID = "{task}"
AND Allocation.studentID = Student.studentID;
"""
        # Queries database and returns info to print_info function
        return query(sixSql)
    else:
        return query(options[cmd])

# Prints all information depending on command number
def print_info(cmd) -> None:
    info = get_info(cmd)
    bLen = 60
    # Number of characters each column should take up per row based on num of columns
    two = bLen//2
    three = bLen//3
    four = bLen//4
    # Separation bar
    bar = "-"*bLen
    # Titles corresponsing to queries
    titles = {2:"Subject Info", 3:"All Tasks", 4: "Task Average", 5:"Student Average", 6:"Scaled Grades", 7:"Email, User, Pass"}
    print(bar)
    try:
        print(titles[cmd].center(bLen, " "))
    except(KeyError):
        pass

    # Formatting for each output
    if cmd == 2:
        print("Teacher".center(two, " "), end="")
        print("Subject".center(two, " "))
        print(bar)
        print_db(bLen, two, info)
    elif cmd == 3:
        print("Due Date".center(three, " "), end="")
        print("Task".center(three, " "), end="")
        print("Subject".center(three, " "))
        print(bar)
        print_db(bLen, three, info)
    elif cmd == 4:
        print("Task".center(three, " "), end="")
        print("Average".center(three, " "), end="")
        print("Subject".center(three, " "))
        print(bar)
        print_db(bLen, three, info)
    elif cmd == 5:
        print("ID".center(three, " "), end="")
        print("Student".center(three, " "), end="")
        print("Average".center(three, " "))
        print(bar)
        print_db(bLen, three, info)
    elif cmd == 6 and permissions:
        print("Name".center(three, " "), end="")
        print("Raw".center(three, " "), end="")
        print("Scaled".center(three, " "))
        print(bar)
        print_db(bLen, three, info)
    elif cmd == 7 and permissions:
        print("ID".center(four, " "), end="")
        print("User".center(four, " "), end="")
        print("Pass".center(four, " "), end="")
        print("Email".center(four, " "))
        print(bar)
        print_db(bLen, four, info)
    # Deny access if task 6 & 7 and no permissions
    else:
        print(bar)
        print("You do not have the permissions to view this.")

# Main code
if __name__ == '__main__':
    # By default, no permissions and not logged in
    permissions = False
    loggedIn = False
    # Loop if logged out
    while not loggedIn:
        position = input("Are you a teacher or student? ")
        if position == "teacher":
            username, password = get_login()
            # Gets dict of valid logins for teachers from db
            userPass = dict(query("""SELECT loginUser, loginPass
FROM Teacher;"""))
            # Checks user login against valid logins
            loggedIn = check_login(username, password, userPass)
            if loggedIn:
                # Teachers have permissions
                permissions = True
            else:
                print("Wrong username or password.")
        elif position == "student":
            username, password = get_login()
            # Gets dict of valid logins for students from db
            userPass = dict(query("""SELECT loginUser, loginPass
FROM Student;"""))
            # Checks user login against valid logins
            loggedIn = check_login(username, password, userPass)
            if not loggedIn:
                print("Wrong username or password.")
        # Not student or teacher
        else:
            print("That is not a valid position.")
    
    # Interface for database
    while True:
        print_menu(permissions)
        cmd = int(input("Enter command number: "))
        # Quit program
        if cmd == 1:
            print("Logged out.")
            break
        # Print the info for the command if valid command
        elif cmd > 1 and cmd < 8:
            print_info(cmd)
