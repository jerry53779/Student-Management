  College Management System
Welcome to the College Management System project! This is a simple Python application that helps manage student details in a college setting using a MySQL database.

Features
Add Student Details: Add new students to the database, including their roll number, name, and email.
Remove Student Details: Remove existing students from the database based on their roll number.
Edit Student Details: Update the name and email of existing students in the database.
Display Student Details: View all the student details stored in the database.
Search Student Details: Search for a specific student by their roll number.
Prerequisites
Python 3
MySQL Database
Setup
Clone this repository to your local machine:
git clone https://github.com/your-username/college-management-system.git

Install the required Python packages:

pip install mysql-connector-python
Make sure you have MySQL installed and running on your machine. You'll need to create a database named MANAGEMENT and a table named DETAILS with the following schema:

sql
CREATE TABLE IF NOT EXISTS DETAILS(
    ROLL_NUM INT(4) PRIMARY KEY,
    NAME VARCHAR(20),
    EMAIL_ID VARCHAR(30)
);
Update the MySQL connection details in the Python script (college_management_system.py) if necessary:

python
con = sql.connect(host='localhost', user='root', passwd='root')
Run the Python script:

Copy code
python college_management_system.py
Usage
Choose an option from the menu:

1: Add Student Details
2: Remove Student Details
3: Edit Student Details
4: Display Student Details
5: Search Student Details
6: Stop
Follow the prompts to perform the selected operation.
