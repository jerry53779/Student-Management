import mysql.connector as sql
con=sql.connect(host='localhost',user='root',passwd='root')
cur=con.cursor()
print("\n\n\t\t\t\t\t \033[1m Collage Mannagement System \033[0m")
cur.execute("CREATE DATABASE IF NOT EXISTS MANAGEMENT;")
cur.execute("USE MANAGEMENT;")
cur.execute("CREATE TABLE IF NOT EXISTS DETAILS(ROLL_NUM INT(4) PRIMARY KEY,NAME VARCHAR(20),EMAIL_ID VARCHAR(30));")
def append():
    n = int(input("\n\n\nEnter the Number of student details that you want to enter: "))
    for i in range(n):
        roll = int(input("\nEnter the Roll Number of the student: "))
        name = input("\nEnter the Name of the student: ")
        email = input("\nEnter the email id of the student: ")
        cur.execute("INSERT INTO DETAILS VALUES (%s,%s,%s);", (roll, name, email))
        con.commit()
    cur.execute("SELECT * FROM DETAILS WHERE ROLL_NUM = %s",(roll,))
    rows = cur.fetchall()
    for row in rows:
        print(row)

def drop():
    n = int(input("\n\n\nEnter the Number of student details that you want to enter: "))
    for i in range(n):
        roll = int(input("Enter the roll number of the student that you want to drop: "))
        cur.execute("DELETE FROM DETAILS WHERE ROLL_NUM = %s", (roll,))
        con.commit()
    print("The Student(s) Details with the entered roll number(s) are deleted")

def edit():
    n = int(input("\n\n\nEnter the Number of student details that you want to enter: "))
    for i in range(n):
        roll = int(input("Enter the id that you want to edit: "))
        name = input("Enter the New Name: ")
        email = input("Enter the new email id: ")
        cur.execute("UPDATE DETAILS SET NAME=%s, EMAIL_ID=%s WHERE ROLL_NUM=%s", (name, email, roll))
        con.commit()
    print("The Details of above Students are Updated")

def display():
    cur.execute("SELECT * FROM DETAILS;")
    rows = cur.fetchall()
    print("The details available are: \n")
    for row in rows:
        print(row)

def search():
    n = int(input("\n\n\nEnter the Number of student details that you want to enter: "))
    for i in range(n):  
        roll=int(input("Enter the roll number of the student to search: "))
        cur.execute("SELECT* FROM DETAILS WHERE ROLL_NUM=%s",(roll,))
        rows = cur.fetchall()
        print("The details available are: \n")
        for row in rows:
            print(row)


def main():
    while True:
        fn = int(input("\n\nChoose which Function you want to execute from below:\n1. ADD DETAILS\n2. REMOVE DETAILS\n3. EDIT DETAILS\n4. SHOW DETAILS\n5. SEARCH \n6. STOP\nEnter the option: "))
        if fn == 1:
            append()
        elif fn == 2:
            drop()
        elif fn == 3:
            edit()
        elif fn == 4:
            display()
        elif fn==5:
            search()
        elif fn == 6:
            break
        else:
            print("Option unavailable !!!!")
main()

con.close()
cur.close()