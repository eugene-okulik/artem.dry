import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor()
cursor.execute("INSERT INTO students (name, second_name) VALUES (%s, %s)", ('Artem', 'Dryamin'))
db.commit()
student_id = cursor.lastrowid
print('Student ID:', student_id)
cursor.execute("INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)",
               ('Best group AQA', 'nov 26', 'apr 26'))
db.commit()
group_id = cursor.lastrowid
print('Group ID:', group_id)
cursor.execute("UPDATE students SET group_id = %s WHERE id = %s", (group_id, student_id))
db.commit()
cursor.execute("INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)", ('BEST AQA', student_id))
db.commit()
cursor.execute("INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)", ('Good Job', student_id))
db.commit()
cursor.execute("INSERT INTO subjects (title) VALUES (%s)", ('Best subject1',))
db.commit()
subject1_id = cursor.lastrowid
cursor.execute("INSERT INTO subjects (title) VALUES (%s)", ('Best subject2',))
db.commit()
subject2_id = cursor.lastrowid
cursor.execute("INSERT INTO lessons (title, subject_id) VALUES (%s, %s)", ('Best lesson1', subject1_id))
lesson1_id = cursor.lastrowid
cursor.execute("INSERT INTO lessons (title, subject_id) VALUES (%s, %s)", ('Best lesson2', subject1_id))
lesson2_id = cursor.lastrowid
cursor.execute("INSERT INTO lessons (title, subject_id) VALUES (%s, %s)", ('Best lesson3', subject2_id))
lesson3_id = cursor.lastrowid
cursor.execute("INSERT INTO lessons (title, subject_id) VALUES (%s, %s)", ('Best lesson4', subject2_id))
lesson4_id = cursor.lastrowid
db.commit()
cursor.execute("INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)", (2, lesson1_id, student_id))
cursor.execute("INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)", (3, lesson2_id, student_id))
cursor.execute("INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)", (4, lesson3_id, student_id))
cursor.execute("INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)", (5, lesson4_id, student_id))
db.commit()
cursor.execute("SELECT * FROM marks WHERE student_id = %s", (student_id,))
print("\nMarks:", cursor.fetchall())
cursor.execute("SELECT * FROM books WHERE taken_by_student_id = %s", (student_id,))
print("\nBooks:", cursor.fetchall())
cursor.execute("""
    SELECT * FROM students s
    LEFT JOIN `groups` g ON s.group_id = g.id
    LEFT JOIN books b ON b.taken_by_student_id = s.id
    LEFT JOIN marks m ON m.student_id = s.id
    LEFT JOIN lessons l ON l.id = m.lesson_id
    LEFT JOIN subjects subj ON subj.id = l.subject_id
    WHERE s.id = %s
""", (student_id,))

print("\nFull info:")
for row in cursor.fetchall():
    print(row)
db.close()
