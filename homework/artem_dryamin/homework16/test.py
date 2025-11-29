import csv
import os
import dotenv
import mysql.connector as mysql


path = os.path.dirname(__file__)
base_path = os.path.dirname(os.path.dirname(path))
path_file = os.path.join(base_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')
csv_records = []
with open(path_file, newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        csv_records.append(row)

dotenv.load_dotenv()
db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=int(os.getenv('DB_PORT')),
    database=os.getenv('DB_NAME')
)
cursor = db.cursor()
cursor.execute("""
    SELECT 
        s.name,
        s.second_name,
        g.title AS group_title,
        b.title AS book_title,
        subj.title AS subject_title,
        l.title AS lesson_title,
        m.value AS mark_value
    FROM students s
    LEFT JOIN `groups` g ON s.group_id = g.id
    LEFT JOIN books b ON b.taken_by_student_id = s.id
    LEFT JOIN marks m ON m.student_id = s.id
    LEFT JOIN lessons l ON l.id = m.lesson_id
    LEFT JOIN subjects subj ON subj.id = l.subject_id
""")
columns = [desc[0] for desc in cursor.description]
db_records = []
for row in cursor.fetchall():
    db_record = {}
    for col, val in zip(columns, row):
        db_record[col] = val if val is not None else ''
    db_records.append(db_record)


def make_key(rec):
    return (
        rec['name'],
        rec['second_name'],
        rec['group_title'],
        rec['book_title'],
        rec['subject_title'],
        rec['lesson_title'],
        str(rec['mark_value'])
    )


csv_keys = {make_key(r) for r in csv_records}
db_keys = {make_key(r) for r in db_records}

missing_in_db = csv_keys - db_keys

if missing_in_db:
    print("Есть в файле, но нет бд:")
    for key in sorted(missing_in_db):
        name, second_name, group, book, subject, lesson, mark = key
        print(f"  {name} {second_name}, группа: {group}, книга: '{book}', "
              f"предмет: '{subject}', урок: '{lesson}', оценка: {mark}")
else:
    print("Все данные из файла присутствуют в базе.")
db.close()